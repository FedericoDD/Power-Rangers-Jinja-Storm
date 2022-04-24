from jinja2 import Template

name = 'Naruto'
age = 12
tm = Template("My name is {{ name }} and I am {{ age }}")
msg = tm.render(name=name, age=age)
print(msg)
# My name is Naruto and I am 12