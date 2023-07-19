def my_function():
    result = 2 ** 3
    return result


def format_name(f_name, l_name) -> str:
    formatted_name = f"{f_name.title()} {l_name.title()}"
    return formatted_name


print(format_name("LEvis","wilSon"))
