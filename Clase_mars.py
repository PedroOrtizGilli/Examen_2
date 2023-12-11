import pygame, math
from imagenes import *
from Clase_disparo import Disparo


class MarsPeople:
    def __init__(self, animaciones, ancho, alto, pos_x, pos_y, velocidad, nombre):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, ancho, alto)
        self.rectangulo = self.animaciones['idle_izquierda'][0].get_rect()
        self.rectangulo.x = pos_x
        self.rectangulo.y = pos_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones['idle_izquierda']
        self.lista_proyectiles = []
        self.ultima_accion = 'izquierda'
        self.dispara = False
        self.vida = 1
        self.valor = 200
        self.tiempo_ultimo_disparo_iz = 0
        self.tiempo_ultimo_disparo_dr = 0
        self.esta_muerto = False
        self.esta_muriendo = False
        self.nombre = nombre

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
            self.ultima_accion = 'derecha'
        else:
            self.animacion_actual = self.animaciones['caminar_izquierda']
            self.ultima_accion = 'izquierda'

    def animar(self, pantalla):
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

    def actualizar(self, pantalla, controles, lista_disparos):
        if not self.esta_muerto:
            self.animar(pantalla)
            self.avanzar(controles)
            self.actualizar_proyectiles(pantalla)
            self.atacar()
            self.verificar_colision_disaros(pantalla, lista_disparos)

    def verificar_colision_disaros(self, pantalla, lista_disparos):
        if not self.esta_muriendo:
            for disparo in lista_disparos:
                if self.rectangulo.colliderect(disparo.rectangulo):
                    self.vida -= 1
                    if self.vida == 0:
                        self.animacion_actual = self.animaciones['muerte_izquierda']
                        self.velocidad = 0
                        lista_disparos.remove(disparo)
                        self.animar(pantalla)
                        self.esta_muriendo = True

    def atacar(self):
        x = None
        margen = 47
        y = self.rectangulo.centery
        if self.ultima_accion == 'izquierda':
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_disparo_iz >= 2000:
                self.animacion_actual = self.animaciones['disparo_izquierda']
                x = self.rectangulo.left - 100 + margen
                if x is not None:
                    self.lista_proyectiles.append(Disparo(mars_bullet_left, x, y, self.ultima_accion, 100, 100))
                    self.tiempo_ultimo_disparo_iz = tiempo_actual
        else:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_ultimo_disparo_dr >= 2000:
                self.animacion_actual = self.animaciones['disparo_derecha']
                x = self.rectangulo.right - margen
                if x is not None:
                    self.lista_proyectiles.append(Disparo(mars_bullet_righ, x, y, self.ultima_accion, 100, 100))
                    self.tiempo_ultimo_disparo_dr = tiempo_actual

    def actualizar_proyectiles(self, pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            pantalla.blit(p.animacion_actual, p.rectangulo)
            p.actualizar()
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1
            i += 1
