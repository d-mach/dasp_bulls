import random


DELKA: int = 4 


def pozdrav(pocet_cislic: int):
    print(f"""
Hi there!
-----------------------------------------------
I've generated a random {pocet_cislic} digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------""")


def vygeneruj_cislo(pocet_cislic: int) -> list[str]:
    moznosti: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    vyber_pocitace: list[str] = [random.choice(moznosti)]
    moznosti.remove(vyber_pocitace[0])
    moznosti.append("0")

    kolik_jeste: int = pocet_cislic-1
    while kolik_jeste > 0:
        r: str = random.choice(moznosti)
        vyber_pocitace.append(r)
        moznosti.remove(r)
        kolik_jeste -= 1

    return vyber_pocitace


def pokus_uzivatele(pocet_cislic: int) -> str:
    while True:
        vyber: str = input(">>> ")
        if len(vyber) != pocet_cislic:
            print(f"Please enter {pocet_cislic} digits")
        elif not vyber.isdigit():
            print("Please enter only digits") 
        elif vyber[0] == "0":
            print("Please don´t start with zero")
        else:
            duplicity: set = set()
            for x in vyber:
                duplicity.add(x)
            if len(duplicity) != pocet_cislic:
                print("Please don´t use digits repeatedly") 
            else:
                break

    return vyber


def vyhodnot_pokus(vyber_pocitace: list[str], vyber: str) -> tuple[int, int]:
    bull: int = 0
    cow: int = 0
    for p, u in zip(vyber_pocitace, vyber):
        if p == u:
            bull += 1
        elif u in vyber_pocitace:
            cow += 1
    
    return (bull, cow)


def main():
    pozdrav(DELKA)
    vyber_pocitace = vygeneruj_cislo(DELKA)
    print(vyber_pocitace)

    pokusy: int = 0
    bull: int = 0
    cow: int = 0
    while bull < DELKA:
        pokusy += 1
        vyber = pokus_uzivatele(DELKA)
        bull, cow = vyhodnot_pokus(vyber_pocitace, vyber)

        if bull < DELKA:    
            print(f"{bull} bull{'' if bull == 1 else 's'}, {cow} cow{'' if cow == 1 else 's'}")
            print("-----------------------------------------------")
        else: 
            print(f"Correct, you've guessed the right number\nin {pokusy} guesses!")
            print("-----------------------------------------------")
            print("That's amazing!")
    
     
if __name__ == "__main__":
    main()  
    
          
