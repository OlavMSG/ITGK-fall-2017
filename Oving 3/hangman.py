hemmelig_ord = input("Hemmelig ord: ")
antall_liv = int(input("Hvor mange liv har du? "))

while True:
    bokstav = input("Gjett en bokstav: ")
    while len(bokstav) > 1:
        bokstav = input("Du kan bare gjette en bokstav: ")

    er_i_ord = False
    for c in hemmelig_ord:
        if c == bokstav:
            er_i_ord = True
    if not er_i_ord:
        print("Bokstaven", bokstav, "er ikke i ordet")
        antall_liv -= 1
        if antall_liv ==0:
            print("Du tapte.")