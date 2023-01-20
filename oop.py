class Person:

    def __init__(self, first_name, last_name, age=20):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

p1 = Person('jensen', 'yuen')

print(p1.full_name())
