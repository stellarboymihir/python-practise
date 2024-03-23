# import converter
# from converter import kg_to_lbs
#
#
# print(kg_to_lbs(340))
#
# # print(converter.kg_to_lbs(76))

# from ecommerce import shipping
# shipping.calc_shipping()

import random
#
# for i in range(3):
#     print(random.randint(10, 20))
#
# members = ['Shubhamn', 'Hardik', 'Shreyas', 'Rishabh', 'Ruturaj']
# leaders = random.choice(members)
# print(leaders)

# import random
#
#
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())


from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin
# Relative path
path = Path()
for file in path.glob('*'):
    print(file)