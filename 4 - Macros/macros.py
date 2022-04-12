from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('4 - Macros/templates'))

persons = [
    {'name': 'Andrea', 'missions': 151}, 
    {'name': 'Matteo', 'missions': 90}, 
    {'name': 'Lorenzo', 'missions': 90}, 
    {'name': 'Emanuele', 'missions': 151}, 
    {'name': 'Sergey', 'missions': 138},
    {'name': 'Federico', 'missions': 88}
]



def statements(persons):
    
    template = env.get_template('macros.txt')

    output = template.render(persons=persons)
    with open('4 - Macros/rendered/macros.txt', 'w') as res:
        res.write(output)

