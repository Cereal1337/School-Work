myFile = open("file.txt", "w")
myFile.write("Hello\n")
myFile.write("Hi\n")
myFile.write("Greetings")

myFile = open("file.txt", "r")

def readAll():
    while True:
        f = myFile.readline()
        print(f)
        if f == "":
            exit()

readAll()
