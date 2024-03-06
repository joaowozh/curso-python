from living_being import Person

p1 = Person('Marcos', 25, 'marcos@mail.com', '1234567890')

greeting = p1.greeting()
contact = p1.contact()

print(type(p1))
print(p1.name)
print(p1.age)
print(p1.email)
print(p1.phone)
# print(greeting)
# print(contact)

print('-------------------')

p2 = Person('Ana', 30, 'ana@mail.com', '0987654321')

greeting = p2.greeting()
contact = p2.contact()

print(type(p2))
print(p2.name)
print(p2.age)
print(p2.email)
print(p2.phone)

print('-------------------')

p3 = Person('Lucas', 35, 'lucas@mail.com', '6789054321')

greeting = p3.greeting()
contact = p3.contact()

print(type(p3))
print(p3.name)
print(p3.age)
print(p3.email)
print(p3.phone)

print('-------------------')

from living_being import Animal

a1 = Animal('Rex', 'dog', 5)

greeting = a1.greeting()

print(type(a1))
print(a1.name)
print(a1.species)
print(a1.age)