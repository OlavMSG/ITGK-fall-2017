poeng = float(input("Skriv inn din poengsum: "))
lovligpoeng = poeng - int(poeng)
if lovligpoeng != 0:
    print("Feilmelding: Poengsummen du anga er ikke et heltall")
elif poeng > 100 or poeng < 0:
    print("Poengsummen du har angitt ligger ikke mellom 0 og 100."
          "Du skrev inn poengsummen:", poeng)
elif poeng >= 89:
    print("Du fikk A")
elif poeng >= 77:
    print("Du fikk B")
elif poeng >= 65:
    print("Du fikk C")
elif poeng >= 53:
    print("Du fikk D")
elif poeng >= 41:
    print("Du fikk E")
else:
    print("Du fikk F")