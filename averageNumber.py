def averageNumber():
    num1 = int(input("Pick a number. "))
    num2 = int(input("Pick another number. "))
    num3 = int(input("Pick another number. "))

    num = num1 + num2 + num3
    average = num / 3
    print(f"The average value is {average}")

averageNumber()