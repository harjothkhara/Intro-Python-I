# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12


def changeX():
    global x
    x = 99


changeX()

# This prints 12. What do we have to modify in changeX() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y
        y = 999
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)


outer()

# Notes - Python 3 introduced the nonlocal keyword that allows you to assign to variables in an outer, but non-global, scope. ... The usage of nonlocal is very similar to that of global, except that the former is used for variables in outer function scopes and the latter is used for variable in the global scope
