# marksheet making
def result_output(result):
    if result >= 80 and result <= 100:
        return "A+"
    elif result >= 70 and result <= 79:
        return "A"
    elif result >= 60 and result <= 69:
        return "A-"
    elif result >= 50 and result <= 59:
        return "B"
    elif result >= 40 and result <= 49:
        return "C"
    elif result >= 33 and result <= 39:
        return "D"
    elif result > 100:
        return "mark can not be bigger then 100"
    else:
        return "F"


# Name = input(("Enter name:"))
# Roll = int(input(("Enter roll:")))
# classes = int(input(("Enter class:")))
# IdNo= int(input(("Enter Id_No:")))
english = int(input(("Enter English mark:")))
chemistry = int(input(("Enter chemistry mark:")))
physic = int(input(("Enter physics mark:")))
Islam = int(input(("Enter Islam mark:")))
# Total = english + chemistry + physic + Islam
# def gift (Total):
# print(Total)

# gift(Name,Roll,classes,IdNo,english,chemistry,physic,Islam)


print(f"English = {result_output(english)}")
print(f"English = {result_output(chemistry)}")
print(f"English = {result_output(physic)}")
print(f"English = {result_output(Islam)}")


