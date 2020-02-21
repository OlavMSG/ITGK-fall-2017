print("# Oppgave a:")
a = float(input("Et tall: "))
b = float(input("Et tall til: "))
print("a*b =",a*b,"og a+b =",a+b)
if a*b < a+b:
    print("Det minste er ", a*b)
else:
    print("Det minste er ", a+b)
print("# Oppgave b:")
rett = 3*4
print("Hva er 3*4?",end="")
svar = float(input(" Skriv inn ditt svar: "))
if svar == rett:
    print("Du svarte riktig!")
else:
    print("Du svarte feil, rett svar var ", rett,". Du svarte ", svar)