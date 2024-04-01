# -*- coding: utf-8 -*-
"""Dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LdFnMCKUs8MVaMzwNNf0jO1ESmJXXZQc

## Import necessary libraries
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""## Data Preparation"""

df = pd.read_csv("employee_data.csv", encoding='windows-1252')

df.shape

# handling missing value
missing_attrition = df[df['Attrition'].isnull()]
missing_attrition.head()

df = df.dropna(subset=['Attrition'])
df.shape

"""## Business Dashboard"""

df['Education'] = df['Education'].map({1: 'Below College', 2: 'College', 3: 'Bachelor', 4: 'Master', 5: 'Doctor'})
df['EnvironmentSatisfaction'] = df['EnvironmentSatisfaction'].map({1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'})
df['JobInvolvement'] = df['JobInvolvement'].map({1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'})
df['JobSatisfaction'] = df['JobSatisfaction'].map({1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'})
df['PerformanceRating'] = df['PerformanceRating'].map({1: 'Low', 2: 'Good', 3: 'Excellent', 4: 'Outstanding'})
df['RelationshipSatisfaction'] = df['RelationshipSatisfaction'].map({1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'})
df['WorkLifeBalance'] = df['WorkLifeBalance'].map({1: 'Low', 2: 'Good', 3: 'Excellent', 4: 'Outstanding'})

df['Attrition'] = df['Attrition'].replace({1: 'Yes', 0: 'No'})

attrition_count = df['Attrition'].value_counts()
attrition_rate = attrition_count / len(df) * 100

fig, ax = plt.subplots()
ax.pie(attrition_count, labels=attrition_count.index, autopct='%1.1f%%', startangle=90, colors=['#06D6A0', '#EF476F'])
ax.axis('equal')
ax.set_title('Attrition Rate')
plt.show()

attrition_counts = df['Attrition'].value_counts()
print("Active Employees (No) and Attrition Employees (Yes)")
print(attrition_counts)

def GroupAge(age):
  if age <= 35:
    return '18-35'
  elif age >= 36 and age <= 55:
    return '36-55'
  elif age > 55:
    return '>55'

df['Age'] = df['Age'].apply(GroupAge)

df['EmployeeId'].count()

attritionByAgeGender = df[df['Attrition'] == 'Yes'].groupby(['Age', 'Gender'])['Attrition'].count().reset_index(name='Attrition_Yes_Count')
attritionByAge = df.groupby(['Age', 'Gender'])['Attrition'].count().reset_index(name='Total_Count')
result = attritionByAge.merge(attritionByAgeGender, on=['Age', 'Gender'], how='left').fillna(0)
result = result.drop(columns=['Total_Count'])  # Menghapus kolom Total_Count
result = result.sort_values(by='Attrition_Yes_Count', ascending=False)
result

attritionByGender = df[df['Attrition'] == 'Yes'].groupby('Gender').agg({'Attrition': 'count'})
attritionByGender.columns = ['Attrition_Yes_Count']
attritionByGender

attritionByEducationField = df[df['Attrition'] == 'Yes'].groupby('EducationField').agg({'Attrition': 'count'})
attritionByEducationField.columns = ['Attrition_Yes_Count']
attritionByEducationField = attritionByEducationField.sort_values(by='Attrition_Yes_Count', ascending=False)
attritionByEducationField

attritionByEducation = df[df['Attrition'] == 'Yes'].groupby('Education').agg({'Attrition': 'count'})
attritionByEducation.columns = ['Attrition_Yes_Count']
attritionByEducation

def GroupDistanceFromHome(distance):
  if distance <= 5:
    return 'Nearby'
  elif distance >= 6 and distance <= 15:
    return 'Far'
  else:
    return 'Very Far'

df['DistanceFromHome'] = df['DistanceFromHome'].apply(GroupDistanceFromHome)

attritionByDistanceFromHome = df.groupby(['Attrition', 'DistanceFromHome']).size().unstack(fill_value=0)
attrition_yes_data = attritionByDistanceFromHome.loc['Yes']
attrition_yes_data_df = attrition_yes_data.reset_index().rename_axis(None, axis=1)
attrition_yes_data_df.columns = ['DistanceFromHome', 'Count']
attrition_yes_data_df

attritionByMaritalStatus = df[df['Attrition'] == 'Yes'].groupby('MaritalStatus').agg({'Attrition': 'count'})
attritionByMaritalStatus.columns = ['Attrition_Yes_Count']
attritionByMaritalStatus

attritionByDepartmentGender = df[df['Attrition'] == 'Yes'].groupby(['Department', 'Gender']).agg({'Attrition': 'count'})
attritionByDepartmentGender.columns = ['Attrition_Yes_Count']
attritionByDepartmentGender = attritionByDepartmentGender.sort_values(by='Attrition_Yes_Count', ascending=False)
attritionByDepartmentGender

attritionByBusinessTravelGender = df[df['Attrition'] == 'Yes'].groupby(['BusinessTravel', 'Gender']).agg({'Attrition': 'count'})
attritionByBusinessTravelGender.columns = ['Attrition_Yes_Count']
attritionByBusinessTravelGender = attritionByBusinessTravelGender.sort_values(by='Attrition_Yes_Count', ascending=False)
attritionByBusinessTravelGender

attritionByJobLevelGender = df[df['Attrition'] == 'Yes'].groupby(['JobLevel', 'Gender']).agg({'Attrition': 'count'})
attritionByJobLevelGender.columns = ['Attrition_Yes_Count']
attritionByJobLevelGender

attritionByJobRoleGender = df[df['Attrition'] == 'Yes'].groupby(['JobRole', 'Gender']).size().unstack(fill_value=0)
attritionByJobRoleGender = attritionByJobRoleGender.sort_values(by=['JobRole'], ascending=False)

attritionByJobRoleGender

attritionByGender = df[df['Attrition'] == 'Yes'].groupby('Gender').agg({'Attrition': 'count'})
attritionByGender.columns = ['Attrition_Yes_Count']
attritionByGender

attritionByOverTime = df[df['Attrition'] == 'Yes'].groupby('OverTime').agg({'Attrition': 'count'})
attritionByOverTime.columns = ['Attrition_Yes_Count']
attritionByOverTime

def working_years(years):
    if years < 1:
        return 'Junior'
    elif 1 <= years <= 3:
        return 'Middle'
    else:
        return 'Senior'

df['ExperienceCategory'] = df['TotalWorkingYears'].apply(working_years)

attritionByTotalWorkingYears = df[df['Attrition'] == 'Yes'].groupby('ExperienceCategory').agg({'Attrition': 'count'})
attritionByTotalWorkingYears.columns = ['Attrition_Yes_Count']
attritionByTotalWorkingYears = attritionByTotalWorkingYears.sort_values(by='Attrition_Yes_Count', ascending=False)
attritionByTotalWorkingYears

attritionByJobSatisfaction = df[df['Attrition'] == 'Yes'].groupby('JobSatisfaction').agg({'Attrition': 'count'})
attritionByJobSatisfaction.columns = ['Attrition_Yes_Count']
attritionByJobSatisfaction

attritionByEnvironmentSatisfaction = df[df['Attrition'] == 'Yes'].groupby('EnvironmentSatisfaction').agg({'Attrition': 'count'})
attritionByEnvironmentSatisfaction.columns = ['Attrition_Yes_Count']
attritionByEnvironmentSatisfaction

attritionByRelationshipSatisfaction = df[df['Attrition'] == 'Yes'].groupby('RelationshipSatisfaction').agg({'Attrition': 'count'})
attritionByRelationshipSatisfaction.columns = ['Attrition_Yes_Count']
attritionByRelationshipSatisfaction

attritionByWorkLifeBalance = df[df['Attrition'] == 'Yes'].groupby('WorkLifeBalance').agg({'Attrition': 'count'})
attritionByWorkLifeBalance.columns = ['Attrition_Yes_Count']
attritionByWorkLifeBalance

"""Monthly Income Categories:
- Low Income: Monthly income Less than or equal to 25% of the mean <= 2900 (usd).

- Medium Income: Monthly income between 25% and 75% of the mean 2900 (usd) to 8736 (usd).

- High Income: Monthly income more than 75% of the mean > 8736 (usd).
"""

def categorize_income(income):
    if income <= 2900:
        return 'Low Income'
    elif income <= 8736:
        return 'Medium Income'
    else:
        return 'High Income'

df['IncomeCategory'] = df['MonthlyIncome'].apply(categorize_income)

attritionByIncomeCategory = df[df['Attrition'] == 'Yes'].groupby('IncomeCategory').agg({'Attrition': 'count'})
attritionByIncomeCategory.columns = ['Attrition_Yes_Count']
attritionByIncomeCategory

averageMonthlyIncome = df['MonthlyIncome'].mean()
averageMonthlyIncome

averageHourlyRate = df['HourlyRate'].mean()
averageHourlyRate

averageMonthlyRate = df['MonthlyRate'].mean()
averageMonthlyRate

"""--- End of code ---"""