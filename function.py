# Function -- block of code used for reusability
# factorial number using functions

def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n - 1)
num = int(input("Enter a number: "))
result = f(num)
print(f"The factorial of {num} is {result}")



def test(**kw): #parameters 
    print(kw);
test(name="xyz", age=30);

def test(a, b, *args):
    sum = 0;
    for i in args:
        sum = sum + i;
    print(sum);
    test(10,20,30,40);



def test(a, b, *args , **kwargs):
    print("Parameters are: ", a, b);
    print("Arguments are:",args);
    print("Key Arguments are: ",kwargs);

test(10,20,30,40, id=1, name="xyz");


# make a fibonacci series using function by taking user input
n = int(input("Enter the number of terms: "))
a = 0
b = 1
next = b  
count = 1

while count <= n:
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
print()


def add(a, b):
    return a + b;
def show(res):
    print(res);
show(add(10, 20))

x = 50; #global variable
def test():
    x = 100;
test()
print("outside fn: ",x);

# match case withdraw , deposit , check balance , exit

balance = 1000;
def deposit(amount):
    global balance;
    balance = balance + amount;
def withdraw(amount):
    global balance;
    if(balance >= amount):
        balance = balance - amount;
def show():
    print("Balance is : ", balance);


