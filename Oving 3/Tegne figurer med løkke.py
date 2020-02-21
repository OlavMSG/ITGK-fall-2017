from turtle import *
oppgave = input("Hvilken oppgave: ")
if oppgave == "a":
    for i in range(1, 5, 1):
        forward(100)
        left(90)

elif oppgave == "b":
    for i in range(16, 0, -3): # starter på 16, trekker fra 3 hver gang
        pensize(i)  # gradvis tynnere penn etter som i minker
        forward(50)
elif oppgave == "c":
    for i in range(0, 36, 1):
        forward(250-7*i)
        left(90)
        forward(250-7*i)
        left(90)
elif oppgave == "d":
    print("Jeg kan tegne et polygon.")
    kanter = int(input("Velg antall kanter: "))
    omkrets = float(input("Velg omkrets på polygonet: "))
    i = 0
    while i != 360:
        forward(omkrets/kanter)
        left(360/kanter)
        i += 360/kanter
elif oppgave == "e":  #valgte å bruke while-løkke
    print("Jeg kan tegne en 'polygon blomst'.")
    kanter = int(input("Velg antall kanter: "))
    omkrets = float(input("Velg omkrets på polygonet: "))
    antall = int(input("Antall polygon i blomsten: "))

    i = 0
    j = 0
    while j != antall:
        if i != 360:
            while i != 360 and j != antall:
                forward(omkrets/kanter)
                left(360/kanter)
                i += 360/kanter
            left(360/antall)
            i = 0
            j += 1


else:
    print("Error")






