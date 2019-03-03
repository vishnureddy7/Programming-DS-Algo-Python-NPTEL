#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs08/progassignment?action=submit&name=108

import sys

def sort_key(student):
    return student[0];

current = 'Courses';
courses = dict();
students = dict();
grades = dict();
grade_points = {'A':10,'AB':9,'B':8,'BC':7,'C':6,'CD':5,'D':4}
while(True):
    line = input();
    if(line == 'Courses'):
        current = 'Courses';
        continue;
    elif(line == 'Students'):
        current = 'Students'
        continue;
    elif(line == 'Grades'):
        current = 'Grades';
        continue;
    elif(line == 'EndOfInput'):
        break;
    elif(current == 'Courses'):
        code,name,sem,year,instr = line.split('~');
        courses[code] = (name,sem,year,instr);
    elif(current == 'Students'):
        roll,name = line.split('~');
        students[roll] = name;
    elif(current == 'Grades'):
        code,sem,year,roll,grade = line.split('~');
        try:
            grades[roll].append((code,sem,year,grade_points[grade]));
        except:
            grades[roll] = [(code,sem,year,grade_points[grade])];

students = sorted(students.items(), key=sort_key);
for student in students:
    line = student[0]+'~'+student[1]+'~';
    points = 0;
    try:
        for grade in grades[student[0]]:
            points += grade[3];
        points = round(points/len(grades[student[0]]),2)
    except:
        pass;
    line += str(points);
    print(line);
