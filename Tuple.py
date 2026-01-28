# Creating a tuple

# tpl = 10, 20, 30
# print(tpl)
# print(type(tpl))

# Set :: Collection of unique items mutable, unordered
# st = [1, 2, 3, 6, 5, 9]
# st.add(7)
# st.update9[3, 10]
# print(st)

# Union,Intersection,Difference,Symmetric Difference
# st1  = {10, 20, 30, 40}
# st2 = {50, 60, 70, 80}
# print(st1 | st2)          # Union
# print(st1 & st2)          # Intersection
# print(st1 - st2)          # Difference
# print(st1 ^ st2)          # Symmetric Difference

# one platform users , two platform users , three platform users
Youtube = {'a', 'b', 'c', 'd'}
Facebook = {'c', 'd', 'e', 'f'}
Instagram = {'e', 'f', 'g', 'h'}
print(" Users on at least one platform: ", Youtube | Facebook | Instagram)
print(" Users on exactly two platforms: ", (Youtube & Facebook) | (Facebook & Instagram) | (Instagram & Youtube) - (Youtube & Facebook & Instagram))



# set comprehension
st = {x*x for x in range(1, 4) if x%2 == 0}
print(st)