from jinja2 import Environment, FileSystemLoader

"""
Here you can read a file and
do simple math operations.
"""

env = Environment(loader=FileSystemLoader('3 - Expressions/templates'))

persons = [
    {'name': 'Andrea', 'missions': 151}, 
    {'name': 'Matteo', 'missions': 90}, 
    {'name': 'Lorenzo', 'missions': 90}, 
    {'name': 'Emanuele', 'missions': 151}, 
    {'name': 'Sergey', 'missions': 138},
    {'name': 'Federico', 'missions': 88}
]

def statements(persons,file):
    
    template = env.get_template('expressions.txt')
    output = template.render(persons=persons,file=file)
    with open('3 - Expressions/rendered/expressions.txt', 'w') as res:
        res.write(output)
file=open('1 - Variables/rendered/showpersons.txt')
statements(persons,file)
file.close()
