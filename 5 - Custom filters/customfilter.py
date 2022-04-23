from jinja2 import Environment, FileSystemLoader

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

def average(sum_var,num): 
    """
    sum_var = sum of elements
    num = number of elements
    """
    try:
        avg = sum_var / num
    except ZeroDivisionError:
        avg='NaN'
    return avg

env.filters["up1"] = up1
env.globals["average"] = average

file=open('4 - Macros/rendered/macros.txt','r')


# S T R E A M
def statements(persons,file):

    template = env.get_template('customfilter.txt.jinja')
    
    """
    You can use stream instead of render and dump insteas of "with open..."
    to use memory in a more efficiency way.
    """
    
    output = template.stream(persons=persons,file=file).dump('5 - Custom filters/rendered/customfilter.txt')

statements(persons,file)