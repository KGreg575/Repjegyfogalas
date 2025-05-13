import os

from rendszer import FoglalasiRendszer

def main():
    rendszer = FoglalasiRendszer()
    while True:
        print("\n--- Repülőjegy Foglalási Rendszer ---")
        print("1. Jegy foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Járatok listázása")
        print("0. Kilépés")
        valasz = input("Választás: ")

        if valasz == "1":
            nev = input("Utas neve: ")
            jaratszam = input("Járatszám: ")
            print(rendszer.jegy_foglalasa(nev, jaratszam))
        elif valasz == "2":
            nev = input("Utas neve: ")
            jaratszam = input("Járatszám: ")
            print(rendszer.foglalas_lemondasa(nev, jaratszam))
        elif valasz == "3":
            print("\nAktuális foglalások:")
            print(rendszer.foglalasok_listazasa())
        elif valasz == "4":
            print("\nElérhető járatok:")
            print(rendszer.jaratok_listazasa())
        elif valasz == "0":
            os.system("start https://www.youtube.com/watch?v=Gkd5TWMaZRI")
            print("Kilépés... Többet ne jöjjön!")
            break
        else:
            print("Hibás választás, próbáld újra!")

if __name__ == "__main__":
    main()
