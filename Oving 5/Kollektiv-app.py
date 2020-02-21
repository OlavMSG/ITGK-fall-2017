def pris(alder, sykkel):
    pris = 0
    if sykkel == "j":
        pris += 50
    if alder < 5 or alder > 60:
        pris += 0
    elif alder < 21:
        pris += 20
    elif alder < 26:
        pris += 50
    else:
        pris += 80

    print("Prisen på billett nr.", i,"er", pris, ",-")
    return int(pris)


print("Velkommen til vår Kollektiv-app \n")

antall = int(input("Hvor mange billetter vil du kjøpe? "))
pris1 = 0
for i in range(1, antall+1, 1):
    print("Hvor gammel er personen som billett nr.", i, end="")
    alder = int(input(" er for? "))
    sykkel = "K"
    while sykkel != "j" and sykkel != "n":
        sykkel = input("Har personen med seg sykkel(j/n)? ")
        if sykkel != "j" and sykkel != "n":
            print("Du må svare j eller n.")

    pris1 += pris(alder, sykkel)
print("\nDu må betale", pris1, ",- Ha en fin tur.")



