print("Velkommen til TravelevatoR. \nVi tilbyr reiser fra Trondheim til Pythonville")
dager = int(input("Dager til du skal reise? "))

if dager < 0:
    print("Har du en tidsmaskin????")
elif dager >= 14:
    print("Du kan få minipris: ", 199, ",- kan ikke refunderes/endres")
    janei = input("Ønskes dette (J/N)? ")

    if janei == "J":
        print("Takk for pengene, god reise!")
    elif janei == "N":
        print("Da tilbyr vi fullpris:", 440, ",-")
        alder = int(input("Skriv inn din alder: "))
        if alder < 0:
            print("En feil har oppstått, vær så snill å kjør programet på nytt")
        elif alder < 16:
            pris = 440*50/100
            print("Prisen på biletten blir: ", pris, ",-")
        elif alder >= 60:
            print("Du er Senior (60+)")
            pris = 440*75/100
            print("Prisen på biletten blir: ", pris, ",-")
        else:
            honor = input("Er du Student eller Millitær i uniform (J/N)? ")
            if honor == "J":
                pris = 440*75/100
                print("Prisen på biletten blir: ", pris, ",-")
            elif honor == "N":
                print("Da tilbyr vi fullpris:", 440, ",-")
            else:
                print("En feil har oppstått, vær så snill å kjør programet på nytt")
    else:
        print("En feil har oppstått, vær så snill å kjør programet på nytt")

else:
    print("For sent for minipris; fullpris", 440, ",-")
    alder = int(input("Skriv inn din alder: "))
    if alder < 0:
        print("En feil har oppstått, vær så snill å kjør programet på nytt")
    elif alder < 16:
         pris = 440*50/100
         print("Prisen på biletten blir: ", pris, ",-")
    elif alder >= 60:
        print("Du er Senior (60+)")
        pris = 440*75/100
        print("Prisen på biletten blir: ", pris, ",-")
    else:
        honor = input("Er du Student eller Millitær i uniform (J/N)? ")
        if honor == "J":
            pris = 440*75/100
            print("Prisen på biletten blir: ", pris, ",-")
        elif honor == "N":
            print("Da tilbyr vi fullpris:", 440, ",-")
        else:
            print("En feil har oppstått, vær så snill å kjør programet på nytt")
