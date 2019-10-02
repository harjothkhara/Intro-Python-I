# Loops
print("Hello, world!")
​
a = 10
b = 20
​
print(f"a + b is {a+b}")
​
for i in range(10, 5, -1):  # this is a comment
    print(i)
​
for i in "hello":
    print(i)
​
x = 0
​
while x < 5:
    print(x)
    x += 1   # x++

# Functions


def add10(x):
    print(f"x is {x}")
    return x + 10


​


def addxy(x, y):
    return x + y


​


def hello():
    print("Hello, world!")


​
print(add10(5))
print(add10(2))

# Global


def foo():
    global x


​
print(f"1: x is {x}")
x = 10
print(f"2: x is {x}")
​
x = 20
​
foo()
​
print(x)

# List
numbers = [1, 2, 3, 4, 5]
​
print(numbers)
​
for i in numbers:
    print(i)
​
for i in range(len(numbers)):
    print(f"{i}: {numbers[i]}")
​


def print_last_in_list(l):
    #print(l[len(l) - 1])
    print(l[-2])


​
print_last_in_list(numbers)

# List comprehensions
​
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
​
"""
cap_names = []
​
for n in names:
    cap_names.append(n.capitalize())
"""
​
#                output             for                if
cap_names = [n.capitalize() for n in names if n[0] != 's']
​
print(cap_names)

# Dictionaries

# create an empty dictionary
d = {}
​
# create a dictionary with at least two key : value pairs
e = {"foo": 12, "bar": 20}
​
# access & print an element in the dictionary
print(e["bar"])
​
# iterate through dictionary
for k in e:
    print(f'{k} is {e[k]}')
