# Return as an early exit
def format_name(f_name, l_name) -> str:
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    return f"Result: {f_name.title()} {l_name.title()}"


# Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))
