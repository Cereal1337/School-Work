import random

num = random.randint(1, 10)

number = input("Please pick a number between 1 and 10: ")

if number == num:
    print("Thats correct!")
else:
    print("Thats not correct!")