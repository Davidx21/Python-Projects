import random

class Game():
    def __init__(self, listaPalabras):
        self.listaPalabras = listaPalabras
        self.palabra = ""
        self.nueva_palabra() #Llamar al método para iniciar el juego
    
    def nueva_palabra(self):
        nuevaPalabra = random.choice(self.listaPalabras).upper()
        #Para no volver a escoger la misma palabra.
        if nuevaPalabra == self.palabra: 
            #Recursividad = En este caso el método se llama a sí mismo.
            #Asegurarse que hay almenos dos palabras    
            self.nueva_palabra()   
        else:
            self.intentos = 7 #Número de veces que se permite perder
            self.palabra = nuevaPalabra
            self.letras = list(self.palabra) #Lista con las letras correctas
            self.palabraJugador = list("x"*len(self.palabra))#Lista del jugador según avanza
            print("Escribe SALIR para terminar juego.")
            print("Palabra: " + "".join(self.palabraJugador))#Para mostrar el avance de la palabra
            self.set_letra()
    
    def final(self, mensaje):
        print(mensaje)
        self.nueva_palabra()

    def revisar_respuesta(self, letra):
        #Lógica principal del juego
        if letra.upper() in self.letras:
            n = 0
            for x in self.letras:
                if letra.upper() == x:
                    self.palabraJugador[n] = letra.upper()
                n += 1
            print("".join(self.palabraJugador))
            if self.letras == self.palabraJugador:
                self.final("Felicidades, ganó el juego.")
            else:
                self.set_letra()  #Vuelve a solicitar letra
        else:
            self.intentos -= 1
            print("Incorrecto. Intentos: " + str(self.intentos))
            if self.intentos == 0:
                self.final("Game Over, no ganó.")
            self.set_letra()

    def set_letra(self):
        letra = input("Letra: ")
        if len(letra) != 1 or letra.isnumeric():
            if letra.upper() == "SALIR":
                print("Gracias por jugar")
                exit()
            else:
                print("Introduce una letra")
                self.set_letra()
        else:
            self.revisar_respuesta(letra)

#Crear instancia
listaPalabras = ["Pizza","Oro","Julieta","Payaso","Hipopotamo","Zopilote"]
game = Game(listaPalabras) 