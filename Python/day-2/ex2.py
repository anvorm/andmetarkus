# andmed csv failis
# "C:\Users\USER\Documents\andmetarkus\Python\day-2\ANALYSIS\input\CustomerTable.csv"
# "C:/Users/USER/Documents/andmetarkus/Python/day-2/ANALYSIS/input/CustomerTable.csv"
import csv

data_from_csv = []

with open('C:/Users/USER/Documents/andmetarkus/Python/day-2/ANALYSIS/input/CustomerTable.csv', encoding="utf-8") as f:
    # tekitab reader objekti. klassis tekib objekt
    reader = csv.reader(f, delimiter=',') # delimiter eraldaja
    # teisendab objekti listiks
    data_from_csv = list(reader)

# esimene rida
insert_statement = "INSERT INTO customers"

# insert_statement + veergude nimed
# insert_statement += pikalt kirjutades insert_statement = insert_statement + ...
insert_statement += f"\n({','.join(data_from_csv[0])}) \nVALUES"

# mis väärtused lisada

for row in data_from_csv[1:-1]:
    # liidame insert lausele juurde rea väärtused
    insert_statement += f"\n({','.join(row)}),"

insert_statement += f"\n({','.join(data_from_csv[-1])});"  # viimasele reale ei ole koma vaid semikoolon
print(insert_statement)

