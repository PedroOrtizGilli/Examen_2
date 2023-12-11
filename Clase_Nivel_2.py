import pygame
from Clase_niveles import Niveles
from Clase_Personaje_principal import Arabian
from Clase_recolectables import Recolectables
from Clase_plataformas import Plataforma
from Clase_mars import MarsPeople
from imagenes import *
from logica_2 import *
from Clase_trampa import Trampa

class NivelDos(Niveles):
    def __init__(self, pantalla: pygame.Surface):

        W = pantalla.get_width()
        H = pantalla.get_height()

        fondo_nivel_2 = pygame.image.load(r"Nivel_2\nivel 2.png")
        fondo_nivel_2 = pygame.transform.scale(fondo_nivel_2, (2000, H))

        arabian_nivel_2 = Arabian(arabian_diccionario, (150, 170), 50, 600, 10, r"Soundboard\Caminar_desierto.wav")

        piso_nivel_2 = Plataforma(2000, 20, 0, 780, False, "")
        plat_2 = Plataforma(500, 50, 100, 500, True, r"Plataforma\12.png")
        plat_3 = Plataforma(500, 50, 1300, 500, True, r"Plataforma\12.png")
        plat_4 = Plataforma(500, 50, 675, 250, True, r"Plataforma\12.png")

        plataformas_nivel_2 = [piso_nivel_2, plat_2, plat_3, plat_4]

        mars_1 = MarsPeople(mars_people_diccionario, 150, 170, 1000, 500, 5, 'mars')
        mars_1.rectangulo.bottom = piso_nivel_2.rectangulo.top
        mars_2 = MarsPeople(mars_people_diccionario, 150, 170, 1400, 500, 5, 'mars')
        mars_2.rectangulo.bottom = plat_2.rectangulo.top

        lista_enemigos_lv2 = [mars_1, mars_2]

        ayuda_1 = Plataforma(50, 50, 500, 700, False, '')
        ayuda_2 = Plataforma(50, 50, ANCHO, 750, False, '')

        ayudas_lv2 = [ayuda_1, ayuda_2]

        moneda_12 = Recolectables(monedas, random.randint(0, 1800), 450, "moneda", 50, 50)
        moneda_22 = Recolectables(monedas, random.randint(0, 1800), 700, "moneda", 50, 50)
        moneda_32 = Recolectables(monedas, random.randint(0, 1800), 300, "moneda", 50, 50)
        moneda_42 = Recolectables(monedas, random.randint(0, 1800), 600, "moneda", 50, 50)
        medalla_lv2 = Recolectables(medallas, random.randint(0, 1800), 710, "medalla", 70, 70)
        vida2 = Recolectables(vidas, random.randint(0, 1800), 395, 'vida', 60, 35)

        lista_recolectables_lv2 = [moneda_12, moneda_22, moneda_32, moneda_42, vida2, medalla_lv2]

        barril_explosivo_lv2 = Trampa(barril_diccionario, 1000, 560, 20, 20)
        lista_trampas_lv2 = [barril_explosivo_lv2]

        super().__init__(pantalla, arabian_nivel_2, plataformas_nivel_2, fondo_nivel_2, lista_enemigos_lv2, 
                         ayudas_lv2, lista_recolectables_lv2, lista_trampas_lv2, True)