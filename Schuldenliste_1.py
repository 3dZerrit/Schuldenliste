
import json
import colorama

colorama.init()


genopen = open("Liste.json", "r")
Alldict = json.loads(genopen.read())
genopen.close()


while True:
    UserInput = input()

    if UserInput == "print":
        for printen in Alldict.keys():
            if Alldict[printen] == 0:
                print(f"{printen}: {colorama.Fore.YELLOW}{str(Alldict[printen])}{colorama.Fore.RESET}")

            elif Alldict[printen] < 0:
                print(f"{printen}: {colorama.Fore.RED}{str(Alldict[printen])}{colorama.Fore.RESET}")
    
            elif Alldict[printen] > 0:
                print(f"{printen}: {colorama.Fore.GREEN}{str(Alldict[printen])}{colorama.Fore.RESET}")
            
        


    elif UserInput == "stop":
        print(f"{colorama.Fore.RED}Sucessfully stopped{colorama.Fore.RESET}")
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
    
    
