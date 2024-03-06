from living_being import Person

p1 = Person('Marcos', 25, 'marcos@mail.com', '1234567890', 'ABC')

print(p1.name)
print(p1.age)
p1.age = 26
print(p1.age)
p1.age = -100
print(p1.age)