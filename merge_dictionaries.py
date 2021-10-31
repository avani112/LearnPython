# define two dictionaries a and b
a = {"one": 1, "two": 2}
b = {"three": 3, "four": 4}

# merge two dictionaries (Python 3.9 or greater) and print result
c = a | b
print(c)

# merge two dictionaries (Python 3.5 or greater) and print result
c = {**a, **b}
print(c)
