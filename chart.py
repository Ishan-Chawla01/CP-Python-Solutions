import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Generate a synthetic dataset
np.random.seed(42)
data = {
    'Age': np.random.normal(loc=35, scale=10, size=200).astype(int),
    'Salary': np.random.normal(loc=50000, scale=15000, size=200),
    'Experience': np.random.normal(loc=8, scale=3, size=200),
    'Department': np.random.choice(
        ['Sales', 'Tech', 'HR', 'Marketing'], size=200
    ),
    'Score': np.random.uniform(50, 100, size=200),
}
df = pd.DataFrame(data)

# Set up a 2x3 grid figure for multiple visual charts
plt.figure(figsize=(15, 10))
plt.suptitle(
    'Comprehensive Data Visualization Dashboard', fontsize=16, fontweight='bold'
)

# 1. Box Plot: Distribution of Salary by Department
plt.subplot(2, 3, 1)
sns.boxplot(x='Department', y='Salary', data=df, palette='Set2')
plt.title('1. Box Plot (Salary by Department)')
plt.xlabel('Department')
plt.ylabel('Salary ($)')

# 2. Histogram: Age Distribution with KDE
plt.subplot(2, 3, 2)
sns.histplot(df['Age'], kde=True, color='teal', bins=15)
plt.title('2. Histogram (Age Distribution)')
plt.xlabel('Age')
plt.ylabel('Frequency')

# 3. Heatmap: Correlation Matrix among Numerical Features
plt.subplot(2, 3, 3)
numeric_df = df[['Age', 'Salary', 'Experience', 'Score']]
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('3. Heatmap (Correlation Matrix)')

# 4. Bar Chart: Average Score per Department
plt.subplot(2, 3, 4)
avg_score = df.groupby('Department')['Score'].mean().reset_index()
plt.bar(
    avg_score['Department'],
    avg_score['Score'],
    color=['#4C72B0', '#DD8452', '#55A868', '#C44E52'],
)
plt.title('4. Bar Chart (Avg Score by Department)')
plt.xlabel('Department')
plt.ylabel('Average Score')

# 5. Scatter Plot: Experience vs. Salary
plt.subplot(2, 3, 5)
plt.scatter(df['Experience'], df['Salary'], alpha=0.7, color='purple')
plt.title('5. Scatter Plot (Experience vs Salary)')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary ($)')

# 6. Pie Chart: Employee Department Share
plt.subplot(2, 3, 6)
dept_counts = df['Department'].value_counts()
plt.pie(
    dept_counts,
    labels=dept_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel'),
)
plt.title('6. Pie Chart (Department Share)')

plt.tight_layout()
plt.show()