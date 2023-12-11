import pygame
from Clase_niveles import Niveles
from Clase_Personaje_principal import Arabian
from Clase_recolectables import Recolectables
from Clase_plataformas import Plataforma
from Clase_pez import Pez
from imagenes import *
from logica_2 import *
from Clase_trampa import Trampa

class NivelTres(Niveles):
    def __init__(self, pantalla: pygame.Surface):

        W = pantalla.get_width()
        H = pantalla.get_height()

        fondo_nivel_3 = pygame.image.load(r"Nivel_3\Nivel_3.png")
        fondo_nivel_3 = pygame.transform.scale(fondo_nivel_3, (2000, ALTO))

        arabian_nivel_3 = Arabian(arabian_diccionario, (150, 170), 50, 500, 10, r"Soundboard\Caminar_desierto.wav")

        piso_nivel_3 = Plataforma(2000, 20, 0, 700, False, "")
        piso_nivel_3.top = arabian_nivel_3.rectangulo_principal.bottom
        plataf_1 = Plataforma(500, 50, 100, 400, True, r'Plataforma\12.png')
        plataf_2 = Plataforma(500, 50, 1200, 400, True, r'Plataforma\12.png')

        plataformas_nivel_3 = [piso_nivel_3, plataf_1, plataf_2]

        #Ayudas_3
        ayuda_13 = Plataforma(50, 50, 550, 400, False, '')
        ayuda_23 = Plataforma(50, 50, 1200, 400, False, '')
        ayuda_33 = Plataforma(50, 50, 1900, 570, False, '')
        ayuda_43 = Plataforma(50, 50, -50, 570, False, '')
        aydua_53 = Plataforma(50, 50, -50, 190, False, '')
        ayuda_63 = Plataforma(50, 50, 1900, 190, False, '')

        lista_ayduas_3 = [ayuda_13, ayuda_23, ayuda_33, ayuda_43, aydua_53, ayuda_63]

        #Enemigos
        # pez_1 = Pez(pez_diccionario, 1000, 390, 10, 100, 75)
        pez_2 = Pez(pez_diccionario, 1600, 580, 15, 100, 75, 'pez')
        pez_3 = Pez(pez_diccionario, 100, 200, 15, 100, 75, 'pez')

        lista_enemigos_lv3 = [pez_2, pez_3]

        #Recolectables
        moneda_13 = Recolectables(monedas, random.randint(0, 1800), 450, "moneda", 50, 50)
        moneda_23 = Recolectables(monedas, random.randint(0, 1800), 200, "moneda", 50, 50)
        moneda_33 = Recolectables(monedas, random.randint(0, 1800), 300, "moneda", 50, 50)
        moneda_43 = Recolectables(monedas, random.randint(0, 1800), 600, "moneda", 50, 50)
        medalla_lv3 = Recolectables(medallas, random.randint(0, 1800), 630, "medalla", 70, 70)
        vida3 = Recolectables(vidas, random.randint(0, 1800), 395, 'vida', 60, 35)

        lista_recolectables_lv3 = [moneda_13, moneda_23, moneda_33, moneda_43, vida3, medalla_lv3]

        barril_explosivo_lv3 = Trampa(barril_diccionario, 1000, 480, 200, 220)
        lista_trampas_lv3 = [barril_explosivo_lv3]

        super().__init__(pantalla, arabian_nivel_3, plataformas_nivel_3, fondo_nivel_3, lista_enemigos_lv3, 
                         lista_ayduas_3, lista_recolectables_lv3, lista_trampas_lv3, True)