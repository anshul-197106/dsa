# Modifying the first element of a list and printing all elements
lst1 = [12, 34, 56, 78, 90]
lst1[0] = 35
for i in lst1:
    print(i, end=" ");



# write a program to find the largest element in a list
lst2 = [23, 45, 67, 89, 12, 90, 34]
largest = lst2[0]   
for i in lst2:
    if i > largest:
        largest = i
print("\nLargest element is:", largest)



# write a program find second largest element in a list
lst3 = [23, 45, 67, 89, 12, 90, 34]
largest = second_largest = lst3[0]
for i in lst3:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("Second largest element is:", second_largest)

# write a program to find largest and second largest element in a list
lst4 = [23, 45, 67, 89, 12, 90, 34]
largest = second_largest = lst4[0]
for i in lst4:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("Largest element is:", largest)
print("Second largest element is:", second_largest) 

# 
lst = ["BCA", "BBA", "B.Tech"];
# built in function //  append - - last position, insert , extend
lst.append("PhD")      # adds element at last position
lst.insert(2, "BA")    # adds element at specified position
lst.extend(["BCom"])   # adds multiple elements at last position
print(lst)


# blank list add it by using append, insert, extend 
new_lst =[ ];
new_lst.append("BCA")
new_lst.insert(1,"BTech")
new_lst.extend(["MCA", "MTech"])
print(new_lst)


# list comprehension
lst = [10, 20, 30]
new_lst = [num for  num in lst];
# new_lst = [i for  i in lst];

# print(new_lst);

# # map function :: perform on each element of list
lst = [2, 3, 4, 5, 6]
res = list(map(lambda x: x*x+1, lst))
print(res)

# # filter :: filter out element based on condition
lst = [2, 3, 4, 5, 6, 7]
res = filter(lambda x: x > 5, lst)
print(list(res))


# syntax of map and filter
# map(function, iterable)
# filter(function, iterable)
# reduce(function, iterable)  # need to import functools

# from functools import reduce
from functools import reduce
list = [10, 20, 30, 40, 50]
res = reduce(lambda a,b : b-a, list)
print (res)

