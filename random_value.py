import numbers
import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=5))
print(random.choices('AbCdEf', k=5))
print(",".join(random.choices('AbCdEf', k=5)))
print(",".join(random.choices(string.ascii_letters + string.digits, k=10)))

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

number = [1, 2, 3, 4, 5]
random.shuffle(number)
print(number)
num = list(map(int, string.digits))
random.shuffle(num)
print(num)