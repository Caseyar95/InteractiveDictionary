import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def printDef ():
    q = "go"
    while q != "q":
        
        userWord = input("Enter word: ")

        i = 0;
        y = 0;
        z = 0;
        success = 0;
        userWord = userWord.lower()
        if userWord == "q":
            print("See you later")
            q = "q"
            break

        try:
            altWord = get_close_matches(userWord, data.keys(), cutoff=0.8)[0]
        except IndexError:
            i = 1

        try:
            altTitle = get_close_matches(userWord.title(), data.keys(), cutoff=0.8)[0]
        except IndexError:
            y = 1

        try:
            altAcro = get_close_matches(userWord.upper(), data.keys(), cutoff=0.6)[0]
        except IndexError:
            z = 1

        if userWord in data:
            for item in data[userWord]:
                print(item) #return here
            print("\n")
            break

        elif userWord.title() in data:
            for item2 in data[userWord.title()]:
                print(item2)
            print("\n")
            break

        elif userWord.upper() in data:
            for item4 in data[userWord.upper()]:
                print(item4)
            print("\n")
            break

        elif  i != 1 :
            print("The word doesn't exist.")
            yn = input("Did you mean %s?  Enter y if yes, or n if no: \n" % altWord) 
            yn = yn.lower()

            if yn == "y" or yn == "yes":
                for item1 in data[altWord]:
                    print(item1) #return here
                print("\n")
                break
            elif yn == "q":
                print("See you later")
                q = "q"
                break
            elif yn == "n" or yn == "no":
                print ("Okay... ")
            else:
                print("Sorry, please try again")
                success = 1


        if y != 1:
            nn = input("Did you mean %s?  Enter y if yes or n if no: \n" % altTitle)
            nn = nn.lower()
            if nn == "y" or nn == "yes":
               for item3 in data[altTitle]:
                   print(item3) #return here
               print("\n")
               break
            elif nn == "q":
                print("See you later")
                q = "q"
                break
            elif yn == "n" or yn == "no":
                print("Okay...")
            else:
                print("Sorry, please try again")
                success = 1

        if z != 1:
                zn = input("Did you mean %s?  Enter y if yes or n if no: \n" % altAcro)
                zn = zn.lower()
                if zn == "y" or zn == "yes":
                    for item5 in data[altAcro]:
                        print(item5) #return here
                    print("\n")
                    break
                elif zn == "q":
                    print("See you later")
                    q = "q"
                    break
                else:
                    print ("Sorry please try again")

        else:
            print ("Sorry please try again")

    print(":D")
    
print("At any time press q to quit")
printDef()