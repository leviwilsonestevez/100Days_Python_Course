try:
    with open("s", "r") as non_existing_file:
        non_existing_file.write("Nothing")
except FileNotFoundError as non_exist_file_error:
    print("This is a FileNotFoundError")
finally:
    print("This message appears wether or not exists an error.Next a raised Error")
    raise TypeError("This is an error that I made up")
