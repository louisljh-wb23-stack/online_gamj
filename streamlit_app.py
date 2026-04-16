import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# =========================
# TITLE
# =========================
st.title("KNN Decision Boundary (PCA vs LDA)")

# =========================
# LOAD DATA (建议用本地CSV)
# =========================
df = pd.read_csv("online_gaming_behavior_dataset.csv")  

# =========================
# FEATURES & TARGET
# =========================
X = df[['SessionsPerWeek',
        'AchievementsUnlocked',
        'PlayerLevel',
        'AvgSessionDurationMinutes']]

y = df['EngagementLevel']

# =========================
# SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# =========================
# ENCODE
# =========================
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)
y_test_encoded = le.transform(y_test)

class_names = le.classes_

# =========================
# UI
# =========================
n_neighbors = st.slider("Select K", 1, 50, 29)
method_choice = st.selectbox("Method", ["PCA", "LDA"])

# =========================
# MODEL
# =========================
if method_choice == "PCA":
    model = make_pipeline(StandardScaler(), PCA(n_components=2))
else:
    model = make_pipeline(StandardScaler(), LinearDiscriminantAnalysis(n_components=2))

# =========================
# TRANSFORM (train only)
# =========================
model.fit(X_train, y_train_encoded)
X_train_2d = model.transform(X_train)
X_test_2d = model.transform(X_test)

# =========================
# KNN
# =========================
knn = KNeighborsClassifier(
    n_neighbors=n_neighbors,
    metric='manhattan',
    weights='distance'
)

knn.fit(X_train_2d, y_train_encoded)

acc = knn.score(X_test_2d, y_test_encoded)

# =========================
# GRID
# =========================
x_min, x_max = X_test_2d[:, 0].min() - 1, X_test_2d[:, 0].max() + 1
y_min, y_max = X_test_2d[:, 1].min() - 1, X_test_2d[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 300),
    np.linspace(y_min, y_max, 300)
)

grid = np.c_[xx.ravel(), yy.ravel()]
Z = knn.predict(grid).reshape(xx.shape)

# =========================
# PLOT
# =========================
fig, ax = plt.subplots()

cmap = plt.cm.Set1
norm = mpl.colors.BoundaryNorm(
    boundaries=np.arange(-0.5, len(class_names) + 0.5, 1),
    ncolors=len(class_names)
)

ax.contourf(xx, yy, Z, alpha=0.4, cmap=cmap, norm=norm)
ax.scatter(
    X_test_2d[:, 0],
    X_test_2d[:, 1],
    c=y_test_encoded,
    cmap=cmap,
    norm=norm,
    edgecolor='black'
)

ax.set_title(f"{method_choice} + KNN (Test Acc={acc:.2f})")

st.pyplot(fig)

# =========================
# METRIC
# =========================
st.metric("Test Accuracy", f"{acc:.2f}")
