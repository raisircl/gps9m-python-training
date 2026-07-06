import collections
students = collections.namedtuple('students', ['name', 'age', 'marks'])
s1=students('John', 20, 85)
print(f"Student Name {s1.name}, Age {s1.age}, Marks {s1.marks} ")