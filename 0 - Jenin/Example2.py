from jinja2 import Template

t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
msg=t.render()
print(msg)
# 'My favorite numbers: 1 2 3 4 5 6 7 8 9 '