#221RDB265 Vitalijs Vasiljevs
# P.s. Kad es apstiprinaju uzdevumu un apskatiju to, konstatēju, ka mans kods jau ir pilnībā pabeigts. 
# Es nezinu, vai tas bija tā plānots vai nē, uzdevuma nosacījumos par to nekas nav rakstīts.
# Tāpēc es izdzēsu visu veco kodu, kas nebija mans, un uzrakstīju savu no nulles.
import re

phoneNumbers = {}
def find(number, fromMain):
    global phoneNumbers
    if number in phoneNumbers:
        if fromMain:
            print(phoneNumbers[number])
        return True
    else:
        if fromMain:
            print("not found")
        return False
    
def printPhones():
    for number in phoneNumbers:
        print(number + " " + phoneNumbers[number])

def add(number, name):
    global phoneNumbers
    if find(number, False):
        delete(number, True)
    phoneNumbers[number] = name
    return


def delete(number, fromAdd):
    global phoneNumbers
    if fromAdd:
        del phoneNumbers[number]
    elif find(number, False):
        del phoneNumbers[number]
    return 
    


def main():
    countComands = int(re.sub("[\r\n]", "", input()))
    for i in range(countComands):
        comandsList = []
        comandsList = re.sub("[\r\n]", "", input()).split()
        comand = comandsList[0].lower()
        if comand == "add":
            add(comandsList[1], comandsList[2])
        elif comand == "del":
            delete(comandsList[1], False)
        elif comand == "find":
            find(comandsList[1], True)
        elif comand == "print":
            printPhones()
        else:
            printPhones("wrong command")
        
        
if __name__ == "__main__":
    main()
