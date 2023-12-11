from logica_2 import *
from imagenes import *
from modo import *
from Clase_Nivel_1 import NivelUno
from Clase_Nivel_2 import NivelDos
from Clase_nivel_3 import NivelTres
from Clase_nivel_final import NivelFinal

pygame.init()

dict_niveles = {"nivel_1": NivelUno(PANTALLA), "nivel_2": NivelDos(PANTALLA), "nivel_3": NivelTres(PANTALLA),
                "nivel_final": NivelFinal(PANTALLA)}

while running:
    clock.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                cambiar_modo()
    keys = pygame.key.get_pressed()

    if estado_juego == "nombre":
        PANTALLA.blit(fondo, (0, 0))
        PANTALLA.blit(txt_box, (550, 300))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                nombre_jugador = nombre_jugador[:-1]
            elif event.key == pygame.K_INSERT and nombre_jugador != '':
                estado_juego = "enMenu"
            else:
                nombre_jugador += event.unicode

        superficie_texto = fuente.render(nombre_jugador, True, 'White')
        PANTALLA.blit(superficie_texto, (700, 430))

    elif estado_juego == "enMenu":
        arabian_nights.play()
        arabian_nights.set_volume(0.1)
        desert.stop()
        fantasy.stop()
        into_the_cosmos.stop()
        regular_show.stop()
        stage_clear.stop()
        game_over.stop()

        PANTALLA.blit(fondo, (0, 0))
        PANTALLA.blit(nombre, (550, 30))
        jugar.draw(PANTALLA)
        configuracion.draw(PANTALLA)
        marcador.draw(PANTALLA)
        salir.draw(PANTALLA)

        if jugar.click():
            estado_juego = "seleccion"
        if configuracion.click():
            estado_juego = "configuracion"
        if marcador.click():
            estado_juego = "enMarcador"
        if salir.click():
            pygame.quit()
            sys.exit()

    elif estado_juego == "seleccion":
        PANTALLA.blit(fondo, (0, 0))
        mouse_pos_seleccion = pygame.mouse.get_pos()
        nivel_1.draw(PANTALLA)
        nivel_2.draw(PANTALLA)
        nivel_3.draw(PANTALLA)
        nivel_final.draw(PANTALLA)
        volver_boton.draw(PANTALLA)
        if volver_boton.click():
            estado_juego = "enMenu"
        if nivel_1.recta.collidepoint(mouse_pos_seleccion):
            PANTALLA.blit(fondo_nivel_1, (0,0))
            nivel_1.draw(PANTALLA)
            if nivel_1.click():
                estado_juego = "nivel_1"
        elif nivel_2.recta.collidepoint(mouse_pos_seleccion):
            PANTALLA.blit(fondo_nivel_2, (0,0))
            nivel_2.draw(PANTALLA)
            if nivel_2.click() and lv2_unlock:
                estado_juego = "nivel_2"
        elif nivel_3.recta.collidepoint(mouse_pos_seleccion):
            PANTALLA.blit(fondo_nivel_3, (0,0))
            nivel_3.draw(PANTALLA)
            if nivel_3.click() and lv3_unlock:
                estado_juego = "nivel_3"
        elif nivel_final.recta.collidepoint(mouse_pos_seleccion):
            PANTALLA.blit(fondo_nivel_final, (0,0))
            nivel_final.draw(PANTALLA)
            if nivel_final.click() and lv4_unlock:
                estado_juego = "nivel_final"

    elif estado_juego == "configuracion":
        PANTALLA.blit(fondo, (0, 0))
        volver_boton.draw(PANTALLA)
        volumen.draw(PANTALLA)
        on.draw(PANTALLA)
        off.draw(PANTALLA)
        if volver_boton.click():
            estado_juego = "enMenu"

    elif estado_juego == "enMarcador":
        PANTALLA.blit(fondo, (0, 0))
        arabian_nights.stop()
        conteo_puntos.play(1)
        conteo_puntos.set_volume(0.01)
        volver_boton.draw(PANTALLA)
        y = 300
        filas = sqlconnect("select * from Datos order by puntaje desc limit 3")
        for fila in filas:
            texto_fila = ' '.join(map(str, fila))
            jugador = fuente.render(texto_fila, True, 'White')
            PANTALLA.blit(jugador, (700, y))
            y += 100
        if volver_boton.click():
            estado_juego = "enMenu"

    elif estado_juego == "nivel_1":
        if bandera_lv1:
            nivel_actual.final = False
            dict_niveles["nivel_1"] = NivelUno(PANTALLA)
            bandera_lv1 = False
        else:
            nivel_actual = dict_niveles["nivel_1"]
            nivel_actual.update(eventos, estado_juego)
            arabian_nights.stop()
            desert.play(1)   
            desert.set_volume(0.01)

            if nivel_actual.enemigos_muertos():
                stage_clear_surface.draw(PANTALLA)
                desert.stop()
                stage_clear.play(1)
                stage_clear.set_volume(0.1)
                lv2_unlock = True
                if stage_clear_surface.click():
                    estado_juego = "nivel_2"
                    bandera_lv1 = True

            if nivel_actual.arabian.esta_muriendo:
                nivel_actual.final = True
                game_over_surface.draw(PANTALLA)
                desert.stop()
                game_over.play(1)
                game_over.set_volume(0.1)
                if game_over_surface.click():
                    estado_juego = "enMenu"
                    bandera_lv1 = True

            if nivel_actual.volver_menu:
                estado_juego = "enMenu"

            if estado_juego != 'nivel_1' and not nivel_actual.volver_menu:
                del dict_niveles["nivel_1"]

    elif estado_juego == "nivel_2" and lv2_unlock:
        if bandera_lv2:
            nivel_actual.final = False
            dict_niveles["nivel_2"] = NivelDos(PANTALLA)
            bandera_lv2 = False
        else:
            nivel_actual = dict_niveles["nivel_2"]
            nivel_actual.update(eventos, estado_juego)
            arabian_nights.stop()
            stage_clear.stop()
            desert.stop()
            fantasy.play(1)
            fantasy.set_volume(0.01)

            if nivel_actual.enemigos_muertos():
                stage_clear_surface.draw(PANTALLA)
                stage_clear.play(1)
                stage_clear.set_volume(0.1)
                lv3_unlock = True
                if stage_clear_surface.click():
                    estado_juego = "nivel_3"
                    bandera_lv2 = True
            
            if nivel_actual.arabian.esta_muriendo:
                nivel_actual.final = True
                game_over_surface.draw(PANTALLA)
                fantasy.stop()
                game_over.play(1)
                game_over.set_volume(0.1)
                if game_over_surface.click():
                    estado_juego = "enMenu"
                    bandera_lv2 = True
            
            if estado_juego != 'nivel_2':
                del dict_niveles["nivel_2"]

    elif estado_juego == "nivel_3" and lv3_unlock:
        if bandera_lv3:
            nivel_actual.final = False
            dict_niveles["nivel_3"] = NivelTres(PANTALLA)
            bandera_lv3 = False
        else:
            nivel_actual = dict_niveles["nivel_3"]
            nivel_actual.update(eventos, estado_juego)
            arabian_nights.stop()
            stage_clear.stop()
            fantasy.stop()
            into_the_cosmos.play(1)
            into_the_cosmos.set_volume(0.01)

            if nivel_actual.enemigos_muertos():
                stage_clear_surface.draw(PANTALLA)
                stage_clear.play(1)
                stage_clear.set_volume(0.1)
                lv4_unlock = True
                if stage_clear_surface.click():
                    estado_juego = "nivel_final"
                    bandera_lv3 = True

            if nivel_actual.arabian.esta_muriendo:
                nivel_actual.final = True
                game_over_surface.draw(PANTALLA)
                into_the_cosmos.stop()
                game_over.play(1)
                game_over.set_volume(0.1)
                if game_over_surface.click():
                    estado_juego = "enMenu"
                    bandera_lv3 = True

            if estado_juego != 'nivel_3':
                del dict_niveles["nivel_3"]

    elif estado_juego == "nivel_final" and lv4_unlock:
        if bandera_lv4:
            nivel_actual.final = False
            dict_niveles["nivel_final"] = NivelFinal(PANTALLA)
            bandera_lv4 = False
        else:
            nivel_actual = dict_niveles["nivel_final"]
            nivel_actual.update(eventos, estado_juego)
            arabian_nights.stop()
            stage_clear.stop()
            into_the_cosmos.stop()
            regular_show.play(1)
            regular_show.set_volume(0.01)

            if nivel_actual.enemigos_muertos():
                stage_clear_surface.draw(PANTALLA)
                stage_clear.play(1)
                stage_clear.set_volume(0.1)
                try:
                    with sqlite3.connect("Datos_juego.db") as Datos:
                        sentencia = '''
                                    insert into Datos (nombre, puntaje) values (?,?)
                                    '''
                        Datos.execute(sentencia, (nombre_jugador, nivel_actual.arabian.puntaje))
                        Datos.commit()
                except Exception as error:
                    print(error)
                if stage_clear_surface.click():
                    estado_juego = "enMenu"
                    bandera_lv4 = True
            
            if nivel_actual.arabian.esta_muriendo:
                nivel_actual.final = True
                game_over_surface.draw(PANTALLA)
                regular_show.stop()
                game_over.play(1)
                game_over.set_volume(0.1)
                if game_over_surface.click():
                    estado_juego = "enMenu"
                    bandera_lv4 = True
            
            if estado_juego != 'nivel_final':
                del dict_niveles["nivel_final"]

    pygame.display.update()