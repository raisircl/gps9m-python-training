from Rect import Rect
r1=Rect() # object 1
r2=Rect() # object 2

r3=Rect(3,4) # object 3

r1.l=5
r1.b=7

r1.display()
r3.display()

print(r1.greet)

r1.greet="Hello I am using greet for me "
print(r1.greet)
print(r3.greet)

print(f"Total Rect objects created: {Rect.count}")

