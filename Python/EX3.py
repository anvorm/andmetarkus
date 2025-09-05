age = 22
if age >= 18:
    print("võid hääletada")
    if age >= 18:
        print("riigikogu")
else:
    print("ei või hääletada")
number_to_check = 100
if number_to_check < 100:
    print("alla 100")
if number_to_check == 100:
    print("võrdne 100")
if number_to_check > 100:
    print("suurem kui 100")

if number_to_check >= 18:
    print("täiskasvanu ")
else:
    print("alaealine")

is_adult = age >= 18
print(f"kas on täiskasvanu {is_adult}")

print("isik täiskasvanu") if age >= 18 else print("isik alaealine")

