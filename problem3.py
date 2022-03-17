import math
def grade(number):
    if number > 100:
        return "Number greater than 100 !"
    elif number < 0:
        return "Number less than 0 !"
    elif number >= 80 and number <= 100:
        return "A+"
    elif number >= 70 and number < 80:
        return "A"
    elif number >= 60 and number < 70:
        return "A-"
    elif number >= 50 and number < 60:
        return "B"
    elif number >= 40 and number < 50:
        return "C"
    elif number >= 33 and number < 40:
        return "D"
    elif number >= 0 and number < 33:
        return "F"


def points(number):
    if number >= 80 and number <= 100:
        return 5.00
    elif number >= 70 and number < 80:
        return 4.00
    elif number >= 60 and number < 70:
        return 3.50
    elif number >= 50 and number < 60:
        return 3.00
    elif number >= 40 and number < 50:
        return 2.00
    elif number >= 33 and number < 40:
        return 1.00
    elif number >= 0 and number < 33:
        return 0.00



def totul_grade(number):
    if number > 4.00 and number <= 5.00:
        return "A+"
    elif number > 3.50 and number <= 4.00:
        return "A"
    elif number > 3.00 and number <= 3.50:
        return "A-"
    elif number > 2.00 and number <= 3.00:
        return "B"
    elif number > 1.00 and number <= 2.00:
        return "C"
    elif number > 0.00 and number <= 1.00:
        return"D"
    elif number == 0:
        return "F"


student_id = int(input("Enter student Id : "))
student_name = input("Enter student name : ")
student_roll = int(input("Enter student roll : "))
sub_bangla = int(input("Enter bangla mark : "))
sub_english = int(input("Enter english mark : "))
sub_math = int(input("Enter math mark : "))



point_bangla = points(sub_bangla)
point_english = points(sub_english)
point_math = points(sub_math)
totul_point = (point_bangla + point_english + point_math) / 3.00




print("\n\nSubject\t\tgrade\t\tPoints\n")
print(f"Bangal\t\t{grade(sub_bangla)}\t\t{point_bangla}")
print(f"English\t\t{grade(sub_english)}\t\t{point_english}")
print(f"Math\t\t{grade(sub_math)}\t\t{point_math}")
print("-" * 40)
print(f"Your Grade\t{totul_grade(totul_point)}\t\t{math.floor(totul_point) * 1.00}")
