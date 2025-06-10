# 2. Student Grade Calculator 
# Create a program that: - Asks for a student’s name and 5 subject marks - Calculates the average - Displays a grade based on the average: 
# A (90–100) 
# B (80–89) 
# C (70–79) 
# D (60–69) 
# F (below 60)

def Student_Grade_Calculator ():
    grades = []

    name = input("Enter your're name: ")

    for i in range(5):
        userInput = input(f"Enter score {i + 1} : ")
        grades.append(float(userInput))
    
    total = sum(grades)
    
    average = total / 5
    
    grade = ""
    
    if average > 90:
        grade =  "A"
    elif average > 80:
        grade = "B"
    elif average > 70:
        grade = "C"
    elif average > 60:
        grade = "D"
    else:
        grade = "F"

    return [name, grade]
    
info = Student_Grade_Calculator()
    
print(f"hey {info[0]}, your score is  {info[1]}")