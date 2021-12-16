# 1-savol
def s1(students, chairs):
    return (students-chairs if students > chairs else 0)

print(s1(25,21))
print(s1(18,20))
# output : 4
# output: 0 


import random
# 4-savol
def s4(item):
    result_num = 0
    