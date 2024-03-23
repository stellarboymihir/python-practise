# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_Verified": True
# }
#
# customer["name"] = "Jack Smith"
# print(customer["name"])
# print(customer.get("is_Verified"))
#
# customer["birthdate"] = "Sept 30 2000"
# print(customer["birthdate"])
#
# print(customer.get("birtdate", "Jan 1 1980"))


phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""

for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)