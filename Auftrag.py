from timeit import default_timer 
import random

# Auftrag [Name, Erstellung, Annahme, Bearbeitet]
def Auftragsgenerator():
    name = str(random.random())
    Auftrag = [ name , default_timer() ,0.0 , 0.0]

    return Auftrag


def AuftragsListe(number): 
    myList = [[] * 4] * number
    for auftrag in myList:
        auftrag = Auftragsgenerator()
    return auftrag



# Verarbetung der Aufträgee
def AuftragsVerarbeiter():

    return()

# Bestimmt Reihenfolge der Aufträge
def AuftragsAuflister():

    return()


def AuftragsStatisitc():

    return()