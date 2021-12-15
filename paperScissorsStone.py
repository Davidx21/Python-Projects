import random

class Pelea():
    def __init__(self,arma1,arma2):
        self.combinaciones = [["tijera","tijera"],["tijera","piedra"],["tijera","papel"],["papel","papel"],["papel","piedra"],["papel","tijera"],
        ["piedra","tijera"],["piedra","papel"],["piedra","piedra"]]
        self.resultados = ["empate","piedra","tijera","empate","papel","tijera","piedra","papel","empate"]
        self.batalla = [arma1,arma2]
        self.pos = self.combinaciones.index(self.batalla)
        self.resultado = self.resultados[self.pos]
    def get_resultado(self):
        return (self.resultado.capitalize())

class Game():
    def __init__(self):
        print("Jugemos Piedra, Papel y Tijera")
        print("------------------------------")
        print("pi:Piedra pa:Papel ti:Tijera")
        self.objetos = ["piedra","papel","tijera"]
        self.empezar()

    def ganador(self):
        self.computadora = random.choice(self.objetos)
        pelea = Pelea(self.objeto,self.computadora)
        print("Tu: " + self.objeto + " vs " + "Máquina: " + self.computadora)
        if (pelea.get_resultado().lower() == "empate"):
            print("Empate")
        elif (pelea.get_resultado().lower() == self.objeto):
            print("Ganaste")
        else:
            print("Perdiste")

    def empezar(self):
        seleccion = input("Selección: ").lower()
        if seleccion == "pi" or seleccion == "pa" or seleccion == "ti":
            if seleccion == "pi":
                self.objeto = "piedra" 
            elif seleccion == "pa":
                self.objeto = "papel"
            elif seleccion == "ti":
                self.objeto = "tijera"
            self.ganador()
        else:
            print("pi:Piedra pa:Papel ti:Tijera")
            self.empezar() #Recursividad

game = Game()