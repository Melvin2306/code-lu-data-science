import pandas
import seaborn as sns

### Task 2- Read the file 'yob2021.txt' into pandas.
df = pandas.read_csv('yob2021.txt')

### Task 3 - Display the first 10 rows of the DataFrame
print(df.head(10))

### Task 4 - Display the number of rows and columns.
print(df.shape)

### Task 5 - Calculate the total number of babies born in 2021, i.e. the sum of the third column.
print(df['Count'].sum())

### Task 6 - Like Task 5, but calculate the sum for boys and girls separately.

### Task 7 - Check if "Melvin" occurs in the data.

### Task 8 - Calculate the percentage of girls and boys among the total births.

### Task 9 - Create a table that contains the top 5 girls names and top 5 boys names.


