girl_names = ["Jaanika", "Malle", "Kersti", "Ann", "Mari", "Kati"]
for x in girl_names:
    print(x)
for x in range(2):
    print(girl_names[x])
for x in range(1, 4):
    print(girl_names[x])
for x in girl_names[1:4]:
    print(x)
for name in reversed(girl_names):
    print(name)
for i in range(0, len(girl_names), 2): 
    print(girl_names[i])
for i in girl_names:
    if i[0] == "K":
        print(i)

sorted_names = {"M": []}
M_names = []
for i in girl_names:
    if i[0] == "M":
        M_names.append(i)
        sorted_names["M"].append(i)
print(sorted_names)



