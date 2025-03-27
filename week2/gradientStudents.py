import os

def gradingStudents(grades):
    # Lista para armazenar as notas arredondadas
    rounded_grades = []  
    
    for grade in grades:  
        if grade < 38:  
            rounded_grades.append(grade)
        else:
            next_multiple = ((grade // 5) + 1) * 5  
            if (next_multiple - grade) < 3:  
                rounded_grades.append(next_multiple)
            else:
                rounded_grades.append(grade)
    
    return rounded_grades 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []
    for _ in range(grades_count):
        grades.append(int(input().strip()))

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)) + '\n')

    fptr.close()
