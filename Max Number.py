x = int(input("Enter 1st number :"))
y = int(input("Enter 2nd number :"))
z = int(input("Enter 3rd number :"))
if x>y:
    if x>z:
        print(f"The 1st number is max_number = {x}.\n")
    else:
        print(f"The 3rd number is max_number : {z}.\n")
elif y>x:
    if y>z:
        print(f"The 2nd number is max_number :{y}.\n")
    else:
        print(f"The 3rd number is max_number : {z}.\n")
elif x==y and x==z and z==y:
    print("The three number is same.\n")
else:
    print("Two Number is same!\n")