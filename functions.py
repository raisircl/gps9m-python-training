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
Types 
Accept  Return
Y       Y
N       Y
Y       N
N       N
'''
def total(n1,n2):
    "sum of 2 nos"
    print(f"The sum is {n1+n2}")

def factorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

def table(num):
    for i in range(1,num+1):
        print(f"{num}x{i}={num*i}")

def sayhello(name="Guest"):
    print(f"Hello {name} Welcome to function")

def getpi():
    return 3.14

