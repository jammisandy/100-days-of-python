#Addition
def addition(x, y):
    return x + y

#Multiplication
def substract(x, y):
    return x - y

#Addition
def multiply(x, y):
    return x * y

#Addition
def divide(x, y):
    return x / y

operations = {
    "+": addition,
    "-": substract,
    "*": multiply,
    "/": divide
}

repeat = True

while repeat:

   num1 = int(input("What is your first number:"))
   num2 = int(input("What is your second number:"))

   for symbol in operations:
       print(symbol)

   operation_symbol = input("Pick any operation from line above: ")

   calculation_function = operations[operation_symbol]
   answer = calculation_function(num1, num2)
   print(f"{num1}{operation_symbol}{num2} = {answer}")
   my_input = input("Do you want to continue 'Y' or 'N': ")
   if my_input == 'N':
      repeat = False
print("End of loop")
