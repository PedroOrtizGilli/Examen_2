import pygame, time
from imagenes import *
from Clase_disparo import Disparo

class Boss:
    def __init__(self, animaciones, x, y, ancho, alto, velocidad) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, ancho, alto)
        self.rectangulo = animaciones['idle_left'][0].get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones['idle_left']
        self.bandera_ataque = False
        self.tiempo_ultimo_disparo = 0
        self.ataque_uno = True
        self.ataque_dos = False
        self.contador_disparos = 0
        self.tiempo_entre_ataques = 0

        self.lista_proyectiles = []
        self.vida = 5
        self.valor = 1000

        self.esta_muriendo = False
        self.esta_muerto = False

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

    def caminar(self):
        velocidad_actual = self.velocidad
        if not self.esta_muriendo:
            if self.animacion_actual == self.animaciones['idle_right']:
                velocidad_actual *= -1
            self.rectangulo.x += velocidad_actual

    def ataque(self, pantalla, ayudas):
        x = None
        margen = 47
        y = self.rectangulo.centery + 55
        tiempo_actual = pygame.time.get_ticks()
        print(self.contador_disparos)

        if self.ataque_uno:
            if self.animacion_actual == self.animaciones['idle_left']:
                self.caminar()
                if self.rectangulo.x <= pantalla.get_width() - pantalla.get_width():
                    self.animacion_actual = self.animaciones['idle_right']
                    self.ataque_uno = False
                    self.ataque_dos = True
                    self.tiempo_entre_ataques = tiempo_actual
            elif self.animacion_actual == self.animaciones['idle_right']:
                self.caminar()
                for ayuda in ayudas:
                    if self.rectangulo.colliderect(ayuda.rectangulo):
                        self.animacion_actual = self.animaciones['idle_left']
                        self.ataque_uno = False
                        self.ataque_dos = True
                        self.tiempo_entre_ataques = tiempo_actual

        elif self.ataque_dos:
            if tiempo_actual - self.tiempo_ultimo_disparo >= 350:
                if self.animacion_actual == self.animaciones['idle_left']:
                    if self.contador_pasos == len(self.animacion_actual):
                        x = self.rectangulo.left - margen
                        if x is not None:
                            self.lista_proyectiles.append(Disparo(boss_shoot_bajo_left, 
                                                                x, 
                                                                y, 
                                                                'izquierda', 
                                                                100, 100))
                            self.tiempo_ultimo_disparo = tiempo_actual
                            self.contador_disparos += 1
                            self.tiempo_inicial = time.time()
                elif self.animacion_actual == self.animaciones['idle_right']:
                    if self.contador_pasos == len(self.animacion_actual):
                        x = self.rectangulo.left + 320 - margen
                        if x is not None:
                            self.lista_proyectiles.append(Disparo(boss_shoot_bajo_right, 
                                                                x, 
                                                                y, 
                                                                'derecha', 
                                                                100, 100))
                            self.tiempo_ultimo_disparo = tiempo_actual
                            self.contador_disparos += 1
                            self.tiempo_inicial = time.time()

        if self.contador_disparos == 5:
            self.ataque_dos = False
            self.tiempo_entre_ataques = tiempo_actual
            if time.time() - self.tiempo_inicial >= 3.5:
                self.contador_disparos = 0
                self.ataque_uno = True

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

    def verificar_colision_disaros(self, pantalla, lista_disparos):
        if not self.esta_muriendo:
            for disparo in lista_disparos:
                if self.rectangulo.colliderect(disparo.rectangulo):
                    self.vida -= 1
                    lista_disparos.remove(disparo)
                    if self.vida == 0:
                        self.esta_muriendo = True
                    if self.esta_muriendo:
                        self.animacion_actual = self.animaciones['muerte_left']
                        self.animar(pantalla)
                        self.esta_muerto = True

    def actualizar(self, pantalla, ayudas, lista_disparos):
        if not self.esta_muerto:
            self.animar(pantalla)
            self.actualizar_proyectiles(pantalla)
            self.ataque(pantalla, ayudas)
            self.verificar_colision_disaros(pantalla, lista_disparos)
