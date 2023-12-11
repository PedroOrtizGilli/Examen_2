import pygame
from modo import *
from logica_2 import *

class Niveles:
    def __init__(self, pantalla, arabian, lista_plataformas, img_fondo, lista_enemigos, 
                 lista_ayudas, lista_recolectables, trampa, hay_trampa) -> None:
        self._slave = pantalla
        self.arabian = arabian
        self.plataformas = lista_plataformas
        self.img_fondo = img_fondo
        self.ultima_accion = 'derecha'
        self.enemigos = lista_enemigos
        self.ayuda = lista_ayudas
        self.recolectables = lista_recolectables
        self.tiempo_ultimo_disparo = 0
        self.menu_pausa = False
        self.pos_personaje = None
        self.estado_personaje = None
        self.pos_enemigos = None
        self.puntaje = 0
        self.hay_trampa = hay_trampa
        if self.hay_trampa:
            self.trampa = trampa
        self.final = False
        self.volver_menu = False

    def devolver_puntaje(self):
        return int(self.puntaje)

    def update(self, lista_eventos, estado_juego):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
        if not self.menu_pausa:
            self.actualizar_pantalla()
            estado_juego = self.leer_inputs(estado_juego)
        else:
            estado_juego = self.leer_inputs(estado_juego)
        return estado_juego

    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo, (0,0))

        if self.hay_trampa:
            for t in self.trampa:
                t.animar(self._slave, self.arabian.lista_proyectiles)
                t.verificar_colision_jugador(self.arabian)
                if t.esta_muerto:
                    del t

        for plataforma in self.plataformas:
            plataforma.draw(self._slave)
            self.arabian.actualizar(self._slave, self.plataformas)

        for reco in self.recolectables:
            reco.animar(self._slave)

        for ayudas in self.ayuda:
            ayudas.draw(self._slave)

        for enemigo in self.enemigos:
            enemigo.actualizar(self._slave, self.ayuda, self.arabian.lista_proyectiles)
            self.arabian.verificar_colision_disaros(enemigo.lista_proyectiles)
            if enemigo.esta_muerto:
                self.arabian.puntaje += enemigo.valor
                self.enemigos.remove(enemigo)
                del enemigo
                print(self.enemigos)

        if not self.enemigos_muertos() and not self.final:
            self.arabian.verificar_colision_objetos(self.recolectables)
            self.arabian.verificar_colision_enemigo(self.enemigos, self.ultima_accion)
            self.arabian.verificar_vidas(self._slave, self.ultima_accion)
            if self.hay_trampa:
                self.arabian.verificar_colision_trampa(self.trampa)
            if self.arabian.esta_muerto:
                self.arabian.remove(self.arabian)

            self.arabian.mostrar_vidas(self._slave)
            self.puntaje = mostrar_puntaje(PANTALLA, str(self.arabian.puntaje).zfill(7), times, 70, "Black", 200, 40)

    def leer_inputs(self, estado_juego):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            self.menu_pausa = True
            menu_pausado.draw(PANTALLA)
            continuar.draw(PANTALLA)
            volumen.draw(PANTALLA)
            on.draw(PANTALLA)
            off.draw(PANTALLA)
            menu.draw(PANTALLA)
        if on.click():
            pygame.mixer.Channel.set_volume(pygame.mixer.music.get_volume() + 0.01)
        if off.click():
            pygame.mixer.music.set_volume(0.0)
        if menu.click():
            self.volver_menu = True
            self.menu_pausa = False
            self.arabian.rectangulo_principal.topleft = self.pos_personaje
            self.arabian.accion = self.estado_personaje

            for i, enemigo in enumerate(self.enemigos):
                enemigo.rectangulo.topleft = self.pos_enemigos[i]
        if continuar.click() or keys[pygame.K_ESCAPE]:
            print("llegue")
            self.menu_pausa = False
            self.arabian.rectangulo_principal.topleft = self.pos_personaje
            self.arabian.accion = self.estado_personaje

            for i, enemigo in enumerate(self.enemigos):
                enemigo.rectangulo.topleft = self.pos_enemigos[i]

        if not self.menu_pausa:

            self.pos_personaje = self.arabian.rectangulo_principal.topleft
            self.estado_personaje = self.arabian.accion
            self.pos_enemigos = [(enemigo.rectangulo.topleft) for enemigo in self.enemigos]

            if keys[pygame.K_TAB]:
                    cambiar_modo()

            elif keys[pygame.K_RIGHT]:
                self.arabian.accion = "derecha"
                self.ultima_accion = "derecha"
                self.arabian.sonido_caminar()

            elif keys[pygame.K_LEFT]:
                self.arabian.accion = "izquierda"
                self.ultima_accion = "izquierda"
                self.arabian.sonido_caminar()

            elif keys[pygame.K_UP]:
                if self.ultima_accion == "derecha":
                    self.arabian.accion = "salto_derecha"
                else:
                    self.arabian.accion = "salto_izquierda"

            elif keys[pygame.K_j]:
                print("j")
                if self.ultima_accion == "derecha":
                    tiempo_actual = pygame.time.get_ticks()
                    print(f"{tiempo_actual}")
                    if tiempo_actual - self.tiempo_ultimo_disparo >= 500:
                        print(f"{tiempo_actual}, {tiempo_ultimo_disparo}")
                        self.arabian.disparar(self.ultima_accion)
                        self.tiempo_ultimo_disparo = tiempo_actual
                else: 
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - self.tiempo_ultimo_disparo >= 500:
                        print(f"{tiempo_actual}, {tiempo_ultimo_disparo}")
                        self.arabian.disparar(self.ultima_accion)
                        self.tiempo_ultimo_disparo = tiempo_actual

            elif not any(keys):
                if self.ultima_accion == "derecha":
                    self.arabian.accion = "idle_right"
                else:
                    self.arabian.accion = "idle_left"

            if get_mode():
                pygame.draw.rect(self._slave, "Blue", self.arabian.rectangulo_principal, 3)
                for pl in self.plataformas:
                    pygame.draw.rect(self._slave, "Red", pl.rectangulo, 3)
                for e in self.enemigos:
                    pygame.draw.rect(self._slave, "Green", e.rectangulo, 3)
                for r in self.recolectables:
                    pygame.draw.rect(self._slave, "Orange", r.rectangulo, 3)
                for a in self.ayuda:
                    pygame.draw.rect(self._slave, "Yellow", a.rectangulo, 3)
                if self.hay_trampa:
                    for tr in self.trampa:
                        pygame.draw.rect(self._slave, "Grey", tr.rectangulo, 3)
        return estado_juego

    def enemigos_muertos(self):
        return all(enemigo.esta_muerto for enemigo in self.enemigos)
