from tkinter import *
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


window = Tk()
window.wm_title("Dictionary")

data = json.load(open("data.json"))

def clearWindow():
    list1.delete(0, END)

def printDef ():
        var.set("")
        i = 0;
        y = 0;
        z = 0;
        userWord = word_text.get()
        userWord.lower()

        try: #trying to create close matches with all lowercase, proper nouns, and all caps
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

        if userWord in data: #printing definition if exact match is found
            for item in data[userWord]:
                list1.insert(END, item)
            return

        elif userWord.title() in data:
            for item2 in data[userWord.title()]:
                list1.insert(END, item2)
            return

        elif userWord.upper() in data:
            for item4 in data[userWord.upper()]:
                list1.insert(END, item4)
            return

        if  i != 1 : #if all lowercase match is found
            list1.insert(END, ("Did you mean %s?  Enter y if yes, or n if no: \n" % altWord))
            window.wait_variable(var)

            if var.get() == "yes":
                for item1 in data[altWord]:
                    list1.insert(END, item1)
                return
            elif var.get() == "no":
                list1.insert(END, "Okay... ")
            else:
                list1.insert(END, "Sorry, please try again")
                return


        if y != 1: #if proper noun match is found
            list1.insert(END, ("Did you mean %s?  Enter y if yes or n if no: \n" % altTitle))
            window.wait_variable(var)

            if var.get() == "yes":
               for item3 in data[altTitle]:
                   list1.insert(END, item3)
               return
            elif var.get() == "no":
                list1.insert(END, "Okay...")
            else:
                list1.insert(END, "Sorry, please try again")
                return


        if z != 1: #if uppercase match is found
            list1.insert(END, ("Did you mean %s?  Enter y if yes or n if no: \n" % altAcro))
            window.wait_variable(var)

            if var.get() == "yes":
                for item5 in data[altAcro]:
                    list1.insert(END, item5)
                return
            else:
                list1.insert(END, "Sorry please try again")
                return

        #no matches found
        list1.insert(END, "Sorry please try again")
        return




lWord = Label(window, text="Enter word --->")
lWord.grid(row=0, column=0)

word_text = StringVar()
eWord = Entry(window, textvariable=word_text)
eWord.grid(row=0, column=1)

list1 = Listbox(window, height=6, width=100)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)

sbList = Scrollbar(window)
sbList.grid(row=2, column=2, rowspan=7)

list1.configure(yscrollcommand=sbList.set)
sbList.configure(command=list1.yview)

#sbList2 = Scrollbar(window)
#sbList2.grid(row=8, column=1, columnspan=2)

#list1.configure(xscrollcommand=sbList2.set)
#sbList2.configure(command=list1.xview)

var = StringVar()

bYes = Button(window, text="Yes", width=10, command=lambda: var.set("yes"))
bYes.grid(row=3, column=3)

bNo = Button(window, text="No", width=10, command=lambda: var.set("no"))
bNo.grid(row=5, column=3)

bNo = Button(window, text="Close", width=10, command=window.destroy)
bNo.grid(row=7, column=3)

bRun = Button(window, text="Start", width=10, command=printDef)
bRun.grid(row=0, column=2)

bClear = Button(window, text="Clear", width=10, command=clearWindow)
bClear.grid(row=6, column=3)


window.mainloop()
