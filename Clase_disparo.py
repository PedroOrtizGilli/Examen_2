import pygame
from imagenes import *

class Disparo:
    def __init__(self, animaciones, x, y, direccion, ancho, alto):
        self.animaciones = animaciones
        reescalar_disparos(self.animaciones, ancho, alto)
        self.rectangulo = animaciones[0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.direccion = direccion
        self.animacion_actual = self.animaciones[0]

    def actualizar(self):
        if self.direccion == "derecha":
            self.rectangulo.x += 20
        elif self.direccion == "izquierda":
            self.rectangulo.x -= 20