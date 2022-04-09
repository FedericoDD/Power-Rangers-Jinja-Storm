from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('2 - Statements/templates'))


def statements(foods):
    template = env.get_template('Statements.html')
    output = template.render(foods=foods)
    env.trim_blocks = False
    env.lstrip_blocks = False
    with open('2 - Statements/rendered/Statements.html', 'w') as res:
        res.write(output)

foods = [
    {'name': 'Miso', 'kcal': 199}, 
    {'name': 'Ramen', 'kcal': 436}, 
    {'name': 'Salmon', 'kcal': 208}, 
    {'name': 'Tuna', 'kcal': 132}, 
    {'name': 'Rice', 'kcal': 130}, 
    {'name': 'Nori', 'kcal': 35},
    {'name': 'Anko', 'kcal': 242},
    {'name': 'Dorayaki', 'kcal': 289}, 
]

statements(foods)

########################################################################
######################### I N E R I T ##################################
########################################################################

# base template: base.html
# child template: about.html
template = env.get_template('about.html')
output = template.render()
with open('2 - Statements/rendered/about.html', 'w') as res:
        res.write(output)