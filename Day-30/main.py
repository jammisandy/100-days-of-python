try:
    file = open("a.file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
    sand = ["hi","hello","sand"]
    print(sand[9])
except FileNotFoundError:
    file = open("a.file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
except IndexError as index_mess:
    print(index_mess)
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
