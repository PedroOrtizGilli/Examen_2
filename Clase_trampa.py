import pygame
from imagenes import *

class Trampa:
    def __init__(self, animaciones, pos_x, pos_y, ancho, alto) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, ancho, alto)
        self.rectangulo = self.animaciones['barril'][0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.animacion_actual = self.animaciones['barril']
        self.vida = 2
        self.contador_pasos = 0
        self.esta_muerto = False

    def verificar_colision_disparos(self, lista_disparos):
        for disparo in lista_disparos:
            if self.rectangulo.colliderect(disparo.rectangulo):
                self.contador_pasos += 1
                self.vida -= 1
                lista_disparos.remove(disparo)
    
    def verificar_colision_jugador(self, jugador):
        if self.rectangulo.colliderect(jugador.rectangulo_principal):
            self.vida = 0

    def animar(self, pantalla, lista_disparos):
        largo = len(self.animacion_actual)
        if not self.esta_muerto:
            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
            if self.verificar_colision_disparos(lista_disparos):
                self.contador_pasos += 1
            if self.vida == 0:
                self.animacion_actual = self.animaciones['explosion']
                self.contador_pasos += 1
                if self.contador_pasos == largo:
                    self.esta_muerto = True
    