def outer_function():
    print("i am outer function")

    def netsted_function():
        print("inner function")

    return netsted_function

inner_function = outer_function()
inner_function()