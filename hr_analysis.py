import pandas as pd
df = pd.read_csv("HR_data.csv")
print(df.head())
print(df.info())

df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])

df['YearsInCompany'] = pd.Timestamp.today().year - df['JoiningDate'].dt.year

print(df.isnull().sum())

# Number of employees per department
print(df['Department'].value_counts())

# Average salary by department
avg_salary=(df.groupby('Department')['Salary'].mean())
print(avg_salary.round(2))

# Gender Distribution
gender_percentage=(df['Gender'].value_counts(normalize=True) * 100)
print(gender_percentage.astype(str) + '%')

# Highest earning employees
top_earners = df.sort_values(by='Salary', ascending=False).head(5)
print(top_earners[['Name', 'Department', 'Salary']])

# Top performers
top_performers = df.sort_values(by='PerformanceScore', ascending=False).head(5)
print(top_performers[['Name', 'Department', 'PerformanceScore']])

# Salary rank
df['SalaryRank'] = df['Salary'].rank(ascending=False)

# Female employees in IT with salary > 60K
filtered = df.query("Gender == 'Female' and Department == 'IT' and Salary > 60000")
print(filtered[['Name','Department','Gender','Salary']])

# Pivot table
pivot = pd.pivot_table(df, 
                       values='Salary', 
                       index='Department', 
                       columns='Gender', 
                       aggfunc='mean',
                       fill_value=0)
print(pivot)

df.to_csv("HR_data_final.csv",index=False)

