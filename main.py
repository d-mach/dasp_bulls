import random


DELKA = 4

print(f"""
Hi there!
-----------------------------------------------
I've generated a random {DELKA} digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
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

#print(vyber_pocitace)

pokusy = 0
bull = 0
while bull < DELKA:
    while True:
        vyber = input(">>> ")
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

    pokusy += 1
         
    bull = 0
    cow = 0
    for p, u in zip(vyber_pocitace, vyber):
        if p == u:
            bull += 1
        elif u in vyber_pocitace:
            cow += 1
    
    if bull < DELKA:    
        print(f"{bull} bull{'' if bull == 1 else 's'}, {cow} cow{'' if cow == 1 else 's'}")
        print("-----------------------------------------------")
    else: 
        print(f"Correct, you've guessed the right number\nin {pokusy} guesses!")
        print("-----------------------------------------------")
        print("That's amazing!")
    
      
    
    
          
