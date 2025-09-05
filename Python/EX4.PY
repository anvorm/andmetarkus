def is_adult(age):
    if age is None or not isinstance(age, int) or age < 0:
        return False
    elif age >= 18:
        return True
    else:
        return False
   

print(is_adult(77))
age = 15

if is_adult(age):
    print("valib")
else:
    print("ei vali")

eu_northern_country_codes = ["DK", "EE", "FI", "IS", "LT", "LV", "NO", "SE"]
def is_northern_country(country_code):
    if not isinstance(country_code, str) or len(country_code) != 2:
        return False
    return country_code in eu_northern_country_codes
     
print(is_northern_country("oop"))

