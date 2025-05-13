from Repulojegy.jarat import BelfoldiJarat, NemzetkoziJarat
from Repulojegy.legitarsasag import LegiTarsasag
from Repulojegy.jegyfoglalas import JegyFoglalas

class FoglalasiRendszer:
    def __init__(self):
        self.legi_tarsasag = LegiTarsasag("WizzAir")
        self.foglalasok = []
        self._elore_toltes()

    def _elore_toltes(self):
        j1 = BelfoldiJarat("B01", "Debrecen")
        j2 = NemzetkoziJarat("N01", "London")
        j3 = NemzetkoziJarat("N02", "Berlin")
        self.legi_tarsasag.jarat_hozzaadas(j1)
        self.legi_tarsasag.jarat_hozzaadas(j2)
        self.legi_tarsasag.jarat_hozzaadas(j3)

        self.foglalasok.append(JegyFoglalas("Kovács Péter", j1))
        self.foglalasok.append(JegyFoglalas("Szabó Anna", j2))
        self.foglalasok.append(JegyFoglalas("Péter Árpád", j2))
        self.foglalasok.append(JegyFoglalas("Galambos Tibor", j3))
        self.foglalasok.append(JegyFoglalas("Fülpesi László", j1))
        self.foglalasok.append(JegyFoglalas("Dávid Zsófia", j3))

    def jegy_foglalasa(self, utas_nev, jaratszam):
        jarat = self.legi_tarsasag.jarat_kereses(jaratszam)
        if not jarat:
            return "Hiba: Nincs ilyen járatszám."
        self.foglalasok.append(JegyFoglalas(utas_nev, jarat))
        return f"Sikeres foglalás. Ár: {jarat.jegyar} Ft"

    def foglalas_lemondasa(self, utas_nev, jaratszam):
        for f in self.foglalasok:
            if f.utas_nev == utas_nev and f.jarat.jaratszam == jaratszam:
                self.foglalasok.remove(f)
                return "Foglalás sikeresen lemondva."
        return "Hiba: A megadott foglalás nem található."

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Nincsenek foglalások."
        return "\n".join([f.info() for f in self.foglalasok])

    def jaratok_listazasa(self):
        return "\n".join([j.info() for j in self.legi_tarsasag.jaratok])
