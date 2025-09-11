# Laeme excelist ilmaandmed
import pandas as pd

data = pd.read_excel('Python/day-3/Tallinn-Harku-2004-2024.xlsx',
                     skiprows=2)
df = pd.DataFrame(data)

# Filtreeri ainult read, kus Aasta on 2024
df_2024 = df[df['Aasta'] == 2024]


# Salvesta DataFrame uude faili
df_2024.to_csv('Python/day-3/tallinn_harku_2024.csv', index=False)