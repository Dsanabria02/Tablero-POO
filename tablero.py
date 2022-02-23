from Ficha import *
from random import*

class Tablero:
    color=""
    numeroDeCasillas=0
    tamanno=""
    cantidadJugadores=0
    ordenJugadores=0
    listaFichas=["Ficha 1","Ficha 2","Ficha 3","Ficha 4","Ficha 5","Ficha 6"]
    rnd=0

    



    
    def __init__(self,color,numeroDeCasillas,tamanno,cantidadJugadores,ordenJugadores):
        self.color=color
        self.numeroDeCasillas=numeroDeCasillas
        self.tamanno=tamanno
        self.cantidadJugadores=cantidadJugadores
        self.ordenJugadores=ordenJugadores


    

    def siguienteTurno(self):
        self.rnd=randint(0, self.cantidadJugadores)
        print("El siguiente turno es de:  ",self.listaFichas[rnd])
        return""




        
        
