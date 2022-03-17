user_input_number = int(input("Enter any integer number :"))
if user_input_number % 2 == 0:
    print(f"{user_input_number}  number is Even .")
else:
    print(f"{user_input_number} number is Odd.")

# Even number print 1 to 100
for i in range(1,100):
    if i % 2 == 0:
        print(i)

# Odd number print 1 to 100
print("Odd Number :")
for i in range(1,100):
    if i % 2 != 0:
        print("\t",i)

# Even number print 1 to user_input
user_input = int(input("Enter Any integer number :"))
for i in range(1, user_input+1):
    if i % 2 == 0:
        print(i)
#Odd number print 1 to user_input
user_input = int(input("Enter Any integer number :"))
for i in range(1, user_input+1):
    if i % 2 != 0:
        print(i)