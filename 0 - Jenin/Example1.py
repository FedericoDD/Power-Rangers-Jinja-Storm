from jinja2 import Template

t = Template("Hello {{ something }}! {# Hello! #}")
print(t.render(something="World"))
# 'Hello World!'