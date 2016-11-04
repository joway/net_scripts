from hack_hznu_teacher import hack_teacher

with open('teacher.txt') as file:
    line = file.readline()
    while line:
        stu_num = line[:-1]
        hack_teacher(stu_num)
        line = file.readline()
