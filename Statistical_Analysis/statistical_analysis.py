import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
 
# Load data
df = pd.read_csv("hr_analytics_clean_dataset.csv")
 
numeric_cols = ['salary', 'Age', 'Experience_Years', 'Tenure_Years', 'Performance_Score']
 

# Descriptive statistics (Section 3 of the report)
desc = df[numeric_cols].describe().T
desc['skew'] = df[numeric_cols].skew()
desc['kurtosis'] = df[numeric_cols].kurt()
 
print("=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)
print(desc[['mean', '50%', 'std', 'min', 'max', 'skew', 'kurtosis']].round(2))
 

# Visual exploration (Section 4 of the report)
sns.set_style('whitegrid')
 
# Salary distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['salary'], bins=40, kde=True)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.tight_layout()
plt.savefig('fig1_salary_distribution.png', dpi=150)
plt.close()
 
# Salary by department
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Department', y='salary')
plt.title('Salary by Department')
plt.tight_layout()
plt.savefig('fig2_salary_by_department.png', dpi=150)
plt.close()
 
# Average performance score by department
plt.figure(figsize=(8, 5))
dept_perf = df.groupby('Department')['Performance_Score'].mean().sort_values()
sns.barplot(x=dept_perf.index, y=dept_perf.values)
plt.title('Average Performance Score by Department')
plt.ylabel('Avg. Performance Score')
plt.tight_layout()
plt.savefig('fig3_performance_by_department.png', dpi=150)
plt.close()
 
# Salary vs experience (sampled for clarity)
plt.figure(figsize=(8, 5))
sample = df.sample(n=min(2000, len(df)), random_state=42)
sns.scatterplot(data=sample, x='Experience_Years', y='salary', alpha=0.4)
plt.title('Salary vs. Experience')
plt.tight_layout()
plt.savefig('fig4_salary_vs_experience.png', dpi=150)
plt.close()
 
# Correlation heatmap
plt.figure(figsize=(6, 5))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('fig5_correlation_heatmap.png', dpi=150)
plt.close()
 
# Performance rating distribution
plt.figure(figsize=(8, 5))
order = ['Needs Improvement', 'Satisfactory', 'Good', 'Excellent']
sns.countplot(data=df, x='Performance_Rating', order=order)
plt.title('Performance Rating Distribution')
plt.tight_layout()
plt.savefig('fig6_performance_rating_distribution.png', dpi=150)
plt.close()
 
# Employee status breakdown
plt.figure(figsize=(6, 6))
status_counts = df['Status'].value_counts()
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Employee Status Breakdown')
plt.tight_layout()
plt.savefig('fig7_status_breakdown.png', dpi=150)
plt.close()
print("\nStatus breakdown (%):")
print((status_counts / status_counts.sum() * 100).round(1))
 
# Hiring trend by year
plt.figure(figsize=(9, 5))
hires_per_year = df['Hire_Year'].value_counts().sort_index()
sns.lineplot(x=hires_per_year.index, y=hires_per_year.values, marker='o')
plt.title('Hiring Trend by Year')
plt.xlabel('Year')
plt.ylabel('Employees Hired')
plt.tight_layout()
plt.savefig('fig8_hiring_trend.png', dpi=150)
plt.close()
 

# Inferential statistical analysis
print("\n" + "=" * 60)
print("INFERENTIAL STATISTICAL ANALYSIS (alpha = 0.05)")
print("=" * 60)
 
# One-way ANOVA: Performance Score by Department
groups_dept = [g['Performance_Score'].values for _, g in df.groupby('Department')]
f_stat, p_val = stats.f_oneway(*groups_dept)
print(f"\nANOVA - Performance Score by Department: F = {f_stat:.2f}, p = {p_val:.3f}")
 
# One-way ANOVA: Salary by Job Level
groups_level = [g['salary'].values for _, g in df.groupby('Job_Level')]
f_stat2, p_val2 = stats.f_oneway(*groups_level)
print(f"ANOVA - Salary by Job Level: F = {f_stat2:.2f}, p = {p_val2:.3g}")
print("Mean salary by job level:")
print(df.groupby('Job_Level')['salary'].mean().round(1))
 
# Pearson correlation: Salary vs Experience
r1, p1 = stats.pearsonr(df['salary'], df['Experience_Years'])
print(f"\nPearson - Salary vs. Experience: r = {r1:.3f}, p = {p1:.3f}")
 
# Pearson correlation: Tenure vs Performance Score
r2, p2 = stats.pearsonr(df['Tenure_Years'], df['Performance_Score'])
print(f"Pearson - Tenure vs. Performance Score: r = {r2:.3f}, p = {p2:.3f}")
 
# Welch's t-test: Salary Remote vs On-site
remote = df[df['Work_Mode'] == 'Remote']['salary']
onsite = df[df['Work_Mode'] == 'On-site']['salary']
t_stat, p_t = stats.ttest_ind(remote, onsite, equal_var=False)
print(f"\nWelch's t-test - Salary: Remote vs. On-site: t = {t_stat:.2f}, p = {p_t:.3f}")
 
# Chi-square test: Job Level vs Status
ct = pd.crosstab(df['Job_Level'], df['Status'])
chi2, p_chi, dof, exp = stats.chi2_contingency(ct)
print(f"Chi-square - Job Level vs. Status: chi2 = {chi2:.2f}, p = {p_chi:.3f}")
 

