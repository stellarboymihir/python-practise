# if it's hot
#     It's hot day
#     Drink plenty of water
# otherwise if it's cold
#     It's a cold day
#     Wear warm clothes
# otherwise
#     It's a lovely day...

# is_hot = False
# is_cold = False
#
#
# if is_hot:
#     print("It's a hot day...")
#     print("Drink plenty of water...")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day...")
# print("Enjoy your day")


# Price of a house $1M
# If Buyer has a good credit
#     they need to put down by 10%
# Otherwise
#     they need to put down by 20%
# Print the down payment

price = 1000000
good_credit = False

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")


#
# If applicant has high income AND good credit
#     Eligible for loan
#  IF applicant has good credit AND doesn't have a criminal record


# AND: both
# OR: at least one


#
# # has_high_income = True
# has_good_credit = True
# has_criminal_record = False
#
#
#
# if  has_good_credit and not has_criminal_record:
#     print("Eligible for loan")


# temp = 20
#
# if temp != 30:
#     print("It's a hot day")
# elif temp < 10:
#     print("It's a cold day")
# else:
#     print("It's neither hot or cold")

character = "JAy"
if len(character) < 3:
    print("Name must be at least 3 characters.")
elif len(character) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good! ")
