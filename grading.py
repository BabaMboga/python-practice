#Tammy
grade = int(input("Grade: "))
def gradeCalculator(grade):
    if grade <= 100 and grade >= 90:
        print("You got an A*")
    elif grade < 90 and grade >= 80:
        print("You got an A")
    elif grade < 80 and grade >= 70:
        print("You got a B")
    elif grade < 70 and grade >= 60:
        print("You got a C")
    elif grade < 60 and grade >= 50:
        print("You got a D")
    elif grade < 50 and grade >= 40:
        print("You got an E")
    elif grade < 40 and grade >= 0:
        print("You Failed Bruh")
    elif grade < 0 or grade > 100:
        print("Incorrect input, try again")
gradeCalculator(grade)