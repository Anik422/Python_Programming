numbers = int(input("Enter any integer number :"))
count = 0
for number in range(1, numbers):
    if number % 2 == 0:
        print(number)
        count += 1
print(f"We have {count} even numbers")