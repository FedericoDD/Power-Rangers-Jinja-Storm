from jinja2 import Environment, FileSystemLoader, select_autoescape

"""
Jinja uses a central object called the template Environment.
Instances of this class are used to store the configuration 
and global objects, and are used to load templates from the
file system or other locations. Even if you are creating
templates from strings by using the constructor of Template
class, an environment is created automatically for you,
albeit a shared one.
"""

env = Environment(loader=FileSystemLoader('1 - Variables/templates'),
        autoescape=select_autoescape(
        enabled_extensions=('txt'),
        default_for_string=True,)
 )

"""
To load a template from this environment, call the get_template()
method, which returns the loaded Template.
The template is retrieved from the templates directory.
"""

persons = [
    {'name': 'Andrea', 'age': 26}, 
    {'name': 'Matteo', 'age': 90}, 
    {'name': 'Lorenzo', 'age': 90}, 
    {'name': 'Federico', 'age': 88}, 
    {'name': 'Emanuele', 'age': 29}, 
    {'name': 'Sergey', 'age': 38}
]

template = env.get_template('showpersons.txt')

"""
To render it with some variables, call the render() method.

print(template.render(the="variables", go="here"))

Using a template loader rather than passing strings to Template 
or Environment.from_string() has multiple advantages. Besides being 
a lot easier to use it also enables template inheritance.
"""

output = template.render(persons=persons)
env.trim_blocks = False
env.lstrip_blocks = False
with open('1 - Variables/rendered/showpersons.txt', 'w') as res:
        res.write(output)

######################################################################
####################### F I L T E R S ################################
######################################################################

template = env.get_template('showpersons_filters.txt')
output = template.render(persons=persons)
with open('1 - Variables/rendered/showpersons_filters.txt', 'w') as res:
        res.write(output)