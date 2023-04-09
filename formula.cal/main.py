from newcalci import calci


def choice():
    e = input("enter c for continue or enter e for exit : ")
    while e != "c" and e != "e":
        print("please enter a valide option")
        e = input("enter c for continue or enter e for exit : ")
    return e


while choice() == "c":
    calci()
