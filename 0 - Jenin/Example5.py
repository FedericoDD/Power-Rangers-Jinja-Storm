from jinja2 import Template

person = { 'name': 'Naruto', 'age': 12 }

tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
# tm = Template("My name is {{ per['name'] }} and I am {{ per['age'] }}")
msg = tm.render(per=person)
# My name is Naruto and I am 12
print(msg)