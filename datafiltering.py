import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# filter rows based on condition, eg- filtering IT Dep. employees
it_emp = df[df['Dep'] == 'IT']
print(it_emp)

# eg- filtering employees having salary more than 50000
sal = df[df['Salary'] > 50000]
print(sal)

# find highest number eg- highest salary employee
max_sal = df['Salary'].max()
max_sal_emp = df[df['Salary'] == max_sal]
print("Maximum salary employee: \n", max_sal_emp)

# find lowest number eg- lowest salary employee
min_sal = df['Salary'].min()
min_sal_emp = df[df['Salary'] == min_sal]
print("Minimum salary employee: \n", min_sal_emp)

# count frequency of each column eg- count no of employees in each department
dep_count = df['Dep'].value_counts()
print("No of employees in each dep: \n", dep_count)

# values in desending order eg- highest to lowest age employees
sort = df.sort_values(by='Age', ascending=False)
print("Senior to Junior employees: \n", sort)

# values in ascending order eg- lowest to highest salary employees
sort = df.sort_values(by='Salary', ascending=True)
print("Lowest to Highest salary employee \n", sort)

# add column to the data with specific condition eg- add 'senior' to experience column if age >= 30, otherwise 'junior'
df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x>=30 else 'Junior')
print("Data with Experience Column \n", df)

# --------------------------------------------------------------------------------------
# DATA VISUALIZATION

# pie chart using matplotlib
plt.figure(figsize=(6, 9))
plt.pie(dep_count, labels=dep_count.index, autopct="%1.1f%%", startangle=140)
plt.title("Department")
plt.show() 