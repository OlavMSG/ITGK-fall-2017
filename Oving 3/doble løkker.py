oppgave = input("oppgave: ")

if oppgave == "a":
    m = int(input("Fra m-gangen, m = "))
    n = int(input("Til n-gangen, n = "))
    antall = int(input("Antall ledd: "))

    for i in range(m, n+1, 1):
        print(i,"-gangen")
        for j in range(1, antall+1, 1):
            print(j*i)
elif oppgave == "b":

    n = int(input("Primtall opp til n, n = "))
    #primtall1 = 2

    for k in range(2, n+1):  #1 er ikke et primtall!
        a = k**0.5
        int_a = int(a)
        evt_primtall = True
        for l in range(2, int(a)+1, 1):
            m = k % l
            if m == 0:
                evt_primtall = False
        if evt_primtall:
            print(k)







