import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix, classification_report
)

# Load data
df = pd.read_csv("hr_analytics_clean_dataset.csv")

# Keep active and resigned employees for a clean attrition target.
data = df[df["Status"].isin(["Active", "Resigned"])].copy()
data["Attrition"] = (data["Status"] == "Resigned").astype(int)

# Select useful HR predictors
features = [
    "Department", "Performance_Rating", "Experience_Years", "Work_Mode",
    "salary", "Country", "Age", "Job_Level", "Tenure_Years",
    "Performance_Score", "Salary_Band", "Hire_Year"
]

X = data[features]
y = data["Attrition"]

categorical = [c for c in features if X[c].dtype == "object"]
numeric = [c for c in features if c not in categorical]

# Preprocessing
preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]), numeric),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical)
])

# class_weight="balanced" helps the model pay more attention to the smaller
# resigned group.
model = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    ))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# Evaluate
print("Accuracy :", round(accuracy_score(y_test, y_pred), 3))
print("Precision:", round(precision_score(y_test, y_pred, zero_division=0), 3))
print("Recall   :", round(recall_score(y_test, y_pred, zero_division=0), 3))
print("F1-score :", round(f1_score(y_test, y_pred, zero_division=0), 3))
print("ROC-AUC  :", round(roc_auc_score(y_test, y_prob), 3))

print("\nClassification Report")
print(classification_report(y_test, y_pred, target_names=["No Attrition", "Attrition"]))

# 5-fold cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_auc = cross_val_score(model, X, y, cv=cv, scoring="roc_auc")
print("5-fold CV ROC-AUC:", round(cv_auc.mean(), 3))

# ROC curve
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.figure(figsize=(7, 5))
plt.plot(fpr, tpr, label=f"Logistic Regression (AUC = {roc_auc_score(y_test, y_prob):.3f})")
plt.plot([0, 1], [0, 1], "--", label="Random baseline")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Employee Attrition Prediction")
plt.legend()
plt.tight_layout()
plt.savefig("roc_curve.png", dpi=180)
plt.show()

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5.5, 5))
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Class")
plt.ylabel("Actual Class")
plt.xticks([0, 1], ["No Attrition", "Attrition"])
plt.yticks([0, 1], ["No Attrition", "Attrition"])
for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center", fontsize=13)
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=180)
plt.show()
