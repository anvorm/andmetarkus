import pandas as pd
import numpy as np

ilmaandmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "temperatuur": [18.5, 19.2, 17.8, 16.4, 15.9],
    "niiskus": [65, 60, 70, 68, 75],
    "tuul": [4.2, 3.8, 5.0, 4.5, 6.1]
}

linnad_andmed = {
    "linn": ["Tallinn", "Tartu", "Pärnu", "Narva", "Kuressaare"],
    "elanike_arv": [440000, 95000, 51000, 57000, None],
    "pindala": [159.2, 38.8, 32.2, 84.5, 15.0]  # km²
}

ilma_df = pd.DataFrame(ilmaandmed)
linnad_df = pd.DataFrame.from_dict(linnad_andmed, orient="index").transpose()

print(linnad_df)

# panen kahe tabeli andmed linna alusel kokku

koond_df = pd.merge(ilma_df, linnad_df, on="linn", how="inner")
print(koond_df)

# Paranda None kui linna väärtus on kuressaare

koond_df.loc[koond_df['linn'] == 'Kuressaare', 'elanike_arv'] = 14000
print(koond_df)

# mis linna son kõrgeim temperatuur

korgem_temperatuur = koond_df['temperatuur'].max()
korgem_linn = koond_df.loc[koond_df['temperatuur'] == korgem_temperatuur, 'linn'].values[0]
print(f"Kõrgeim temperatuur on {korgem_temperatuur}°C linnas {korgem_linn}")

# Leia rida, kus temperatuur on kõrgeim
max_temp_row = koond_df.loc[koond_df['temperatuur'] == koond_df['temperatuur'].max()]
print(max_temp_row)

# leida linnade rahavstiku tihedus. Lisaveeruna


# koond_df['rahvastiku_tihedus'] = (koond_df['elanike_arv'] / koond_df['pindala']).round(2)
# print(koond_df)

# filtreeri niiskuse järgi

niisked_linnad = koond_df[koond_df['niiskus'] > 70]

# sorteeri andmed tuule kiiruse järgi kasvavalt

koond_df = koond_df.sort_values(by='tuul', ascending=True)
print(koond_df)

# lisa uus veerg mis näitab kas temp on üle või alla keskmise

keskmine_temp = koond_df['temperatuur'].mean()

""" temp_status = []
for temp in koond_df['temperatuur']:
    if temp > keskmine_temp:
        temp_status.append("üle keskmise")
    elif temp < keskmine_temp:
        temp_status.append("alla keskmise")
    else:
        temp_status.append("võrdne keskmisega")

koond_df['temp_staatus'] = temp_status

print(koond_df) """

koond_df["temp_kategooria"] = np.where(koond_df["temperatuur"] > keskmine_temp, "üle keskmise", "alla keskmise")
print(koond_df)

# asenda kõik linnanimed suurte tähdedega

koond_df["linn"] = koond_df["linn"].str.upper()
print(koond_df )

# salvesta koondandmed csv faili

koond_df.to_csv("koondandmed.csv", index=False)
print(koond_df)