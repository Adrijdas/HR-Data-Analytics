# 📊 HR-Data-Analytics

## 📌 Project Overview

This project is an **HR Analytics and Predictive Analytics project** designed to transform employee data into meaningful insights for workforce and HR decision-making.

The project combines:

- 👥 Workforce Analytics
- 💰 Compensation Analytics
- ⭐ Performance Analytics
- 📈 Hiring Trend Analysis
- 📉 Employee Attrition Analysis
- 🤖 Predictive Analytics using Machine Learning
- 📊 Interactive Power BI Dashboard

The primary objective is to understand the current workforce structure and explore whether available HR metrics can be used to predict employee attrition.

---

# 🎯 Project Objectives

The main objectives of this project are to:

- Analyze overall workforce size and employee distribution.
- Monitor active, resigned, and terminated employees.
- Analyze employee attrition.
- Compare salaries across departments and job levels.
- Analyze employee performance.
- Explore hiring trends over time.
- Understand employee distribution across different work modes.
- Analyze workforce distribution by country and department.
- Build a machine learning model to predict employee attrition.
- Evaluate the predictive model using appropriate classification metrics.
- Present HR insights through an interactive Power BI dashboard.
- Generate practical recommendations for HR decision-making.

---

# 📁 Dataset

The project uses a cleaned HR dataset.

### Main Data Categories

| Category | Variables |
|---|---|
| Employee Information | Age, Country |
| Job Information | Department, Job Level, Work Mode |
| Experience | Experience Years, Tenure Years |
| Compensation | Salary, Salary Band |
| Performance | Performance Score, Performance Rating |
| Hiring | Hire Year |
| Employment | Active, Resigned, Terminated |

The dataset contains employee information across different departments, countries, job levels, work modes, performance categories, and employment statuses.

---

# 📊 Power BI HR Analytics Dashboard

An interactive **Power BI dashboard** was created to provide a consolidated view of the organization's HR metrics.

## 🖥️ Dashboard Preview

![HR Analytics Dashboard](HR_Analytics_Dashboard.png)

---

# 📌 Key Dashboard KPIs

The dashboard displays the following major HR indicators:

| KPI | Value |
|---|---:|
| Total Employees | 20K |
| Active Employees | 17K |
| Attrition Rate | 13.2% |
| Average Salary | 83.39K |
| Median Salary | 80.98K |
| Average Performance | 2.64 |
| Maximum Salary | 280K |
| Minimum Salary | 35K |

These KPI cards provide a quick overview of the organization's workforce, compensation, performance, and attrition situation.

---

# 📈 Dashboard Visualizations

The Power BI dashboard contains several visualizations covering different HR areas.

## 👥 Workforce Analysis

- Total Employees by Department
- Employee Status Distribution
- Employees by Work Mode

## 💰 Compensation Analysis

- Average Salary by Department
- Average Salary by Job Level
- Salary Band Distribution

## ⭐ Performance Analysis

- Employee Performance Distribution
- Average Performance by Department

## 📅 Hiring Analysis

- Hiring Trend by Year

---

# 🎛️ Interactive Filters

The dashboard includes interactive slicers that allow users to analyze specific groups of employees.

Available filters:

- **Department**
- **Job Level**
- **Work Mode**
- **Country**

These filters make it possible to move from overall workforce analysis to more detailed employee-segment analysis.

---

# 🔍 Key HR Insights

The dashboard provides several useful observations:

### Workforce

- The organization has approximately **20K employees**.
- Approximately **17K employees are active**.
- Resigned and terminated employees represent smaller portions of the workforce.

### Compensation

- The average salary is approximately **83.39K**.
- The median salary is approximately **80.98K**.
- Salary levels vary across departments.
- Salary also varies across job levels.

### Performance

- The average performance score is approximately **2.64**.
- The largest employee groups are concentrated in the **Good** and **Satisfactory** performance categories.
- Average performance remains relatively close across departments.

### Workforce Distribution

- Employees are distributed across **On-site, Hybrid, and Remote** work modes.
- The dashboard allows workforce analysis by country and department.

### Hiring

- Hiring volume changes across different years.
- The hiring trend provides a historical view of workforce additions.

---

# 🤖 Week 4 – Predictive Analytics

## Business Problem

Employee attrition is an important HR challenge because unexpected employee turnover can affect workforce planning, productivity, and organizational stability.

The predictive analytics component of this project focuses on the following question:

> **Can available HR metrics be used to predict whether an employee is likely to resign?**

---

# 🎯 Target Variable

The prediction target is a binary variable called **Attrition**.

1 = Resigned
0 = Active

# 🧠 Machine Learning Algorithm

## Logistic Regression

**Logistic Regression** was selected for the attrition prediction problem.

### Why Logistic Regression?

