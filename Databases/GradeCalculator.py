def GradeCalclator(number):
    #number = int(input("What score did you get? "))
    if number >= 90:
        print("A*")
    elif number >= 80:
        print("A")
    elif number >= 70:
        print("B")
    elif number >= 60:
        print("C")
    else:
        print("Fail")

GradeCalclator(39)

