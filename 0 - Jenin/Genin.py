#!/usr/bin/env python
from jinja2 import Template

t = Template("Hello {{ something }}!")
t.render(something="World")
print(t)
# 'Hello World!'


t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
t.render()
# 'My favorite numbers: 1 2 3 4 5 6 7 8 9 '


name = 'Naruto'
age = 12
tm = Template("My name is {{ name }} and I am {{ age }}")
msg = tm.render(name=name, age=age)
# My name is Naruto and I am 12


class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name    


person = Person('Naruto', 12)

tm = Template("My name is {{ per.getName() }} and I am {{ per.getAge() }}")
msg = tm.render(per=person)
# My name is Naruto and I am 12


person = { 'name': 'Naruto', 'age': 12 }

tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
# tm = Template("My name is {{ per['name'] }} and I am {{ per['age'] }}")
msg = tm.render(per=person)
# My name is Naruto and I am 12

