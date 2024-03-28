## new_dict ={new_key:new_value for (key,value) in dict.items()}

names = ['Alex', 'bob', 'caroline', 'David', 'tim', 'Freddie']
import random
students_scores = {student:random.randint(1, 100) for student in names}
#print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
#print(passed_students)

## dict comprehension1

## result = {word:len(word) for word in sentense.split()}

##dict comrehen2

## weather_f = {day:temp * 9/5 + 32 for (day,temp) in weather_c.items()}

## iterate pandas data frame

import pandas
student_dict = {"student" : ["Angela", "James" ,"Lilly"],
                "score": [34,56,30]
                }

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

##Loop data frame

for(key,value) in student_data_frame.items():
    print(value)

for(index,row) in student_data_frame.iterrows():
    print(row.score)

