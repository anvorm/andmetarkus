import pandas as pd
file_name = 'C:/Users/USER/Documents/andmetarkus/Python/day-2/ANALYSIS/input/ProductTable.xlsx'

data = pd.read_excel(file_name)
data_dict = data.to_dict(orient='records')

# originaalkujul
print(data)

# sõnastiku kujul
print(data_dict)

file_csv = 'C:/Users/USER/Documents/andmetarkus/Python/day-2/ANALYSIS/input/CustomerTable.csv'

data2 = pd.read_csv(file_csv)
print(data2)
