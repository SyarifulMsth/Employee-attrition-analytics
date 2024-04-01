# -*- coding: utf-8 -*-
"""Notebook.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wZqZNwZiidtMYENhwMah-rXDYnPLixSN

# Project Data Science : HR Attrition Rate Analytics

## Business Understanding

Building machine learning model to help Human Resource (HR) Department predict Attrition Rate

## Import necessary libraries
"""

!pip install psycopg2-binary scikit-learn==1.2.2 joblib==1.3.1

import scipy
import joblib
import psycopg2
import sqlalchemy
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

"""## Data Understanding

The dataset used in this machine learning project is [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/). The dataset consists of 1470 records data with 35 features.

| Field                   | Description                                   |
|-------------------------|-----------------------------------------------|
| EmployeeId              | Employee Identifier                           |
| Attrition               | Did the employee attrition? (0=no, 1=yes)    |
| Age                     | Age of the employee                           |
| BusinessTravel          | Travel commitments for the job                |
| DailyRate               | Daily salary                                  |
| Department              | Employee Department                          |
| DistanceFromHome        | Distance from work to home (in km)           |
| Education               | 1-Below College, 2-College, 3-Bachelor, 4-Master, 5-Doctor |
| EducationField          | Field of Education                           |
| EnvironmentSatisfaction | 1-Low, 2-Medium, 3-High, 4-Very High        |
| Gender                  | Employee's gender                            |
| HourlyRate              | Hourly salary                                |
| JobInvolvement          | 1-Low, 2-Medium, 3-High, 4-Very High        |
| JobLevel                | Level of job (1 to 5)                        |
| JobRole                 | Job Roles                                    |
| JobSatisfaction         | 1-Low, 2-Medium, 3-High, 4-Very High        |
| MaritalStatus           | Marital Status                               |
| MonthlyIncome           | Monthly salary                               |
| MonthlyRate             | Monthly rate                                 |
| NumCompaniesWorked      | Number of companies worked at                |
| Over18                  | Over 18 years of age?                       |
| OverTime                | Overtime?                                    |
| PercentSalaryHike       | The percentage increase in salary last year  |
| PerformanceRating       | 1-Low, 2-Good, 3-Excellent, 4-Outstanding    |
| RelationshipSatisfaction| 1-Low, 2-Medium, 3-High, 4-Very High        |
| StandardHours           | Standard Hours                               |
| StockOptionLevel        | Stock Option Level                          |
| TotalWorkingYears       | Total years worked                           |
| TrainingTimesLastYear   | Number of training attended last year        |
| WorkLifeBalance         | 1-Low, 2-Good, 3-Excellent, 4-Outstanding    |
| YearsAtCompany          | Years at Company                             |
| YearsInCurrentRole      | Years in the current role                    |
| YearsSinceLastPromotion | Years since the last promotion               |
| YearsWithCurrManager    | Years with the current manager               |

## Data Preparation

Data preparation follows a series of steps that starts with collecting the right data, followed by cleaning, labeling, and then validation and visualization.

#### Gathering Data
"""

import pandas as pd
df = pd.read_csv("employee_data.csv", encoding='windows-1252')

"""#### Assessing Data"""

pd.set_option('display.max_columns', None)
df.head()

df.describe()

df.shape

df.info()

df.isna().sum()

"""- There is a **missing value** in the Attrition feature (column), so handling is required at the data cleansing stage.
- Features (column) EmployeeCount, Over18, and StandardHours only have one type of value. So this feature can be ignored (**dropout**) because it does not provide additional information (insight).
"""

df = df.drop(['EmployeeId','EmployeeCount', 'Over18', 'StandardHours'], axis=1)

"""#### Data Cleansing"""

# handling missing value
missing_attrition = df[df['Attrition'].isnull()]
missing_attrition.head()

"""In this problem, there are 412 missing values, this data is not too large when compared to the total data (1471).

There are several ways to deal with missing values, namely by dropping, imputation and interpolation methods. In this problem, the **dropping** data method will be used, because losing around 39% of the data is still acceptable in this case.
"""

df = df.dropna(subset=['Attrition'])

df.shape

# Handling duplicate data
print("Jumlah duplikasi: ", df.duplicated().sum())

"""## Exploratory data analysis (EDA)"""

df.info()

