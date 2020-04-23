
class Tamagotchi:
    prog_nudy = 5 # atrybut klasy
    prog_glodu = 10 # atrybut klasy
    def __init__(self, imie #Argumenty metod klasy): #Metody klasy oraz Konstruktor
        self.imie = imie
        self.slowa = ["Mmmmrrp", "Hrrp"]
        self.poziom_nudy = 0
burek = Tamagotchi("Burek") #Wszystkie instancje klasy