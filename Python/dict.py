# create a dict in a dict 
# dict = {
#     "name" : ["ABC", "XSW"],
#     "ID" : 1,
#     "adress" : {
#         "Home" : "Chd",
#         "Work" : "Delhi",
#     },
# }

# print(dict["adress"]["Home"])

# keys(), values(), items()

# for i in dict:
#     print(i)
# for i in dict.values():
#     print(i)
# for i, j in dict.items():
#     print(i," ", j)


# create a dict and merge them 
# dict1 = {
#     "name" : ["ABC"],
#     "ID" : 1,
# }
# dict2 = {
#     "name" : ["XZC"],
#     "ID" : 3,
#     "Age" : 18,
# }
# dict1.update(dict2)
# print(dict1) 


# reference
# a = [10, 20, 30]
# b = a
# b[0] = 100,
# print(a)
# print(b)


# Shallow Copy
# a = [10, 20, 30]
# b = a[:] #shallow copy 
# b[0] = 100;
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# a = [[10,20],[30,40]]
# b = a[:]
# b[0] = 50;
# print(a)
# print(b)
# print(id(a))
# print(id(b))


# import copy
# a = [[10,20], [30,40]];
# b = copy.deepcopy(a);
# b[0][0]= 100
# print(a)
# print(b)
# print(id(a))
# print(id(b))