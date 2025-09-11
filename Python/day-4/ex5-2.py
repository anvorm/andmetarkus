

vitamiinide_rikkad = []

for k, v in toidud.items():
    b_vitamiinide_arv = sum (1 for vit in v["vitamiinid"] if vit.startswith("B"))

    if b_vitamiinide_arv >=2:
        vitamiinide_rikkad.append(k)

print("B vitamiini rikkad toidud:", vitamiinide_rikkad)

vitamiinide_rikkad_2 = [] 

for k, v in toidud.items():
    b_vitamiinide_arv = len([vit for vit in v["vitamiinid"] if vit.startswith("B")])
    if b_vitamiinide_arv >=2:
        vitamiinide_rikkad_2.append(k)        

print("lahendus 2 B vitamiini rikkad todid:", vitamiinide_rikkad)

# pikk lahend

vitamiinide_rikkad_3 = []

for k, v in toidud.items():
    # vaatame iga toidu puhul vitamiinid
    b_vitamiinide_arv = 0
    for vit in v["vitamiinid"]:
        if vit.startswith("B"):
            b_vitamiinide_arv += 1
    if b_vitamiinide_arv >= 2:
        vitamiinide_rikkad_3.append(k)

print("lahendus 3 B vitamiini rikkad toidud:", vitamiinide_rikkad_3)    

# oneline solulu
vitamiinide_rikkad_4 = [k for k, v in toidud.items() if sum(1 for vit in v["vitamiinid"] if vit.startswith("B")) >= 2]
print("lahendus 4 B vitamiini rikkad toidud:", vitamiinide_rikkad_4)


