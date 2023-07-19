# function that allows inputs
def my_function(input_name, location):
    print(f"Hello {input_name}")
    print(f"What is it like in {location} ?")


name = input("Hi. Put your name please :\n")
location = input("Put your location please :\n")
# my_function(name, location)

my_function(location, name)  # the order of parameters is very important
# Keyword argument
my_function(input_name=name, location=location)
