import pygame
from Clase_niveles import Niveles
from Clase_Personaje_principal import Arabian
from Clase_recolectables import Recolectables
from Clase_plataformas import Plataforma
from Clase_final_boss import Boss
from imagenes import *
from logica_2 import *
from Clase_trampa import Trampa

class NivelFinal(Niveles):
    def __init__(self, pantalla: pygame.Surface):

        W = pantalla.get_width()
        H = pantalla.get_height()

        fondo_nivel_final = pygame.image.load(r"Nivel_final\Nivel_final.png")
        fondo_nivel_final = pygame.transform.scale(fondo_nivel_final, (2000, ALTO))

        arabian_nivel_final = Arabian(arabian_diccionario, (150, 170), 50, 577, 10, r"Soundboard\Caminar_desierto.wav")

        piso_nivel_final = Plataforma(2000, 20, 0, 750, False,"")
        piso_nivel_final.top = arabian_nivel_final.rectangulo_principal.bottom
        estructura = Plataforma(655, 202, 602, 558, False, '')
        estructura_2 = Plataforma(230, 20, 1056, 400, False, '')

        plataformas_nivel_final = [piso_nivel_final, estructura, estructura_2]

        boss = Boss(boss_diccionario, 1500, 600, 370, 250, -35)
        boss.rectangulo.bottom = piso_nivel_final.rectangulo.top

        lista_boss = [boss]

        ayuda = Plataforma(50, 50, 1900, 700, False, '')
        lista_ayudas_final = [ayuda]

        lista_recolectables_final = []

        super().__init__(pantalla, arabian_nivel_final, plataformas_nivel_final, fondo_nivel_final, lista_boss,
                         lista_ayudas_final, lista_recolectables_final, "", False)