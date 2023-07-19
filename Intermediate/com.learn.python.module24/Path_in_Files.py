import os

path_s_file = "C:\\Users\\Levis Wilson\\Desktop\\s.txt"
with open(path_s_file, mode="r", encoding="UTF-8") as file:
    content = file.read()
    print(content)
    file.close()

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
new_path = os.path.join(desktop_path, "s.txt")
with open(new_path, mode="a", encoding="UTF-8") as f:
    f.write("\nnew text added")
    f.close()
