def my_func(f_name,l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide proper firstname and lastname"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result:{formated_f_name} {formated_l_name}"

print(my_func(input("What is your first name?"), input("What is your last name?")))