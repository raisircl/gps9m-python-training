from Rect import Rect
r1=Rect() # object 1
r2=Rect(4,2) # object 2
r3=Rect() # object 3

r1.Length=5
r1.Breadth=7

r3=r1+r2 # adding two objects using operator overloading

print(r1)
print(r2)
print(r3)
