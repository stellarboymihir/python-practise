#  1 lbs = 0.45359237 kg
#  1 kg = 2.2046226218 lbs


weight = int(input('Weight: '))

unit = input(' (L)bs or (K)g: ')

if unit.upper() == "L":
    converter = weight * 0.45
    print(f"You are {converter} kilos")
else:
    converter = weight / 0.45
    print(f"You are {converter} pounds")
