import pygame
from imagenes import *

class Pez:
    def __init__(self, animaciones, pos_x, pos_y, velocidad, ancho, alto, nombre):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, ancho, alto)
        self.rectangulo = animaciones['caminar_izquierda'][0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones
        self.valor = 200
        self.vida = 1
        self.esta_muriendo = False
        self.esta_muerto = False
        self.lista_proyectiles = []
        self.nombre = nombre
    
    def animar(self, pantalla):
        try:
            largo = len(self.animacion_actual)
            if self.contador_pasos >= largo:
                self.contador_pasos = 0
            pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo)
            if not self.esta_muriendo:
                self.contador_pasos += 1
            if self.esta_muriendo:
                self.contador_pasos += 1
                if self.contador_pasos >= largo:
                    self.contador_pasos = len(self.animacion_actual)
                    self.esta_muriendo = False
                    self.esta_muerto = True
        except Exception as error:
            print("e")

    def avanzar(self, controles):
        if self.esta_muriendo:
                self.rectangulo.x -= 0
        else:
            self.rectangulo.x -= self.velocidad

        for pl in controles:
            if self.rectangulo.colliderect(pl.rectangulo):
                self.velocidad *= -1

        if self.velocidad < 0:
            self.animacion_actual = self.animaciones['caminar_derecha']
        else:
            self.animacion_actual = self.animaciones['caminar_izquierda']

    def actualizar(self, pantalla, controles, lista_disparos):
        if not self.esta_muerto:
            self.animar(pantalla)
            self.avanzar(controles)
            self.verificar_colision_disaros(pantalla, lista_disparos)
    
    def verificar_colision_disaros(self, pantalla, lista_disparos):
        if not self.esta_muriendo:
            for disparo in lista_disparos:
                if self.rectangulo.colliderect(disparo.rectangulo):
                    self.animacion_actual = self.animaciones['muerte_izquierda']
                    self.velocidad = 0
                    lista_disparos.remove(disparo)
                    self.animar(pantalla)
                    self.esta_muriendo = True