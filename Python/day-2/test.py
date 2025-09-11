import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

url = "https://demo-datahub.rik.ee/api/v1/meta/classifications"

url_riik = 'https://api.worldbank.org/v2/countries/EST/?format=json'
url_rahvastik_ = 'https://api.worldbank.org/v2/country/EST/indicator/SP.POP.TOTL?format=json'

response = requests.get(url_rahvastik_)
data = response.json()

# json dumps muudab väljundi terminalis loetavaks
# print(json.dumps(data, indent=2, ensure_ascii=False))

print(json.dumps(data, indent=2, ensure_ascii=False))