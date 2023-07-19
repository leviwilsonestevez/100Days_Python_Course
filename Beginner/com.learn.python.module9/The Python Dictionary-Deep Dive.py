# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1: 'apple', 2: 'ball'})

# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'ball')])

mexico_cities = dict([(1, "Ciudad de Mexico"), (2, "Monterrey"), (3, "Guadalajara")])
print(mexico_cities)
print(mexico_cities[1])
for key in mexico_cities:
    print(key)
    print(mexico_cities[key])
