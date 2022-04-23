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

items = [
    {'name': 'Back jacket', 'cost': 9769}, 
    {'name': 'Black trousers', 'cost': 8898}, 
    {'name': 'Light sandals', 'cost': 10374}, 
    {'name': 'Hooded cowl', 'cost': 5347}, 
    {'name': 'Ninjato', 'cost': 88475}, 
    {'name': 'Ninja sword', 'cost': 6319658},
    {'name': 'Smoke bombs', 'cost': 10111},
    {'name': 'New katana', 'cost': 2527863}, 
]


def statements(persons,items):
    
    template = env.get_template('macros.txt')

    output = template.render(persons=persons,items=items)
    with open('4 - Macros/rendered/macros.txt', 'w') as res:
        res.write(output)

statements(persons,items)
