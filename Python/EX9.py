names_sorted = ['Ain', 'Ann', 'Jaanika', 'Kalle', 'Karl', 'Kersti', 'Kusti', 'Malle', 'Margus']
names_starting_with_a = [x for x in names_sorted if x[0] == "A"]
print(names_starting_with_a)

names_containing_a = [x for x in names_sorted if "a" in x]
print(names_containing_a)

short_names = [x for x in names_sorted if len(x) <= 4]
print(short_names)

