import linecache


interrupt = 0

while interrupt == 0:
    UserInput = input()

    if UserInput == "print":
        readerprint = open("Liste.txt", "r")
        printread = readerprint.read()
        print(printread)
        readerprint.close()


    if UserInput == "stop":
       interrupt = interrupt + 1

    if UserInput == "add":
        print("to whom (line number)")
        
        line = linecache.getline("Liste.txt", int(input()))
        splitline = line.split(": ")

        numberlist = splitline[-1]

        print("how much do you want to add")
        addinput = input()
        
        Newdebt = int(numberlist) + int(addinput)
        print(Newdebt)

            
        