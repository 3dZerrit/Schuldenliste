while True:
    UserInput = input()

    if UserInput == "print":
        readerprint = open("Liste.txt", "r")
        printread = readerprint.read()
        print(printread)
        readerprint.close()

    elif UserInput == "stop":
        break

    elif UserInput == "add":
        print("to whom (line number)")
        
        reader = open("Liste.txt","r")
        line = reader.read().split("\n")[int(input())]
        splitline = line.split(": ")

        numberlist = splitline[-1]

        print("how much do you want to add")
        addinput = input()
        
        Newdebt = int(numberlist) + int(addinput)
        print(Newdebt)
    else:
        print("nuh uh")