- The target variable is binary.
- It is suitable for classification problems.
- It is simple and easy to interpret.
- It provides probability-based predictions.
- It is appropriate for an introductory HR predictive analytics project.
- It allows the relationship between predictors and attrition to be studied.

---

# 🔎 Predictive Features

The following HR variables were used as predictors:

- Department
- Performance Rating
- Experience Years
- Work Mode
- Salary
- Country
- Age
- Job Level
- Tenure Years
- Performance Score
- Salary Band
- Hire Year

---

# ⚙️ Data Preprocessing

The predictive modeling workflow included the following steps:

1. Filtered the dataset to Active and Resigned employees.
2. Created the binary `Attrition` target variable.
3. Separated numerical and categorical variables.
4. Handled missing values.
5. Standardized numerical variables.
6. Applied one-hot encoding to categorical variables.
7. Split the dataset into training and testing sets using an **80/20 stratified split**.
8. Used balanced class weights because the resigned group is smaller.

---

# 📏 Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- 5-Fold Cross-Validation
- ROC Curve
- Confusion Matrix

## Model Results

| Metric | Result |
|---|---:|
| Accuracy | 0.517 |
| Precision | 0.117 |
| Recall | 0.502 |
| F1-Score | 0.190 |
| ROC-AUC | 0.496 |
| 5-Fold CV ROC-AUC | 0.491 |

---

# 📉 Model Interpretation

The model achieved a **ROC-AUC of approximately 0.50**.

A score close to 0.50 indicates that the model has **very limited ability to distinguish between employees who resign and employees who remain active**.

Therefore, the current Logistic Regression model should be considered a:

> **Baseline academic predictive model rather than a production HR decision-making system.**

The result is still valuable because it demonstrates the complete predictive analytics workflow and identifies a limitation in the available HR data.

The findings suggest that additional and more relevant HR variables may be required to build a stronger attrition prediction model.

---

# 📊 Model Evaluation Visualizations

The project includes the following model evaluation visuals:

### ROC Curve

The ROC curve is used to evaluate the model's ability to distinguish between the two classes.

![ROC Curve](roc_curve.png)

### Confusion Matrix

The confusion matrix shows the number of:

- True Negatives
- False Positives
- False Negatives
- True Positives

![Confusion Matrix](confusion_matrix.png)

These visualizations help communicate the strengths and limitations of the predictive model.

---

# 💡 HR Recommendations

To improve future employee attrition prediction, additional HR variables could be collected, such as:

- Employee Satisfaction
- Employee Engagement
- Overtime
- Absenteeism
- Promotion History
- Recent Salary Changes
- Manager Changes
- Training Participation
- Workload
- Exit Interview Reasons

Additional data could help identify stronger patterns associated with employee turnover.

Any future HR predictive analytics system should also consider:

- Employee privacy
- Data security
- Fairness
- Responsible use of employee information
- HR governance

---

# 🐍 Python Implementation

## Libraries Used


pandas
numpy
scikit-learn
matplotlib

## 🐍 Python Script

The main Python script performs the following tasks:

- Data loading
- Data preprocessing
- Feature transformation
- Train/test split
- Logistic Regression training
- Prediction
- Model evaluation
- Cross-validation
- ROC curve generation
- Confusion matrix generation

---

# 🛠️ Technologies Used

- Power Query
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Microsoft Power BI
- DAX

---

# 🔄 Project Workflow

Raw HR Dataset
       ↓
Data Cleaning & Preparation
       ↓
Descriptive & Statistical Analysis
       ↓
Power BI Dashboard
       ↓
Feature Preparation
       ↓
Logistic Regression Model
       ↓
Model Evaluation
       ↓
HR Insights & Recommendations

# 📚 Project Outcomes

This project demonstrates an end-to-end HR analytics workflow combining both **descriptive analytics** and **predictive analytics**.

## Skills Demonstrated

- Data Cleaning
- Data Analysis
- HR Analytics
- Statistical Analysis
- Data Visualization
- Power BI
- DAX
- Machine Learning
- Classification
- Model Evaluation
- Business Insight Generation

---

# ✅ Conclusion

This HR Analytics project provides a complete view of workforce, compensation, performance, hiring, and employee attrition.

The Power BI dashboard allows HR users to interactively explore important workforce metrics through KPI cards, charts, and filters.

The predictive analytics component demonstrates how Logistic Regression can be applied to an HR problem such as employee attrition.

Although the current model achieved limited predictive performance, this result provides an important analytical conclusion: **the existing HR variables are not sufficient to reliably predict employee resignation**.

The project therefore demonstrates not only how to build a machine learning model, but also how to evaluate its performance, understand its limitations, and convert analytical findings into meaningful HR recommendations.

---

# 👨💻 Author

**Adrij Das**

**HR Analytics | Data Analytics | Predictive Analytics**

---

⭐ **This project was developed as part of an HR Data Analytics learning project focused on applying analytical and predictive techniques to real-world HR problems.**
