
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
        print(Person)
        
        Person in Alldict
        
    else:
        print("nuh uh")


genwrite = open("Liste.json", "w")
genwrite.truncate(0)
genwrite.write(json.dumps(Alldict))
genwrite.close()
    
    