import random
print("You can guess 3 times from 1 to 5")
for i in range(3):
    user_input = int(input(f"Enter guessing number {i+1} : "))
    n = random.randint(1, 5)
    if n == user_input:
        print("Congratulations! You are win.")
        break
    elif n < user_input:
        print("You Guessed too high!")
        print(f"Correct answer = {n}")
    elif n > user_input:
        print("You guessed too small!")
        print(f"Correct answer = {n}")
print("Thank you for play game.")
