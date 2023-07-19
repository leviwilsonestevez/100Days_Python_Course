file = open("my_file.txt")  # open with only read mode
# alternative syntaxis
content = file.read()
print(content)
file.close()
if file.closed:
    print("The file is closed")

with open("my_file.txt", mode="a") as files:
    files.write("\nNew text add to my file")
