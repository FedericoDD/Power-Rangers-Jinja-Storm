from jinja2 import Template

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
print(msg)
# My name is Naruto and I am 12