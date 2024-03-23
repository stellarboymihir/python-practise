# for item in ["Mosh", "John", "Amay"]:
#     print(item)
#
# for item in range(5,100, 5):
#     print(item)
# #
#
# prices = [10, 20, 30]
#
# total = 0
# for price in prices:
#     total = total + price
# print(f"Total: {total}")
#
# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")

#
# number = [5, 2, 5, 2, 2]
#
# # for i in number:
#     # for j in number:
#     # num += number
#     #     print(f"{number}")
#
# print(number)
# n = int(input("Enter a number: "))
#
# for i in range(1, n ):
#     for j in range(1, n, 2):
#         print("*", end="")
#     print()

    #####
    ##
    #####
    ##
    ##

# number = [5, 2, 5, 2, 2]
#
# for x_count in number:
#     print("x" * x_count)

# number = [1, 1, 1, 1, 5]

# for x_count in number:
#     output = ''
#     for count in range(x_count):
#         output += 'x'
#     print(output)
#
# numbers = [20, 4, 42, 53]
# maxvalue = numbers[3]
# for number in numbers:
#     if number > maxvalue:
#         maxvalue = number
# print(maxvalue)

from utils import find_max

num = [1, 4, 5, 8]
maxvalue = find_max(num)
print(maxvalue(num))
