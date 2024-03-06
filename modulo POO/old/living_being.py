class Person:
    def __init__(self, name, age, email, phone, document):
        self.name = name
        self._age = age
        self.email = email
        self.phone = phone
        self.document = document

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):

        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError('Age must be a positive number.')

    
    def greeting(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old.'

    def contact(self):
        return f'You can contact me at {self.email} or {self.phone}.'

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def greeting(self):
        return f'Hello, my name is {self.name} and I am a {self.species}.'
