
import pandas as pd

# Lae elektrihindade graafikud

source_data = pd.read_json('day-3/elektrihind/el_data_2025.json')
electricity_data = pd.json_normalize(df["data"])
print(electricity_data.head)

source_data_2 = pd.read_csv('day-3/ilmaandmed/Tallinn_Harku_2024.csv')
weather_data = pd.DataFrame(source_data_2)
print(weather_data.head())

weather_data['datetime'] = pd.to_datetime(weather_data['Aeg'])