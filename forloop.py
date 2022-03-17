# #1st class
# for number in range(1,10,2):
#     print("Attempt", number , number * ".")

#2nd class
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempt 3 times and failed")
    