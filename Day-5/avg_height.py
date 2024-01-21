student_heights = input().split()
total_hight = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total_hight += student_heights[n]
  avg_hight = total_hight / len(student_heights)
print("total_height=", total_hight)
print("number of students=", len(student_heights))
print("average height=", int(avg_hight))
