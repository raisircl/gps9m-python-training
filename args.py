def fun(x): # here x is immutable formal argument
    x=20
    print(f"Value of x {x} and address of x {id(x)}")


a=100 
print(f"Value of a {a} and address of a {id(a)}")
fun(a) # here a is immutable actual argument

# by default python passing arguments as reference
# in immutable objects if any change in formal argument its address has been
# changed and if does not affect actual arguments

def data(l): # here l is mutable formal argument if any change in it it affect actual argument
    l.append(100)

numbers=[44,332,567,33]
data(numbers)  # here numbers is actual argument list 
print(numbers)
