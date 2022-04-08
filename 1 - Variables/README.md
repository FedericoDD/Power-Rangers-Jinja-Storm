# Variables

You can use a dot (.) to access attributes of a variable in addition to the standard Python `__getitem__` “subscript” syntax ([]).

The following lines do the same thing: \
`{{ foo.bar }}`\
`{{ foo['bar'] }}`

It’s important to know that the outer double-curly braces are not part of the variable, but the print statement. If you access variables inside tags don’t put the braces around them.

If a variable or attribute does not exist, you will get back an undefined value. What you can do with that kind of value depends on the application configuration: the default behavior is to evaluate to an empty string if printed or iterated over, and to fail for every other operation.

**Variables can be modified by filters.**\
 Filters are separated from the variable by a pipe symbol (|) and may have optional arguments in parentheses. Multiple filters can be chained. The output of one filter is applied to the next.

For example, `{{ name|striptags|title }}` will remove all HTML Tags from variable name and title-case the output (`title(striptags(name)`)).

Filters that accept arguments have parentheses around the arguments, just like a function call. For example: {{ `listx|join(', ') `}} will join a list with commas (`str.join(', ', listx)`).

The List of Builtin Filters below describes all the builtin filters: 
https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters