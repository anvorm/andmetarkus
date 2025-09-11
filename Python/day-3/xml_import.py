# import from xml
import requests
import xml.etree.ElementTree as ET
import pandas as pd

url = "https://www.ilmateenistus.ee/ilma_andmed/xml/forecast.php"

response = requests.get(url)
xml_content = response.content

df = pd.read_xml(xml_content, xpath=".//place")
print(df.head())

# min_temp = df['tempmin'].min()
min_temp_row = df[df['tempmin'] == df['tempmin'].min()]

max_temp_row = df[df['tempmax'] == df['tempmax'].max()]
print(min_temp_row)

grouped = df.groupby('tempmin').size().reset_index(name='count')
print(grouped)

