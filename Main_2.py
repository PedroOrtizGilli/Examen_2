from logica_2 import *
from imagenes import *
from modo import *

pygame.init()

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

    if estado_juego == "enMenu":
        arabian_nights.play()
        arabian_nights.set_volume(0.1)
        desert.stop()
        fantasy.stop()
        into_the_cosmos.stop()
        regular_show.stop()

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
            if nivel_2.click():
                estado_juego = "nivel_2"
        elif nivel_3.recta.collidepoint(mouse_pos_seleccion):
            PANTALLA.blit(fondo_nivel_3, (0,0))
            nivel_3.draw(PANTALLA)
            if nivel_3.click():
                estado_juego = "nivel_3"
        elif nivel_final.recta.collidepoint(mouse_pos_seleccion):
            PANTALLA.blit(fondo_nivel_final, (0,0))
            nivel_final.draw(PANTALLA)
            if nivel_final.click():
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
        arabian_nights.stop()
        desert.play()
        desert.set_volume(0.01)

        if keys[pygame.K_m]:
            pygame.mixer.music.set_volume(0.0)
        if keys[pygame.K_u]:
            pygame.mixer.music.set_volume(1.0)

        if keys[pygame.K_p]:
            menu_pausa = True
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
            estado_juego = "enMenu"
        if estado_juego == "enMenu":
            menu_pausa = False
            arabian_nivel_1.rectangulo_principal.topleft = pos_personaje
            arabian_nivel_1.accion = estado_personaje

            for i, enemigo in enumerate(lista_enemigos_lv1):
                enemigo.rectangulo.topleft = pos_enemigos[i]
        if continuar.click() or keys[pygame.K_ESCAPE]:
            print("llegue")
            menu_pausa = False
            arabian_nivel_1.rectangulo_principal.topleft = pos_personaje
            arabian_nivel_1.accion = estado_personaje

            for i, enemigo in enumerate(lista_enemigos_lv1):
                enemigo.rectangulo.topleft = pos_enemigos[i]

        #verificar si esta pausado para ingresar a las teclas
        if not menu_pausa:

            pos_personaje = arabian_nivel_1.rectangulo_principal.topleft
            estado_personaje = arabian_nivel_1.accion
            pos_enemigos = [(enemigo.rectangulo.topleft) for enemigo in lista_enemigos_lv1]

            if keys[pygame.K_TAB]:
                cambiar_modo()

            if keys[pygame.K_RIGHT]:
                arabian_nivel_1.accion = "derecha"
                ultima_accion = "derecha"
                arabian_nivel_1.sonido_caminar()

            if keys[pygame.K_LEFT]:
                arabian_nivel_1.accion = "izquierda"
                ultima_accion = "izquierda"
                arabian_nivel_1.sonido_caminar()

            if keys[pygame.K_UP]:
                if ultima_accion == "derecha":
                    arabian_nivel_1.accion = "salto_derecha"
                else:
                    arabian_nivel_1.accion = "salto_izquierda"

            if keys[pygame.K_j]:
                if ultima_accion == "derecha":
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - tiempo_ultimo_disparo >= 500:
                        arabian_nivel_1.disparar(ultima_accion)
                        tiempo_ultimo_disparo = tiempo_actual
                else: 
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - tiempo_ultimo_disparo >= 500:
                        arabian_nivel_1.disparar(ultima_accion)
                        tiempo_ultimo_disparo = tiempo_actual

            if not any(keys):
                if ultima_accion == "derecha":
                    arabian_nivel_1.accion = "idle_right"
                else:
                    arabian_nivel_1.accion = "idle_left"

            # prguntar en un if si esta pausado
            print(arabian_nivel_1.cantidad_saltos)
            PANTALLA.blit(fondo_nivel_1, (0,0))
            arabian_nivel_1.mostrar_vidas(PANTALLA)
            arabian_nivel_1.verificar_vidas(PANTALLA, ultima_accion)
            pausa.draw(PANTALLA)

            for m in lista_recolectables_lv1:
                m.animar(PANTALLA)

            for pla in plataformas_nivel_1:
                pla.draw(PANTALLA)

            for enemigo in lista_enemigos_lv1:
                enemigo.actualizar(PANTALLA, ayudas_lv1, arabian_nivel_1.lista_proyectiles)
                if enemigo.esta_muerto:
                    arabian_nivel_1.puntaje += enemigo.valor
                    lista_enemigos_lv1.remove(enemigo)

            arabian_nivel_1.actualizar(PANTALLA, plataformas_nivel_1)
            arabian_nivel_1.verificar_colision_enemigo(lista_enemigos_lv1, ultima_accion)
            arabian_nivel_1.verificar_colision_objetos(lista_recolectables_lv1)

            if arabian_nivel_1.esta_muerto:
                desert.stop()
                game_over.set_volume(0.1)
                game_over.play(1)
                arabian_nivel_1.murio = True
                estado_juego = "enMenu"
            
            puntaje_lv1 = mostrar_puntaje(PANTALLA, str(arabian_nivel_1.puntaje).zfill(7), times, 70, "Black", 200, 40)

            if len(lista_enemigos_lv1) == 0:
                puntaje += int(puntaje_lv1)
                estado_juego = "nivel_2"

            if get_mode():
                pygame.draw.rect(PANTALLA, "Blue", arabian_nivel_1.rectangulo_principal, 3)
                for enemigo in lista_enemigos_lv1:
                    pygame.draw.rect(PANTALLA, "Green", enemigo.rectangulo, 3)
                for disparo in arabian_nivel_1.lista_proyectiles:
                    pygame.draw.rect(PANTALLA, "Grey", disparo.rectangulo, 3)
                for pl in plataformas_nivel_1:
                    pygame.draw.rect(PANTALLA, "Red", pl.rectangulo, 3)
                for r in lista_recolectables_lv1:
                    pygame.draw.rect(PANTALLA, "Orange", r.rectangulo, 3)
                for a in ayudas_lv1:
                    pygame.draw.rect(PANTALLA, "Yellow", a.rectangulo, 3)

            arabian_nivel_2.vida = arabian_nivel_1.vida

    elif estado_juego == "nivel_2":
        arabian_nights.stop()
        desert.stop()
        fantasy.play()
        fantasy.set_volume(0.2)

        if keys[pygame.K_m]:
            pygame.mixer.music.set_volume(0.0)
        if keys[pygame.K_u]:
            pygame.mixer.music.set_volume(1.0)

        if keys[pygame.K_p]:
            menu_pausa = True
            menu_pausado.draw(PANTALLA)
            continuar.draw(PANTALLA)
            volumen.draw(PANTALLA)
            on.draw(PANTALLA)
            off.draw(PANTALLA)
            menu.draw(PANTALLA)
            if on.click():
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
            if off.click():
                pygame.mixer.music.set_volume(0.0)
            if menu.click():
                estado_juego = "enMenu"
        if continuar.click() or keys[pygame.K_ESCAPE]:
            menu_pausa = False
            arabian_nivel_2.rectangulo_principal.topleft = pos_personaje
            arabian_nivel_2.accion = estado_personaje

            for i, enemigo in enumerate(lista_enemigos_lv2):
                enemigo.rectangulo.topleft = pos_enemigos[i]

        if not menu_pausa:

            pos_personaje = arabian_nivel_2.rectangulo_principal.topleft
            estado_personaje = arabian_nivel_2.accion
            pos_enemigos = [(enemigo.rectangulo.topleft) for enemigo in lista_enemigos_lv2]

            if keys[pygame.K_TAB]:
                cambiar_modo()

            if keys[pygame.K_RIGHT]:
                arabian_nivel_2.accion = "derecha"
                ultima_accion = "derecha"
                arabian_nivel_2.sonido_caminar()

            if keys[pygame.K_LEFT]:
                arabian_nivel_2.accion = "izquierda"
                ultima_accion = "izquierda"
                arabian_nivel_2.sonido_caminar()

            if keys[pygame.K_UP]:
                if ultima_accion == "derecha":
                    arabian_nivel_2.accion = "salto_derecha"
                else:
                    arabian_nivel_2.accion = "salto_izquierda"

            elif keys[pygame.K_j]:
                if ultima_accion == "derecha":
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - tiempo_ultimo_disparo >= 500:
                        arabian_nivel_2.disparar(ultima_accion)
                        tiempo_ultimo_disparo = tiempo_actual
                else: 
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - tiempo_ultimo_disparo >= 500:
                        arabian_nivel_2.disparar(ultima_accion)
                        tiempo_ultimo_disparo = tiempo_actual

            if not any(keys):
                if ultima_accion == "derecha":
                    arabian_nivel_2.accion = "idle_right"
                else:
                    arabian_nivel_2.accion = "idle_left"

            PANTALLA.blit(fondo_nivel_2, (0,0))
            arabian_nivel_2.actualizar(PANTALLA, plataformas_nivle_2)
            arabian_nivel_2.mostrar_vidas(PANTALLA)
            arabian_nivel_2.verificar_vidas(PANTALLA, ultima_accion)
            arabian_nivel_2.verificar_colision_enemigo(lista_enemigos_lv2, ultima_accion)
            arabian_nivel_2.verificar_colision_objetos(lista_recolectables_lv2)

            puntaje_lv2 = mostrar_puntaje(PANTALLA, str(arabian_nivel_2.puntaje).zfill(7), times, 70, "White", 200, 40)

            for pla in plataformas_nivle_2:
                pla.draw(PANTALLA)

            for r in lista_recolectables_lv2:
                r.animar(PANTALLA)

            for e in lista_enemigos_lv2:
                e.actualizar(PANTALLA, ayudas_lv2, arabian_nivel_2.lista_proyectiles)
                if e.esta_muerto:
                    arabian_nivel_2.puntaje += e.valor
                    lista_enemigos_lv2.remove(e)
            arabian_nivel_2.verificar_colision_disaros(PANTALLA, e.lista_proyectiles)

            if arabian_nivel_2.esta_muerto:
                fantasy.stop()
                game_over.set_volume(0.1)
                game_over.play(1)
                arabian_nivel_1.murio = True
                estado_juego = "enMenu"
            
            if len(lista_enemigos_lv2) == 0:
                puntaje += int(puntaje_lv2)
                estado_juego = 'nivel_3'

            if get_mode():
                pygame.draw.rect(PANTALLA, "Blue", arabian_nivel_2.rectangulo_principal, 3)
                for pl in plataformas_nivle_2:
                    pygame.draw.rect(PANTALLA, "Red", pl.rectangulo, 3)
                for a in ayudas_lv2:
                    pygame.draw.rect(PANTALLA, "Yellow", a.rectangulo, 3)
                for e in lista_enemigos_lv2:
                    pygame.draw.rect(PANTALLA, 'Green', e.rectangulo, 3)
                for ra in lista_recolectables_lv2:
                    pygame.draw.rect(PANTALLA, 'Orange', ra.rectangulo, 3)

            arabian_nivel_3.vida = arabian_nivel_2.vida

    elif estado_juego == "nivel_3":
        arabian_nights.stop()
        desert.stop()
        into_the_cosmos.play()
        into_the_cosmos.set_volume(0.1)

        if keys[pygame.K_m]:
            pygame.mixer.music.set_volume(0.0)
        if keys[pygame.K_u]:
            pygame.mixer.music.set_volume(1.0)

        if keys[pygame.K_p]:
            menu_pausa = True
            menu_pausado.draw(PANTALLA)
            continuar.draw(PANTALLA)
            volumen.draw(PANTALLA)
            on.draw(PANTALLA)
            off.draw(PANTALLA)
            menu.draw(PANTALLA)
            if on.click():
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
            if off.click():
                pygame.mixer.music.set_volume(0.0)
            if menu.click():
                estado_juego = "enMenu"
        if continuar.click() or keys[pygame.K_ESCAPE]:
            menu_pausa = False
            arabian_nivel_3.rectangulo_principal.topleft = pos_personaje
            arabian_nivel_3.accion = estado_personaje

            for i, enemigo in enumerate(lista_enemigos_lv2):
                enemigo.rectangulo.topleft = pos_enemigos[i]
        
        if not menu_pausa:

            pos_personaje = arabian_nivel_3.rectangulo_principal.topleft
            estado_personaje = arabian_nivel_3.accion
            pos_enemigos = [(enemigo.rectangulo.topleft) for enemigo in lista_enemigos_lv2]

            if keys[pygame.K_TAB]:
                cambiar_modo()

            if keys[pygame.K_RIGHT]:
                arabian_nivel_3.accion = "derecha"
                ultima_accion = "derecha"
                arabian_nivel_3.sonido_caminar()

            if keys[pygame.K_LEFT]:
                arabian_nivel_3.accion = "izquierda"
                ultima_accion = "izquierda"
                arabian_nivel_3.sonido_caminar()

            if keys[pygame.K_UP]:
                if ultima_accion == "derecha":
                    arabian_nivel_3.accion = "salto_derecha"
                else:
                    arabian_nivel_3.accion = "salto_izquierda"

            if keys[pygame.K_j]:
                if ultima_accion == "derecha":
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - tiempo_ultimo_disparo >= 500:
                        arabian_nivel_3.disparar(ultima_accion)
                        tiempo_ultimo_disparo = tiempo_actual
                else: 
                    tiempo_actual = pygame.time.get_ticks()
                    if tiempo_actual - tiempo_ultimo_disparo >= 500:
                        arabian_nivel_3.disparar(ultima_accion)
                        tiempo_ultimo_disparo = tiempo_actual

            if not any(keys):
                if ultima_accion == "derecha":
                    arabian_nivel_3.accion = "idle_right"
                else:
                    arabian_nivel_3.accion = "idle_left"

            PANTALLA.blit(fondo_nivel_3, (0,0))
            arabian_nivel_3.actualizar(PANTALLA, plataformas_nivle_3)
            arabian_nivel_3.mostrar_vidas(PANTALLA)
            arabian_nivel_3.verificar_vidas(PANTALLA, ultima_accion)
            arabian_nivel_3.verificar_colision_enemigo(lista_enemigos_lv3, ultima_accion)
            arabian_nivel_3.verificar_colision_objetos(lista_recolectables_lv3)

            puntaje_lv3 = mostrar_puntaje(PANTALLA, str(arabian_nivel_3.puntaje).zfill(7), times, 70, "White", 200, 40)

            for plat in plataformas_nivle_3:
                plat.draw(PANTALLA)
            
            for rec in lista_recolectables_lv3:
                rec.animar(PANTALLA)

            for e in lista_enemigos_lv3:
                e.actualizar(PANTALLA, lista_ayduas_3, arabian_nivel_3.lista_proyectiles)
                if e.esta_muerto:
                    arabian_nivel_3.puntaje += e.valor
                    lista_enemigos_lv3.remove(e)
            
            if arabian_nivel_2.esta_muerto:
                fantasy.stop()
                game_over.set_volume(0.1)
                game_over.play(1)
                arabian_nivel_1.murio = True
                estado_juego = "enMenu"
            
            if len(lista_enemigos_lv3) == 1:
                puntaje += int(puntaje_lv3)
                estado_juego = 'nivel_final'

            if get_mode():
                pygame.draw.rect(PANTALLA, "Blue", arabian_nivel_3.rectangulo_principal, 3)
                for e in lista_enemigos_lv3:
                    pygame.draw.rect(PANTALLA, 'Red', e.rectangulo, 3)
                for p in plataformas_nivle_3:
                    pygame.draw.rect(PANTALLA, 'Yellow', p.rectangulo, 3)
                for re in lista_recolectables_lv3:
                    pygame.draw.rect(PANTALLA, "Orange", re.rectangulo, 3)
                for ay in lista_ayduas_3:
                    pygame.draw.rect(PANTALLA, 'Grey', ay.rectangulo, 3)

    elif estado_juego == "nivel_final":
        arabian_nights.stop()
        into_the_cosmos.stop()
        regular_show.play()
        regular_show.set_volume(0.1)

        if keys[pygame.K_m]:
            pygame.mixer.music.set_volume(0.0)
        if keys[pygame.K_u]:
            pygame.mixer.music.set_volume(1.0)

        if keys[pygame.K_p]:
            menu_pausa = True
            menu_pausado.draw(PANTALLA)
            continuar.draw(PANTALLA)
            volumen.draw(PANTALLA)
            on.draw(PANTALLA)
            off.draw(PANTALLA)
            menu.draw(PANTALLA)
            if on.click():
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
            if off.click():
                pygame.mixer.music.set_volume(0.0)
            if menu.click():
                estado_juego = "enMenu"
        if continuar.click() or keys[pygame.K_ESCAPE]:
            menu_pausa = False
            arabian_nivel_final.rectangulo_principal.topleft = pos_personaje
            arabian_nivel_final.accion = estado_personaje

            for i, enemigo in enumerate(lista_boss):
                enemigo.rectangulo.topleft = pos_enemigos[i]
        
        if not menu_pausa:

            pos_personaje = arabian_nivel_final.rectangulo_principal.topleft
            estado_personaje = arabian_nivel_final.accion
            pos_enemigos = [(enemigo.rectangulo.topleft) for enemigo in lista_boss]

            if keys[pygame.K_TAB]:
                cambiar_modo()

            if keys[pygame.K_RIGHT]:
                arabian_nivel_final.accion = "derecha"
                ultima_accion = "derecha"
                arabian_nivel_final.sonido_caminar()

            if keys[pygame.K_LEFT]:
                arabian_nivel_final.accion = "izquierda"
                ultima_accion = "izquierda"
                arabian_nivel_final.sonido_caminar()

            if keys[pygame.K_UP]:
                if ultima_accion == "derecha":
                    arabian_nivel_final.accion = "salto_derecha"
                else:
                    arabian_nivel_final.accion = "salto_izquierda"

            if keys[pygame.K_j]:
                if ultima_accion == "derecha":
                    tiempo_actual_final = pygame.time.get_ticks()
                    print(tiempo_actual_final - tiempo_ultimo_disparo)
                    if tiempo_actual_final - tiempo_ultimo_disparo <= 200:
                        arabian_nivel_final.disparar(ultima_accion)
                        tiempo_ultimo_disparo = tiempo_actual_final
                else: 
                    tiempo_actual_final = pygame.time.get_ticks()
                    if tiempo_actual_final - tiempo_ultimo_disparo <= 200:
                        arabian_nivel_final.disparar(ultima_accion)
                        tiempo_ultimo_disparo = tiempo_actual_final

            if not any(keys):
                if ultima_accion == "derecha":
                    arabian_nivel_final.accion = "idle_right"
                else:
                    arabian_nivel_final.accion = "idle_left"

            PANTALLA.blit(fondo_nivel_final, (0,0))
            arabian_nivel_final.vida = arabian_nivel_3.vida
            arabian_nivel_final.actualizar(PANTALLA, plataformas_nivle_final)
            arabian_nivel_final.mostrar_vidas(PANTALLA)
            arabian_nivel_final.verificar_vidas(PANTALLA, ultima_accion)
            arabian_nivel_final.verificar_colision_enemigo(lista_boss, ultima_accion)

            for e in lista_boss:
                e.actualizar(PANTALLA, arabian_nivel_final.lista_proyectiles)
                arabian_nivel_final.verificar_colision_disaros(e.lista_proyectiles)

            puntaje_lvfinal = mostrar_puntaje(PANTALLA, str(arabian_nivel_final.puntaje + puntaje).zfill(7), times, 70, "White", 200, 40)

            if arabian_nivel_2.esta_muerto:
                fantasy.stop()
                game_over.set_volume(0.1)
                game_over.play(1)
                arabian_nivel_1.murio = True
                estado_juego = "enMenu"

            if boss.esta_muerto:
                try:
                    with sqlite3.connect("Datos_juego.db") as Datos:
                        sentencia = '''
                                    insert into Datos (nombre, puntaje) values (?,?)
                                    '''
                        Datos.execute(sentencia, (nombre_jugador, puntaje))
                        Datos.commit()
                except Exception as error:
                    print(error)
                puntaje += int(puntaje_lvfinal)
                estado_juego = "enMenu"

            if get_mode():
                pygame.draw.rect(PANTALLA, "Blue", arabian_nivel_final.rectangulo_principal, 3)
                for b in lista_boss:
                    pygame.draw.rect(PANTALLA, 'Red', b.rectangulo, 3)
                for disparo in arabian_nivel_final.lista_proyectiles:
                    pygame.draw.rect(PANTALLA, "Grey", disparo.rectangulo, 3)
                for shoot in boss.lista_proyectiles:
                    pygame.draw.rect(PANTALLA, 'Grey', shoot.rectangulo, 3)
                for pl in plataformas_nivle_final:
                    pygame.draw.rect(PANTALLA, 'Yellow', pl.rectangulo, 3)

    pygame.display.update()