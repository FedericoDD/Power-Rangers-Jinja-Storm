from jinja2 import Environment, FileSystemLoader

"""
Here you can see how to use a loop ( {% for [...] %} [...] {% endfor %} )
and conditionals ( {if [...]} do this {% elseif [...] %} do this {% else %} do this {% endif %} )
"""

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

"""
Here you can use {% set line %} [...] {% endset %} to create the same file. 
Also you can create a base template (base.html) and a child template (about.html) to 
create a nested template.
"""
template = env.get_template('about.html')
output = template.render(foods=foods)
with open('2 - Statements/rendered/about.html', 'w') as res:
        res.write(output)