"""- There are 7 columns with object types, namely: BusinessTravel, Department, EducationField, Gender, JobRole, MaritalStatus, and Overtime. This column is a categorical feature (non-numerical feature).

- There are 23 numeric columns with int64 data type, namely: Age, DailyRate, DistanceFromHome, Education, EnvironmentSatisfaction, HourlyRate, JobInvolvement, JobLevel, JobSatisfaction, MonthlyIncome, MonthlyRate, NumCompaniesWorked, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany , YearsInCurrentRole, YearsSinceLastPromotion, and YearsWithCurrManager. This is a numerical feature that is the result of a physical measurement.

- There is 1 numeric column with the float64 data type, namely: Attrition. This column is our feature target.
"""

correlation_matrix = df.corr().round(2)
mask = (correlation_matrix.abs() < 0.75) & (correlation_matrix.abs() > -0.75)
correlation_matrix[mask] = np.nan
plt.figure(figsize=(20, 15))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=False)
plt.title('Correlation Matrix of Employee Attrition')
plt.show()

"""Based on the correlation matrix above, several correlations can be seen, such as:
- MonthlyIncome has a strong positive correlation to JobLevel of 0.95.
- MonthlyIncome has a strong positive correlation to TotalWorkingYears of 0.78.
"""

df['Attrition'] = df['Attrition'].replace({1: 'Yes', 0: 'No'})

# Calculating the number of employees who experienced attrition and who are still active
attrition_count = df['Attrition'].value_counts()
attrition_rate = attrition_count / len(df) * 100

# Create plots
fig, ax = plt.subplots()
ax.pie(attrition_count, labels=attrition_count.index, autopct='%1.1f%%', startangle=90, colors=['#06D6A0', '#EF476F'])
ax.axis('equal')
ax.set_title('Attrition Rate')
plt.show()

attritionByOverTime = df.groupby(by='OverTime').agg({'Attrition': 'count'}).reset_index()
attritionByOverTime_sorted = attritionByOverTime.sort_values(by='Attrition', ascending=False)

attritionByOverTime_sorted['OverTime'] = attritionByOverTime_sorted['OverTime'].replace({0: 'No', 1: 'Yes'})

plt.pie(attritionByOverTime_sorted['Attrition'], labels=attritionByOverTime_sorted['OverTime'], autopct='%1.1f%%', startangle=90, colors=['#06D6A0', '#EF476F'])
plt.axis('equal')
plt.title('Attrition Percentage by OverTime')
plt.show()

attritionByAge = df.groupby(by='Age').agg({'Attrition': 'count'}).reset_index()

attritionByAge_sorted = attritionByAge.sort_values(by='Attrition', ascending=False)

plt.figure(figsize=(15, 6))
sns.barplot(x='Age', y='Attrition', data=attritionByAge_sorted, palette='viridis')
plt.xlabel('Age')
plt.ylabel('Attrition Count')
plt.title('Attrition Count by Age')
plt.xticks(rotation=45)
plt.show()

"""## Data preprocessing"""

# Identifies categorical columns
categorical_column = []
for column in df.columns:
    if df[column].dtype == object and len(df[column].unique()) <= 50:
        categorical_column.append(column)

# Convert the 'Attrition' column to a categorical data type and convert categorical values ​​to integers
df['Attrition'] = df.Attrition.astype("category").cat.codes

# Removed the 'Attrition' column from the categorical column list after converting it to an integer
categorical_column.remove('Attrition')

label = LabelEncoder()
for column in categorical_column:
    df[column] = label.fit_transform(df[column])

"""## Random Forest Modelling"""

X = df.drop(columns=['Attrition'])
y = df['Attrition']

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

from sklearn.ensemble import RandomForestClassifier

random_forest = RandomForestClassifier(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
random_forest.fit(X_train, y_train)

train_pred = random_forest.predict(X_train)
test_pred = random_forest.predict(X_test)

train_acc = accuracy_score(y_train, train_pred) * 100
test_acc = accuracy_score(y_test, test_pred) * 100

print(f"Train Accuracy Score: {train_acc:.2f}%")
print(f"Test Accuracy Score: {test_acc:.2f}%")

"""## Evaluation"""

print("Classification Report:")
print("Train:\n", classification_report(y_train, train_pred))
print("Test:\n", classification_report(y_test, test_pred))

"""--- End of code ---"""