import pygame
from imagenes import *
from Clase_disparo import Disparo

class Arabian:
    def __init__(self, animaciones, tamaño, pos_x, pos_y, velocidad, caminar):
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        self.rectangulo_principal = animaciones['idle_right'][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocidad = velocidad
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones['idle_right']
        self.accion = 'idle_right'
        self.vida = 5
        self.delay_vida = False
        self.contador_vidas = 0
        self.puntaje = 0
        self.lista_proyectiles = []

        self.desplazamiento_y = 0 
        self.potencia_salto = -20 
        self.limite_velocidad_salto = 25 
        self.esta_saltando = False
        self.gravedad = 1

        self.sonido_caminata = pygame.mixer.Sound(caminar)
        self.sonido_moneda = pygame.mixer.Sound(r"Soundboard\Moneda.wav")
        self.sonido_moneda.set_volume(1)
        # self.sonido_caminata.set_volume(0.15)

        self.esta_muriendo = False
        self.esta_muerto = False
        # self.murio = False

    def sonido_caminar(self):
        self.sonido_caminata.play()

    def aplicar_gravedad(self, pantalla, plataformas):
        if self.esta_muriendo:
            return 

        if self.esta_saltando:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad

        for pl in plataformas:
            if self.rectangulo_principal.colliderect(pl.rectangulo):
                if self.desplazamiento_y > 0: 
                    self.esta_saltando = False
                    self.desplazamiento_y = 0
                    self.rectangulo_principal.bottom = pl.rectangulo.top
                break
            else:
                self.esta_saltando = True

    def caminar(self, pantalla):
        velocidad_actual = self.velocidad
        if not self.esta_muriendo:
            if self.accion == 'izquierda':
                velocidad_actual *= -1
            nueva_posicion = self.rectangulo_principal.x + velocidad_actual
            if nueva_posicion > 0 and nueva_posicion <= (pantalla.get_width() - self.rectangulo_principal.width):
                self.rectangulo_principal.x += velocidad_actual

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
        if not self.esta_muriendo:
            self.contador_pasos += 1
        if self.esta_muriendo:
            self.contador_pasos += 1
            if self.contador_pasos >= largo:
                self.contador_pasos = len(self.animacion_actual)
                self.esta_muriendo = False
                self.esta_muerto = True

    def actualizar(self, pantalla, plataformas):
        match self.accion:
            case "derecha":
                if not self.esta_muriendo:
                    if not self.esta_saltando:
                        self.animacion_actual = self.animaciones['derecha']
                        self.animar(pantalla)
                    self.caminar(pantalla)
            case "izquierda":
                if not self.esta_muriendo:
                    if not self.esta_saltando:
                        self.animacion_actual = self.animaciones['izquierda']
                        self.animar(pantalla)
                    self.caminar(pantalla)
            case "idle_right":
                if not self.esta_muriendo:
                    if not self.esta_saltando:
                        self.animacion_actual = self.animaciones['idle_right']
                        self.animar(pantalla)
                        self.sonido_caminata.stop()
            case "idle_left":
                if not self.esta_muriendo:
                    if not self.esta_saltando:
                        self.animacion_actual = self.animaciones['idle_left']
                        self.animar(pantalla)
                        self.sonido_caminata.stop()
            case "salto_derecha":
                if not self.esta_muriendo:
                        self.animacion_actual = self.animaciones['salto_derecha']
                        self.animar(pantalla)
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
                        self.sonido_caminata.stop()
            case "salto_izquierda":
                if not self.esta_muriendo:
                        self.animacion_actual = self.animaciones['salto_izquierda']
                        self.animar(pantalla)
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto
                        self.sonido_caminata.stop()

        self.actualizar_proyectiles(pantalla)
        self.aplicar_gravedad(pantalla, plataformas)

    def mostrar_vidas(self, pantalla):
        x = 950
        y = 25
        for i in range(self.vida):
            pantalla.blit(arabian_vidas[i], (x, y))
            x += 35

    def verificar_vidas(self, pantalla, ultima_accion):
        if self.vida == 0:
            self.esta_muriendo = True
            self.velocidad = 0
            if ultima_accion == 'izquierda':
                self.animacion_actual = self.animaciones['muerte_izquierda']
            else:
                self.animacion_actual = self.animaciones['muerte_derecha']
            self.animar(pantalla)

    def verificar_colision_enemigo(self, lista_enemigos, ultima_accion):
        if not self.esta_muriendo:
            for enemigo in lista_enemigos:
                if self.rectangulo_principal.colliderect(enemigo.rectangulo):
                    if self.delay_vida == False:
                        self.vida -= 1
                        self.puntaje -= 50
                        self.delay_vida = True
                    if ultima_accion == 'derecha':
                        self.animacion_actual = self.animaciones['knok_izquierda']
                        if self.contador_pasos < len(self.animacion_actual):
                            self.rectangulo_principal.x -= 200
                            self.delay_vida = False
                    else:
                        self.animacion_actual = self.animaciones['knok_derecha']
                        if self.contador_pasos < len(self.animacion_actual):
                            self.rectangulo_principal.x += 200
                            self.delay_vida = False

    def verificar_colision_objetos(self, lista_recolectables):
        for r in lista_recolectables:
            if self.rectangulo_principal.colliderect(r.rectangulo):
                self.sonido_moneda.play()
                self.puntaje += r.valor
                lista_recolectables.remove(r)
                if r.nombre == "vida":
                    if self.vida < 5:
                        self.vida += 1

    def verificar_colision_disaros(self, lista_disparos):
        if not self.esta_muriendo:
            for disparo in lista_disparos:
                if self.rectangulo_principal.colliderect(disparo.rectangulo):
                    self.vida -= 1
                    self.puntaje -= 50
                    lista_disparos.remove(disparo)

    def verificar_colision_trampa(self, trampa):
        for tr in trampa:
            if self.rectangulo_principal.colliderect(tr.rectangulo):
                self.vida -= 3
                trampa.remove(tr)

    def disparar(self, ultima_accion):
        x = None
        margen = 47
        y = self.rectangulo_principal.centery - 15
        if not self.esta_saltando:
            if ultima_accion == "derecha":
                self.animacion_actual = self.animaciones['distancia_derecha']
                if self.contador_pasos <= len(self.animacion_actual):
                    x = self.rectangulo_principal.right - margen
                    print("dispara")
                if x is not None:
                    self.lista_proyectiles.append(Disparo(arabian_espada_derecha, x, y, ultima_accion, 100, 100))
                    print("disparo")

            elif ultima_accion == "izquierda":
                self.animacion_actual = self.animaciones['distancia_izqueirda']
                if self.contador_pasos <= len(self.animacion_actual):
                    x = self.rectangulo_principal.left - 100 + margen
                    print("dispara")
                if x is not None:
                    self.lista_proyectiles.append(Disparo(arabian_espada_izquierda, x, y, ultima_accion, 100, 100))
                    print("disparo")

    def actualizar_proyectiles(self, pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            p = self.lista_proyectiles[i]
            pantalla.blit(p.animacion_actual, p.rectangulo)
            p.actualizar()
            print("actualizo")
            if p.rectangulo.centerx < 0 or p.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i -= 1
            i += 1
