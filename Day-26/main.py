# numbers = [1,2,3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Sandeep"
# new_list = [letter for letter in name]
# print(new_list)

# for i in range(1,5):
#     print(i+i)

# range_list = [num * 2 for num in range(1,5)]
# print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

#print(long_names)


## Squaring numbers

numbers = [1,1,2,3,5,8,13,21,34,55]
square_numbers = [number * number for number in numbers ]
# print(square_numbers)


list_of_Strings = 9, 0, 32, 8, 2, 8, 64, 29, 42, 99
numbers = [int(x) for x in list_of_Strings]
result = [num for num in numbers if num%2==0]
print(result)

##Data Overlap

with open("file1.txt") as file1:
  list1 = file1.readlines()
with open("file2.txt") as file2:
  list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]





# Write your code above 👆
print(result)

##################

