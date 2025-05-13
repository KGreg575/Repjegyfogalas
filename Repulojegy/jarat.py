class Jarat:
    def __init__(self, jaratszam, celallomas, jegyar):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    def info(self):
        raise NotImplementedError("Ezt a függvényt a gyerekosztályban kell megvalósítani.")

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, jegyar=35999)

    def info(self):
        return f"Belföldi Járat - {self.jaratszam}: {self.celallomas}, Ár: {self.jegyar} Ft"

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas):
        super().__init__(jaratszam, celallomas, jegyar=89599)

    def info(self):
        return f"Nemzetközi Járat - {self.jaratszam}: {self.celallomas}, Ár: {self.jegyar} Ft"
