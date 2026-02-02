# take 3 number from user and check which is largest among them
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"{a} is largest")
elif b >= a and b >= c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")
    

# take a string from user and search how much vowels and consonants are there in the string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0 
consonant_count = 0
for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)


# 22/01/2026
a = 2;
b = input("Enter a number: ") 
print(id(a));          # prints the memory address of variable 


# write a program take marks from user between 0-100 and print grade A if the number are 90-100 grade 
# B if the number are 80-89 grade C if the number are 70-79 and else numbers below than 69 are in grade D
m = int(input("Enter your marks:  "))
if m >= 90 and m <= 100:
    print("Grade A");
elif m >= 80 and m <= 89:
  print("Grade B");
elif m >= 70 and m <= 79:
    print("Grade C");
elif m < 70:
    print("Grade D");

# Xor , left shift, right shift operator
a = 5;
b = 2;
print(a|b);
print(a&b);
print(a ^ b);
print("Left Shift:", a << 2);
print("Right Shift:", a >> 2);


a = 10; #unique add
b = 15; #unique add
print(a is not b ); #identity operator

marks = 52;
if(marks <= 100 and marks >=0):
    if(marks>=90):
        print("Grade A");
    elif(marks>=80 and marks<90):
        print("Grade B");
    elif(marks>=70 and marks<80):
        print("Grade C");
    else:
        print("Fail");
else:
    print("Enter the num between 0-100");

# take a input from user and display weekdays 
day = int(input("Enter a number between : "))
if day == 1:
    print("Monday");
elif day == 2:
    print("Tuesday");
elif day == 3:
    print("Wednesday");
elif day == 4:
    print("Thursday");
elif day == 5:
    print("Friday");
elif day == 6:
    print("Saturday");
elif day == 7:
    print("Sunday");
else:
    print("Invalid input");

a=10;
b=20;
res  = a if a>b else b;
print(res);
 
# print 0 - 50 prime numbers 

for num in range(0, 51):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# break and continue use in loop
i = int(input("Enter a number: "))
for i in range(1, 11):
    if i == 7:
        # break
        continue
    print(i)    

# nested loop star pattern
n = 5
for i in range(1, n+1):   
    for j in range(1, i+1):
        print(i, end=" ")
        # print(j, end=" ")
    print()


rows = 5
for i in range(rows, 0, -1):  
    for j in range(i):  
        print(j, end=" ")  
    print()  