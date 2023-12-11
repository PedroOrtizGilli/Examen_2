import pygame, sys, random, sqlite3, time
from imagenes import *
from Clase_botones import Boton

pygame.font.init()
nombre_jugador = ''
ANCHO = 1900
ALTO = 900
TAMAÑO_PANTALLA = (ANCHO, ALTO)
FPS = 30
estado_juego = "nombre"
running = True
ultima_accion = "derecha"
flag_disparo = False
tiempo_ultimo_disparo = 0
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
times = pygame.font.match_font("timesnewroman")
puntaje = 0
menu_pausa = False
tiempo_final = 0
lv2_unlock = False
lv3_unlock = False
lv4_unlock = False

bandera_lv1 = False
bandera_lv2 = False
bandera_lv3 = False
bandera_lv4 = False

clock = pygame.time.Clock() 

#Puntaje
def mostrar_puntaje(pantalla, puntaje, fuente, tamaño, color, x, y):
    letra = pygame.font.Font(fuente, tamaño)
    superficie = letra.render(puntaje, True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = x,y
    pantalla.blit(superficie, rectangulo)
    return puntaje

#Botones
nombre = pygame.image.load(r"Botones\68.png")
nombre = pygame.transform.scale(nombre, (800,700))
fondo = pygame.image.load(r"Fondo_inicio\1.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)
fondo_nivel_1 = pygame.image.load(r"Nivel_1\Fondo.png")
fondo_nivel_1 = pygame.transform.scale(fondo_nivel_1, (5000, ALTO))
fondo_nivel_2 = pygame.image.load(r"Nivel_2\nivel 2.png")
fondo_nivel_2 = pygame.transform.scale(fondo_nivel_2, (2000, ALTO))
fondo_nivel_3 = pygame.image.load(r"Nivel_3\Nivel_3.png")
fondo_nivel_3 = pygame.transform.scale(fondo_nivel_3, (2000, ALTO))
fondo_nivel_final = pygame.image.load(r"Nivel_final\Nivel_final.png")
fondo_nivel_final = pygame.transform.scale(fondo_nivel_final, (2000, ALTO))

#Botones_menu
jugar_imagen = pygame.image.load(r"Botones\jugar_boton.png")
salir_imagen = pygame.image.load(r"Botones\salir_boton.png")
marcador_imagen = pygame.image.load(r"Botones\marcador_boton.png")
pausa_imagen = pygame.image.load(r"Botones\58.png")
config_imagen = pygame.image.load(r"Botones\57.png")
jugar = Boton(303, 700, jugar_imagen, 200, 100)
configuracion = Boton(650, 700, config_imagen, 200, 100)
marcador = Boton(1000, 700, marcador_imagen, 200, 100)
salir = Boton(1350, 700, salir_imagen, 200, 100)
pausa = Boton(1800, 20, pausa_imagen, 70, 70)

#Botones_seleccion_nivel
nivel_1_imagen = pygame.image.load(r"Botones\nivel_1_boton.png")
nivel_2_imagen = pygame.image.load(r"Botones\nivel_2_boton.png")
nivel_3_imagen = pygame.image.load(r"Botones\nivel_3_boton.png")
nivel_final_imagen = pygame.image.load(r"Botones\nivel_final_boton.png")
nivel_1 = Boton(200,250, nivel_1_imagen, 200, 100)
nivel_2 = Boton(600,250, nivel_2_imagen, 200, 100)
nivel_3 = Boton(1080,250, nivel_3_imagen, 200, 100)
nivel_final = Boton(1500,250, nivel_final_imagen, 200, 100)
volver = pygame.image.load(r"Botones\volver_boton.png")
volver_boton = Boton(780, 740, volver, 200, 100)

#Botones_pausa
menu_pausado_imagen = pygame.image.load(r"Botones\Pause.png")
continuar_imagen = pygame.image.load(r"Botones\Continuar.png")
volumen_imagen = pygame.image.load(r"Botones\Volumen.png")
on_imagen = pygame.image.load(r"Botones\On.png")
off_imagen = pygame.image.load(r"Botones\Off.png")
menu_imagen = pygame.image.load(r"Botones\51.png")
menu_pausado = Boton(400, 50, menu_pausado_imagen, 1000, 700)
continuar = Boton(790, 650, continuar_imagen, 200, 50)
volumen = Boton(600, 250, volumen_imagen, 200, 50)
on = Boton(900, 250, on_imagen, 100, 50)
off = Boton(1100, 250, off_imagen, 100, 50)
menu = Boton(650, 350, menu_imagen, 200, 50)

stage_clear_imagen = pygame.image.load(r"Extras\Stage_clear.png")
stage_clear_surface = Boton(650, 250, stage_clear_imagen, 700, 350)
game_over_imagen = pygame.image.load(r"Extras\Game_over.png")
game_over_surface = Boton(650, 250, game_over_imagen, 700, 350)

#Canciones
pygame.mixer.pre_init(44100, -16, 2, 9000)
pygame.mixer.init()

arabian_nights = pygame.mixer.Sound(r"Soundboard\Arabian_nights.wav")
desert = pygame.mixer.Sound(r"Soundboard\Desert.wav")
fantasy = pygame.mixer.Sound(r"Soundboard\Fantasy_music.wav")
into_the_cosmos = pygame.mixer.Sound(r"Soundboard\Into_the_cosmos.wav")
regular_show = pygame.mixer.Sound(r"Soundboard\Regular_show.wav")

#Sounds
game_over = pygame.mixer.Sound(r"Soundboard\Game_over.wav")
stage_clear = pygame.mixer.Sound(r"Soundboard\Stage_clear.wav")
sonido_moneda = pygame.mixer.Sound(r"Soundboard\Moneda.wav")
conteo_puntos = pygame.mixer.Sound(r"Soundboard\Conteo_puntos.wav")

#Sprites_Arabian
arabian_diccionario = {}
arabian_diccionario['idle_right'] = arabian_idle_right
arabian_diccionario['idle_left'] = arabian_idle_left
arabian_diccionario['derecha'] = arabian_run_right
arabian_diccionario['izquierda'] = arabian_run_left
arabian_diccionario['salto_derecha'] = arabian_jump_right
arabian_diccionario['salto_izquierda'] = arabian_jump_left
arabian_diccionario['knok_derecha'] = arabian_knokback_derecha
arabian_diccionario['knok_izquierda'] = arabian_knokback_izquierda
arabian_diccionario['muerte_izquierda'] = arabian_muerte_izquierda
arabian_diccionario['muerte_derecha'] = arabian_muerte_derecha
arabian_diccionario['distancia_izqueirda'] = arabian_ataque_distancia_izqueirda
arabian_diccionario['distancia_derecha'] = arabian_ataque_distancia_derecha
arabian_diccionario['mele_izquierda'] = arabian_mele_izquierda
arabian_diccionario['mele_derecha'] = arabian_mele_derecha

#Sprites_Enemigos
#Mars_People
mars_people_diccionario = {}
mars_people_diccionario['idle_derecha'] = mars_idle_right
mars_people_diccionario['idle_izquierda'] = mars_idle_left
mars_people_diccionario['caminar_izquierda'] = mars_run_left
mars_people_diccionario['caminar_derecha'] = mars_run_right
mars_people_diccionario['muerte_izquierda'] = mars_muerte_izquierda
mars_people_diccionario['muerte_derecha'] = mars_muerte_derecha
mars_people_diccionario['disparo_izquierda'] = mars_shoot_left
mars_people_diccionario['disparo_derecha'] = mars_shoot_right

#Momia
momia_diccionario = {}
momia_diccionario['trampa'] = momia_trap
momia_diccionario['caminar_izquierda'] = momia_caminar_izquierda
momia_diccionario['caminar_derecha'] = momia_caminar_derecha
momia_diccionario['muerte_izquierda'] = momia_muerte_izquierda
momia_diccionario['muerte_derecha'] = momia_muerte_derecha

#Pez
pez_diccionario = {}
pez_diccionario['caminar_izquierda'] = pez_mov_izquierda
pez_diccionario['caminar_derecha'] = pez_mov_derecha
pez_diccionario['muerte_izquierda'] = pez_muerte_izquierda
pez_diccionario['muerte_derecha'] = pez_muerte_derecha

#Boss
boss_diccionario = {}
boss_diccionario['idle_left'] = boss_idle_left
boss_diccionario['idle_right'] = boss_idle_right 
boss_diccionario['run_left'] = boss_run_left 
boss_diccionario['run_right'] = boss_run_right
boss_diccionario['muerte_left'] = boss_muerte_left
boss_diccionario['muerte_right'] = boss_muerte_right 

#Trampa
barril_diccionario = {}
barril_diccionario['barril'] = barril
barril_diccionario['explosion'] = barril_explosion

#Ingreso nombre jugador
txt_box = pygame.image.load(r"Botones\Pause.png")
txt_box = pygame.transform.scale(txt_box, (600, 250))
fuente = pygame.font.Font(None, 80)

with sqlite3.connect("Datos_juego.db") as Datos:
    try:
        sentencia = '''
                    Create table Datos
                    (
                    id integer primary key autoincrement,
                    nombre text,
                    puntaje integer
                    )
                    '''
        Datos.execute(sentencia)
        print("Pronto")
    except Exception as error:
        print(error)

def sqlconnect(informacion:str):
    with sqlite3.connect("Datos_juego.db") as Datos:
        cursor = Datos.cursor()
        cursor.execute(informacion)
        filas = cursor.fetchall()
    return filas

