# enimies = 1

# def my_func():
#     global enimies
#     enimies += 1
#     print(f"Number of enimies are {enimies}")

# my_func()
# enimies = 10

# print(f"Number of enimies are {enimies}")

enimies = 2

def my_func():
    print(f"Number of enimeies are {enimies}")
    return enimies + 10

enimies = my_func()
print(enimies)