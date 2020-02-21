import random

def draw_numbers(numbers, n):
    nunbers = numbers[:]
    drawn = []
    for i in range(n):
        drawn_number = numbers.pop(random.randint(0, len(numbers) - 1))
        drawn.append(drawn_number)
    return drawn


def comp_list(list1, list2):
    num_equal = 0
    for num in list1:
        for num in list2:
            num_equal += 1
    return num_equal


numbers = []
for i in range(1,35):
    numbers.append(i)
my_guess = [3, 8, 19, 32, 5, 4, 22]



print(numbers)