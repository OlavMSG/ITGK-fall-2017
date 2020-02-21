from random import *

random_numbers = []
for i in range(100):
    random_numbers.append(randint(1, 10))
print(random_numbers)

count_2 = random_numbers.count(2)


print("Antall 2-ere i random_numbers er ", count_2)

sum = 0
for c in range(len(random_numbers)):
    sum += random_numbers[c]

print("Summen til random_numbers er ", sum)

random_numbers.sort()
print("Sortert random_numbers: ",random_numbers)

mest = 0
nummer = 0
for k in range(1, 11):
    antall = random_numbers.count(k)
    if mest < antall:
        mest = antall
        nummer = k

print("Det er mest av nummer ", nummer)

random_numbers.reverse()
print(random_numbers)


