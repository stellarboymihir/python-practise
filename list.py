# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[1] = 'Boy'
#
# print(names[:])
#
# number =  [1, 46, 23, 53, 33, 77, 85,39, 45, 30]
# maxvalue = number[0]
# for num in number:
#     if num > maxvalue:
#         maxvalue = num
#
#
# print(maxvalue)
#
# numbers = [5, 2, 1, 3, 9, 3]
#
#
# print(numbers)
# from builtins import dict
#
# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

# def my_function(x):
#     return list(dict.fromkeys(x))
#
# mylist = my_function(["A", "B", "a", "C", "c"])
# print(mylist)


# def my_function(x):
#     seen = set()
#     result = []
#     for item in x:
#         if item not in seen:
#             result.append(item)
#             seen.add(item)
#     return result
#
# mylist = my_function(["A", "B", "a", "C", "c"])
# print(mylist)

mylist = [2, 4, 5, 6, 3, 6, 3]
result = []
for num in mylist:
    if num not in result:
        result.append(num)
print(result)

# mylist = list(dict.fromkeys(mylist))
# print(mylist)