boys_names = ["Ain", "Kalle", "Kusti", "Karl"]
print(boys_names)
boys_names.append("Margus")
print(boys_names)
girl_names = ["Jaanika", "Malle", "Kersti", "Ann"]
names = []
names = boys_names + girl_names
print(names)
names_sorted = sorted(names)
print(names_sorted)
print(min(girl_names))
print(len(names_sorted))
print(names_sorted[-1])
boys_names_reverse = boys_names.reverse()
print(boys_names_reverse)
transaction_customer_id = [1, 2, 5, 2, 4, 8]
print(transaction_customer_id)
active_customers = set(transaction_customer_id)
print(active_customers)
all_customers = [1,2,3,4,5,6,7,8,9,10]
all_customers = set(range(1,11))
print(all_customers)
passing_customers = all_customers - active_customers
print(passing_customers)
my_company_data = {"id": 12345678
                   , "years_sales": {2023: 10000, 2022: 9000, 2021: 8000}
                   , "activity": "IT"
        }
print(my_company_data)
my_company_data["name"] = "UUS NIMI"
print(my_company_data)

my_company_data.update({"address": "Tartu mnt 1"})
my_company_data["years_sales"][2024] = 11000
print(my_company_data)

popular_boys_names = ("Peeter", "Karl")  
print(popular_boys_names)
print(popular_boys_names[0])
random_data = ("viis", 5, 5.0)
print(random_data)




