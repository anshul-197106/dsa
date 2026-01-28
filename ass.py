# Create a program to count the frequency of each character in a given string without using count() or Counter.

def f(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

text = input("Enter a string: ")
result = f(text)

print("Character frequencies:")
for char, freq in result.items():
    print(f"'{char}': {freq}")



# Create a program that reverses each word but keeps the sentence order unchanged.
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words) 
input_sentence = input("Enter a sentence: ")
output_sentence = reverse_words(input_sentence)
print("Reversed words sentence:", output_sentence)



#  Create a program using *args to multiply all numeric values. Ignore non-numeric values.
def numbers(*args):
    result = 1
    for arg in args:
        if isinstance(arg, (int, float)) and not isinstance(arg, bool):
            result *= arg
    return result

values = [2, "hello", 5, None, 10]
print(numbers(*values))



#  Create a program using lambda, filter, and map
lst = [1, 2, 3, 4, 5, 6]
res = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, lst)))
print (res)



#  Create a program to find the longest word in a string but without using max() 
text = input("Enter a string: ")
words = text.split()
long_word = ""
for word in words:
    if len(word) > len(long_word):
        long_word = word
print("The longest word is:", long_word)



#  Create a program to check whether two strings are anagrams or not without using sorted().
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    return True
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")



#  8
# Create a program to remove duplicates while preserving order. 
lst = [1, 2, 3, 1, 4, 2, 5]
s = set()
new_lst = []
for item in lst:
    if item not in s:
        s.add(item)
        new_lst.append(item)
print(new_lst)



# 9
# Create a program to find common elements between two lists without using set.
l1 = [1, 2, 4, 5]
l2 = [2, 9, 7, 1]
common_elements = []
for item in l1:
    if item in l2 and item not in common_elements:
        common_elements.append(item)
print("Common elements:", common_elements)



# 10
# Create a program to rotate elements of a list to the right by k positions. 
lst = [1, 2, 3, 4, 5]
k = 2
n = len(lst)
k = k  % n
rotated_lst = lst[n - k:] + lst[:n - k]
print("Rotated list:", rotated_lst)



# Create a program to find the missing number from a list containing numbers from 1 to n. 
lst = [1, 2, 4, 5, 6]
n = len(lst) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
missing_number = expected_sum - actual_sum
print("Missing number:", missing_number)



# 12. Create a program to find the first non-repeating character 
text = input("Enter a string: ")
char_count = {}
for char in text:   
    char_count[char] = char_count.get(char, 0) + 1
for char in text:
    if char_count[char] == 1:
        print("First non-repeating character:", char)
        break
        

       
#  Create a program to validate an email ID using basic rules (without regex).
def is_valid_email(email):
    if "@" not in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or not domain or "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    return True
email = input("Enter an email ID: ")

if is_valid_email(email):
    print("Valid email ID")
else:
    print("Invalid email ID")
    


#  Create a program that: Accepts username & password  Allows only 3 attempts
username = input("Enter username: ")
password = input("Enter password: ")
attempts = 0
while attempts < 3:
    if username == "admin" and password == "12345":
        print("Login successful.")
        break
    else:
        attempts += 1
        if attempts < 3:
            print("Invalid credentials. Try again.")
            username = input("Enter username: ")
            password = input("Enter password: ")
        else:
            print("Too many failed attempts. Access denied.")



# Create a program to store student marks in a dictionary and calculate average.
student_marks = {}  
num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    name = input("Enter student name: ")
    marks = float(input(f"Enter marks for {name}: "))
    student_marks[name] = marks
total_marks = sum(student_marks.values())
average_marks = total_marks / num_students
print(f"Average marks: {average_marks}")
