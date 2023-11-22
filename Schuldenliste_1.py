
import json

genopen = open("Liste.json", "r")
Alldict = json.loads(genopen.read())
genopen.close()


while True:
    UserInput = input()

    if UserInput == "print":
        pass

    elif UserInput == "stop":
        break

    elif UserInput == "add":
        print("Whose debt would you like to change?")
        Person = input().lower()
        if Person in Alldict.keys():  
            print("what would you like to change")
            Alldict[Person] = Alldict[Person] + int(input())

        else:
            print("Would you really like to add this person to the list? [Y]es [n]o")
            if input() == "Y":
                Alldict[Person] = 0
                print("what would you like to change")
                Alldict[Person] = Alldict[Person] + int(input())
        

            
        
    else:
        print("nuh uh")


genwrite = open("Liste.json", "w")
genwrite.truncate(0)
genwrite.write(json.dumps(Alldict))
genwrite.close()
    
    