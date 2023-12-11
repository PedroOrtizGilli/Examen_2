import pygame
from imagenes import *

class Recolectables:
    def __init__(self, animaciones, x, y, nombre, ancho, alto):
        self.animaciones = animaciones
        reescalar_disparos(self.animaciones, ancho, alto)
        self.rectangulo = self.animaciones[0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.nombre = nombre
        self.vida = 0
        self.contador_pasos = 0
        if self.nombre == "moneda":
            self.valor = 100
        elif self.nombre == "medalla":
            self.valor = 500
        elif self.nombre == 'vida':
            self.valor = 0
            self.vida = 1

    def animar(self, pantalla):
        largo = len(self.animaciones)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animaciones[self.contador_pasos], self.rectangulo)
        self.contador_pasos += 1