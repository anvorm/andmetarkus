riigid = ["Eesti", "Austria", "Belgia", "Andorra",
          "Hispaania", "Soome", "Albaania", "Itaalia"]

# Leia ja salvesta eraldi järjendisse kõik riigid, mis algavad A ja E tähega. Prindi uus nimek terminali.

OTSITAVAD_ALGUSTÄHED = ("A", "E")

# list comprehension
riigid_ae = [riik for riik in riigid if riik.startswith(OTSITAVAD_ALGUSTÄHED)]

# for tsükkel
riigid_ae2 = []
for riik in riigid:
    if riik[0] in OTSITAVAD_ALGUSTÄHED:
        riigid_ae2.append(riik)


# for tsükkel
riigid_ae3 = []
for riik in riigid:
    if riik.startswith("A") or riik.startswith("E"):
        riigid_ae3.append(riik)

# for eraldi if laused, samaväärne eelmisega

riigid_ae4 = []
for riik in riigid:
    if riik.startswith("A"):
        riigid_ae4.append(riik)
    elif riik.startswith("E"):
        riigid_ae4.append(riik)

# testime lahendusi
print(riigid_ae)
print(riigid_ae2)
print(riigid_ae3)
# Output: ['Eesti', 'Austria', 'Andorra', 'Albaania']