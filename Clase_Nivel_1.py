import pygame, random
from Clase_Personaje_principal import Arabian
from Clase_momia import Momia
from Clase_recolectables import Recolectables
from Clase_niveles import Niveles
from Clase_plataformas import Plataforma
from imagenes import *
from Clase_trampa import Trampa
from logica_2 import *

class NivelUno(Niveles):
    def __init__(self, pantalla: pygame.Surface):

        self.W = pantalla.get_width()
        self.H = pantalla.get_height()

        self.fondo_nivel_1 = pygame.image.load(r"Nivel_1\Fondo.png")
        self.fondo_nivel_1 = pygame.transform.scale(self.fondo_nivel_1, (5000, self.H)) 

        self.arabian_nivel_1 = Arabian(arabian_diccionario, (150, 170), 50, 600, 10, r"Soundboard\Caminar_desierto.wav")

        self.piso_nivel_1 = Plataforma(5000, 20, 0, 800, False,'')
        self.piso_nivel_1.top = self.arabian_nivel_1.rectangulo_principal.bottom
        self.plataforma_1 = Plataforma(500, 50, 100, 550, True, r"Plataforma\12.png")
        self.plataforma_2 = Plataforma(500, 50, 1350, 550, True, r"Plataforma\12.png")
        self.plataforma_3 = Plataforma(500, 50, 675, 300, True, r"Plataforma\12.png")

        self.plataformas_nivel_1 = [self.piso_nivel_1, self.plataforma_1, self.plataforma_2, self.plataforma_3]

        self.momia = Momia(momia_diccionario, 160, 170, 450, 600, 5, False, 'momia')
        self.momia.rectangulo.bottom = self.plataforma_1.rectangulo.top

        self.momia_2 = Momia(momia_diccionario, 160, 170, 1400, 600, 5, False, 'momia')
        self.momia_2.rectangulo.bottom = self.plataforma_2.rectangulo.top

        self.momia_trampa_1 = Momia(momia_diccionario, 160, 170, 1600, 600, 5, True, 'momia')
        self.momia_trampa_1.rectangulo.bottom = self.piso_nivel_1.rectangulo.top

        self.lista_enemigos_lv1 = [self.momia, self.momia_trampa_1, self.momia_2]
        self.enemigos = self.lista_enemigos_lv1.copy()

        self.left_plat_1 = Plataforma(50, 50, 40, 500, False, '')
        self.right_plat_1 = Plataforma(50, 50, 650, 500, False, '')
        self.trampa_1 = Plataforma(50, 50, 500, 750, False, '')
        self.trampa_2 = Plataforma(50, 50, self.W, 750, False, '')
        self.left_plat_2 = Plataforma(50, 50, 1300, 500, False, '')
        self.right_plat_2 = Plataforma(50, 50, 1925, 500, False, '')

        self.ayudas_lv1 = [self.left_plat_1, self.right_plat_1, self.trampa_1, self.trampa_2, 
                      self.left_plat_2, self.right_plat_2]

        self.moneda_1 = Recolectables(monedas, 500, 500, "moneda", 50, 50)
        self.moneda_2 = Recolectables(monedas, 700, 750, "moneda", 50, 50)
        self.moneda_3 = Recolectables(monedas, 300, 300, "moneda", 50, 50)
        self.moneda_4 = Recolectables(monedas, 1000, 600, "moneda", 50, 50)
        self.medalla_lv1 = Recolectables(medallas, random.randint(0, 1800), 730, "medalla", 70, 70)
        self.vida = Recolectables(vidas, 1400, 395, 'vida', 60, 35)

        self.lista_recolectables_lv1 = [self.moneda_1, self.moneda_2, self.moneda_3, 
                                        self.moneda_4, self.vida, self.medalla_lv1]
        self.recolectables = self.lista_recolectables_lv1.copy()

        self.barril_explosivo_lv1 = Trampa(barril_diccionario, 1000, 610, 100, 170)
        self.lista_trampas_lv1 = [self.barril_explosivo_lv1]
        self.trampa = self.lista_trampas_lv1.copy()

        super().__init__(pantalla, self.arabian_nivel_1, self.plataformas_nivel_1, self.fondo_nivel_1, 
                         self.enemigos, self.ayudas_lv1, self.recolectables, self.trampa, True)

    def reinicio(self, objetos:list, objetos_copia:list):
        if len(objetos_copia) < len(objetos):
            for objeto in objetos:
                if objeto not in objetos_copia:
                    objetos_copia.append(objeto)
        return objetos_copia