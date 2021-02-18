name1 = input("Tell me a name.\n")
name2 = input("Tell me another name\n")

if name1[:3].lower() == name2[:3].lower():
    print("The first 3 letters are the same\n")
else: 
    print("The first 3 letters are not the same.\n")