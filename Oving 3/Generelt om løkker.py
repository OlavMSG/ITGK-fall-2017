print("#Oppgave a")

sum = 0
for i in range(1, 101, 1): #Summerer 1+2+3+...+99+100
    sum += i
print("Summen av de", 100, "første tallene er", sum)

print("#Oppgve b")

produkt = 1
g = 0
for j in range(1, 8, 1): #trenger kun 8 her fordi 1*2*3*4*5*6 = 720
    if produkt < 1000:
        produkt *= j
        print(produkt)
        g += 1
    else:
        break
print("Løkken kjørte", g, "ganger, produktet ble", produkt)

print("#Oppgave c")

rett_svar = "pizza"
svar = input("Hva er volum til en pizza med radius z og høyde a? ")
while svar != rett_svar:
    print("Det var feil svar, prøv igjen.")
    svar = input("Hva er volum til en pizza med radius z og høyde a? ")
print("Gratulerer,", svar, "stemmer.")

