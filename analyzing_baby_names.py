import pandas
import seaborn as sns
df = sns.load_dataset('titanic')

### Inspect DataFrames
### 1. Task 1 - Display the DataFrame
print(df)

### 2. Task 2 - Display the first 5 rows 
print(df.head())

### 3. Task 3 - Display the last 5 rows 
print(df.tail())

### 4. Task 4 - Display the number of rows and columns 
print(df.shape)

### 5. Task 5 - List the column names 
print(df.columns)

### 6. Task 6 - List the row index
print(df.index)

### 7. Task 7 - Display the column types
print(df.dtypes)


### Select Rows and Columns
### 1. Task 1 - Display the 'fare' column
print(df['fare'])

### 2. Task 2 - Display the 'fare' and 'age' columns
print(df[['fare', 'age']])

### 3. Task 3 - Display the passenger with id 3
print(df.loc[3])

### 4. Task 4 - Display the passengers with ids 3, 5, 8
print(df.loc[[3, 5, 8]])

### 5. Task 5 - Display the 'fare' and 'age' columns for passengers 3, 5 and 8
print(df.loc[[3, 5, 8], ['fare', 'age']])

### 6. Task 6 - Display the first three passengers and first three columns
print(df.iloc[:3, :3])

### 7. Task 7 - Display the first three columns for every second passengers from 10 through 30
print(df.iloc[10:31:2, :3])


### Filter Rows
### 1. Task 1 - Display the survived passengers
print(df[df['survived'] == 1])

### 2. Task 2 - Display the 2nd class passengers
print(df[df['pclass'] == 2])

### 3. Task 3 - Display the infants (age 1 or younger)
print(df[df['age'] <= 1])

### 4. Task 4 - Display children between 10 and 13
print(df[(df['age'] >= 10) & (df['age'] <= 13)])

### 5. Task 5 - Display survived 2nd class passengers
print(df[(df['survived'] == 1) & (df['pclass'] == 2)])

### 6. Task 6 - Find at least one female passenger who embarked in Cherbourg and is 40-50 years old

### 7. Task 7 - Display the passengers that do not have a missing age


### Read and Write DataFrames
### 1. Task 1 - Write the data to a CSV file
df.to_csv('titanic.csv')

### 2. Task 2 - Read the CSV file to a new DataFrame
df = pandas.read_csv('titanic.csv')

### 3. Task 3 - Write the data to an Excel file
df.to_excel('titanic.xlsx')

### 4. Task 4 - Read the Excel file to a new DataFrame
df = pandas.read_excel('titanic.xlsx')

### 5. Task 5 - Write the data to a JSON file
df.to_json('titanic.json')

### 6. Task 6 - Read the JSON file to a new DataFrame
df = pandas.read_json('titanic.json')

### 7. Task 7 - Make sure all data frames have the same shape


### Aggregation
df = sns.load_dataset('penguins')

### 1. Task 1 - What is the total mass of all penguins?
print(df['body_mass_g'].sum())

### 2. Task 2 - How many penguins are from which island?
print(df['island'].value_counts())

### 3. Task 3 - What is the average body mass of each species?
print(df.groupby('species')['body_mass_g'].mean())

### 4. Task 4 - How long is the longest beak of each species?
print(df.groupby('species')['bill_length_mm'].max())

### 5. Task 5 - What is the mean of each numerical column, per species?
print(df.groupby('species').mean())

### 6. Task 6 - How many penguins are there for each species/sex combination?


