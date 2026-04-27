import random


DELKA = 4

print(f"""
Hi there!
-----------------------------------------------
I've generated a random {DELKA} digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------""")

moznosti = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
vyber_pocitace = [random.choice(moznosti)]
moznosti.remove(vyber_pocitace[0])
moznosti.append("0")

kolik_jeste = DELKA-1
while kolik_jeste > 0:
    r = random.choice(moznosti)
    vyber_pocitace.append(r)
    moznosti.remove(r)
    kolik_jeste -= 1

print(vyber_pocitace)

while True:
    vyber = input("Enter a number: ")
    if len(vyber) != DELKA:
        print(f"Please enter {DELKA} digits")
    elif not vyber.isdigit():
        print("Please enter only digits") 
    elif vyber[0] == "0":
        print("Please don´t start with zero")
    else:
        duplicity = set()
        for x in vyber:
            duplicity.add(x)
        if len(duplicity) != DELKA:
            print("Please don´t use digits repeatedly") 
        else:
            break
    
