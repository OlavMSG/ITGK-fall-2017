print("#oppgave a")
n = int(input("n = "))
sum_tall = 0
for i in range(1, n+1, 1):
    if i%2 != 0:
        sum_tall += i**2
    else:
        sum_tall -= i**2

print("Summen av tallserien er", sum_tall)

print("#oppgave b")
sum_tall = 0
k = int(input("k = "))
g = 0
for i in range(1, n+1, 1):
    if i%2 != 0:
        if sum_tall + i**2 > k:
            break
        else:
            sum_tall += i**2
    else:
        sum_tall -= i**2
    g += 1

print("Den minsste av tallseien under", k, "er", sum_tall,". Tallserien har", g, "elementer")
