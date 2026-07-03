'''
Function is a set of instructions under a name
Part of program also known as sub program
It always ready to perform a task we need to call it.
During call if it expect some arguments (the data which we pass to function)
then we need to pass those arguments to function
syntax: rule to write
def function_name(arg1, arg2, ...):
    .....
    .....
    return [value]

Types: 
Data Accept  Return
Y              Y
N              Y
Y              N
N              N

Why we need functions:
1. When we are unable to perform a job
2. Perform a task again and again after some time 
'''
def msg():
    "This is msg function does not accept argument and return also"
    print("Hello Welcome to function.")
    print("I am msg function does not accept and return")

def table(num):
    "table is a function which accept a number and does not return and print its table"
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")

def fact(num):
    "fact function accept an int and return also int as factorial of num"
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

def getpi():
    "Get PI is a function does not accept but return value of PI"
    return 3.147

__name__="MyFun"

# The .py file in python also known as module. 
# It can be import in the project into another .py file
# its function can be accessible in that .py file which is importing it
 