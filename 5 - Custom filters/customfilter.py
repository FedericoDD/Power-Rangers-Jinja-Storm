from jinja2 import Environment, FileSystemLoader
import statistics

env = Environment(loader=FileSystemLoader('5 - Custom filters/templates'))

persons = [
    {'name': 'Andrea', 'missions': 151}, 
    {'name': 'Matteo', 'missions': 90}, 
    {'name': 'Lorenzo', 'missions': 90}, 
    {'name': 'Emanuele', 'missions': 151}, 
    {'name': 'Sergey', 'missions': 138},
    {'name': 'Federico', 'missions': 88}
]


# C U S T O M   F I L T E R
def up1(val):
    val=val+1
    return val


env.filters["up1"] = up1
env.filters["mean"] = statistics.mean

def statements(persons):
    
    template = env.get_template('customfilter.txt')

    output = template.render(persons=persons)
    with open('5 - Custom filters/rendered/customfilter.txt', 'w') as res:
        res.write(output)

statements(persons)