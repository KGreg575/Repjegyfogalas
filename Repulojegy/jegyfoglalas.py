class JegyFoglalas:
    def __init__(self, utas_nev, jarat):
        self.utas_nev = utas_nev
        self.jarat = jarat

    def info(self):
        return f"{self.utas_nev} - {self.jarat.jaratszam} ({self.jarat.celallomas})"
