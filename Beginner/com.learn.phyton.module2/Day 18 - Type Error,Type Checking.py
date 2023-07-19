#The len function does not work with Integer

#len(237_425_234) Output : TypeError
num_char=len("35favgh")
#print("hello " + num_char ) - Output : TypeError

# The function str convert input into String Type variable
var=str(num_char)
print("Print str  : "+var)

# Check the type of the variable
a=[1,43,2,6]
#print("The type is " + type(a)) Ouput : TypeError
print("The type is " + str(type(a)))
