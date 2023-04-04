import random

print("JACKPOT !!!\n")
print("Info:\norange 2x = 10x\nbell 3x = 3x\n7 3x = 100x\n")

itens = ['orange orange 7', 'bell bell bell', '7 7 7',
         'orange 7 bell', 'bell bell orange', '7 orange 7']

money = int(input("Insert the money: "))
roll = input("Roll ?\n")

result = random.choice(itens)

if roll == "yes":
    print("Result =", result)

    if result == (itens[0]):
        print("You won:",money * 2)
    elif result == (itens[1]):
        print("You won:",money * 3) 
    elif result == (itens[2]):
        print("You won:",money * 100)
    else:
        print("You lost")
 