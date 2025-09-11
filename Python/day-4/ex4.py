# Andmete töötlus

sonad = ["    õun", "banaan    ", "    pirn    ", "ploom", "    viinamari    "]

# variant 1: kasutades string meetodit strip()

puhastatud_sonad = []
for sona in sonad:
    puhastatud_sonad.append(sona.strip())

print(puhastatud_sonad)

# variant 2: kasutades listi comprehensions ja string replace() meetodit
puhastatud_sonad = [sona.replace(" ", "") for sona in sonad]
print(puhastatud_sonad)

# Summade teisendus
summad = ["1,234.56", "12,000.00", "5,678.90", "100.00", "23,456.78"]

numbrina = []
for summa in summad:
    summa = summa.replace(",", "")
    numbrina.append(float(summa))

print(numbrina)
print(type(numbrina[0]))  # Output: <class 'float'>
print(sum(numbrina))

# using list comprehension
numbrina = [float(summa.replace(",", "")) for summa in summad]

# comprehension example

algandmed = [1, 2, 3, 4]
uued_andmed = [x * 2 for x in algandmed]

print(uued_andmed)  # Output: [2, 4, 6, 8]