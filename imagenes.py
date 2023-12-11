import pygame

def reescalar_imagenes(diciconario_animaciones, ancho, alto):
    for clave in diciconario_animaciones:
        for i in range(len(diciconario_animaciones[clave])):
            img = diciconario_animaciones[clave][i]
            diciconario_animaciones[clave][i] = pygame.transform.scale(img, (ancho, alto))

def reescalar_disparos(lista_disparos, ancho, alto):
    for i in range(len(lista_disparos)):
        img = lista_disparos[i]
        lista_disparos[i] = pygame.transform.scale(img, (ancho, alto))

def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        img = pygame.transform.flip(imagen, flip_x, flip_y)
        lista_girada.append(img)
    return lista_girada

#Recolectables
monedas = [pygame.image.load(r"Recolectables\Monedas\1265.png"),
           pygame.image.load(r"Recolectables\Monedas\1266.png"),
           pygame.image.load(r"Recolectables\Monedas\1267.png"),
           pygame.image.load(r"Recolectables\Monedas\1268.png"),
           pygame.image.load(r"Recolectables\Monedas\1269.png"),
           pygame.image.load(r"Recolectables\Monedas\1270.png"),
           pygame.image.load(r"Recolectables\Monedas\1271.png"),
           pygame.image.load(r"Recolectables\Monedas\1272.png")]

medallas = [pygame.image.load(r"Recolectables\Medallas\1241.png"),
            pygame.image.load(r"Recolectables\Medallas\1242.png"),
            pygame.image.load(r"Recolectables\Medallas\1243.png"),
            pygame.image.load(r"Recolectables\Medallas\1244.png"),
            pygame.image.load(r"Recolectables\Medallas\1245.png"),
            pygame.image.load(r"Recolectables\Medallas\1246.png"),
            pygame.image.load(r"Recolectables\Medallas\1247.png")]

vidas = [pygame.image.load(r"Vidas\15.png")]

#ARABIAN
arabian_idle_left = [pygame.image.load(r"Arabian\Idle-caminar\4.png")]

arabian_idle_right = girar_imagenes(arabian_idle_left, True, False)

arabian_run_left = [pygame.image.load(r"Arabian\Idle-caminar\20.png"),
                pygame.image.load(r"Arabian\Idle-caminar\21.png"),
                pygame.image.load(r"Arabian\Idle-caminar\22.png"),
                pygame.image.load(r"Arabian\Idle-caminar\23.png"),
                pygame.image.load(r"Arabian\Idle-caminar\24a.png"),
                pygame.image.load(r"Arabian\Idle-caminar\24.png"),
                pygame.image.load(r"Arabian\Idle-caminar\25.png"),
                pygame.image.load(r"Arabian\Idle-caminar\26.png"),
                pygame.image.load(r"Arabian\Idle-caminar\27.png"),
                pygame.image.load(r"Arabian\Idle-caminar\28.png"),
                pygame.image.load(r"Arabian\Idle-caminar\29.png"),
                pygame.image.load(r"Arabian\Idle-caminar\30.png")]

arabian_run_right = girar_imagenes(arabian_run_left, True, False)

arabian_jump_left = [
                    pygame.image.load(r"Arabian\Salto\40.png")
                    ]

arabian_jump_right = girar_imagenes(arabian_jump_left, True, False)

arabian_agachado_izquierda = [pygame.image.load(r"Arabian\Agacharse\162.png"),
                    pygame.image.load(r"Arabian\Agacharse\163.png"),
                    pygame.image.load(r"Arabian\Agacharse\164.png"),
                    pygame.image.load(r"Arabian\Agacharse\278.png")]

arabian_agachado_derecha = girar_imagenes(arabian_agachado_izquierda, True, False)

arabian_knokback_derecha= [pygame.image.load(r"Arabian\Knokback\0.png"),
                    pygame.image.load(r"Arabian\Knokback\1.png"),
                    pygame.image.load(r"Arabian\Knokback\3.png"),
                    pygame.image.load(r"Arabian\Knokback\3.png"),
                    pygame.image.load(r"Arabian\Knokback\4.png")]

arabian_knokback_izquierda = girar_imagenes(arabian_knokback_derecha, True, False)

arabian_muerte_izquierda = [pygame.image.load(r"Arabian\Muerte\288.png"),
                            pygame.image.load(r"Arabian\Muerte\288.png"),
                            pygame.image.load(r"Arabian\Muerte\289.png"),
                            pygame.image.load(r"Arabian\Muerte\289.png"),
                            pygame.image.load(r"Arabian\Muerte\290.png"),
                            pygame.image.load(r"Arabian\Muerte\290.png"),
                            pygame.image.load(r"Arabian\Muerte\291.png"),
                            pygame.image.load(r"Arabian\Muerte\291.png"),
                            pygame.image.load(r"Arabian\Muerte\292.png"),
                            pygame.image.load(r"Arabian\Muerte\292.png"),
                            pygame.image.load(r"Arabian\Muerte\293.png"),
                            pygame.image.load(r"Arabian\Muerte\293.png"),
                            pygame.image.load(r"Arabian\Muerte\294.png"),
                            pygame.image.load(r"Arabian\Muerte\294.png"),
                            pygame.image.load(r"Arabian\Muerte\295.png"),
                            pygame.image.load(r"Arabian\Muerte\295.png"),
                            pygame.image.load(r"Arabian\Muerte\296.png"),
                            pygame.image.load(r"Arabian\Muerte\296.png"),
                            pygame.image.load(r"Arabian\Muerte\297.png"),
                            pygame.image.load(r"Arabian\Muerte\297.png"),
                            pygame.image.load(r"Arabian\Muerte\316.png"),
                            pygame.image.load(r"Arabian\Muerte\316.png")]

arabian_muerte_derecha = girar_imagenes(arabian_muerte_izquierda, True, False)

arabian_ataque_distancia_izqueirda = [pygame.image.load(r"Arabian\Ataque a distancia\1.png"),
                                      pygame.image.load(r"Arabian\Ataque a distancia\2.png"),
                                      pygame.image.load(r"Arabian\Ataque a distancia\3.png"),
                                      pygame.image.load(r"Arabian\Ataque a distancia\4.png"),
                                      pygame.image.load(r"Arabian\Ataque a distancia\5.png"),
                                      pygame.image.load(r"Arabian\Ataque a distancia\6.png"),
                                      pygame.image.load(r"Arabian\Ataque a distancia\7.png"),
                                      pygame.image.load(r"Arabian\Ataque a distancia\8.png")]

arabian_ataque_distancia_derecha = girar_imagenes(arabian_ataque_distancia_izqueirda, True, False)

arabian_espada_izquierda = [pygame.image.load(r"Arabian\Ataque a distancia\Espada\1.png"),
                            pygame.image.load(r"Arabian\Ataque a distancia\Espada\2.png"),
                            pygame.image.load(r"Arabian\Ataque a distancia\Espada\3.png"),
                            pygame.image.load(r"Arabian\Ataque a distancia\Espada\4.png"),
                            pygame.image.load(r"Arabian\Ataque a distancia\Espada\5.png"),
                            pygame.image.load(r"Arabian\Ataque a distancia\Espada\6.png"),
                            pygame.image.load(r"Arabian\Ataque a distancia\Espada\7.png"),
                            pygame.image.load(r"Arabian\Ataque a distancia\Espada\8.png"),
                            pygame.image.load(r"Arabian\Ataque a distancia\Espada\9.png")]

arabian_espada_derecha = girar_imagenes(arabian_espada_izquierda, True, False)

arabian_mele_izquierda = [pygame.image.load(r"Arabian\Ataque_melee\1.png"),
                          pygame.image.load(r"Arabian\Ataque_melee\2.png"),
                          pygame.image.load(r"Arabian\Ataque_melee\3.png")]

arabian_mele_derecha = girar_imagenes(arabian_mele_izquierda, True, False)

arabian_vidas = [pygame.image.load(r"Vidas\0.png"),
                 pygame.image.load(r"Vidas\1.png"),
                 pygame.image.load(r"Vidas\2.png"),
                 pygame.image.load(r"Vidas\3.png"),
                 pygame.image.load(r"Vidas\4.png")]

reescalar_disparos(arabian_vidas, 30, 20)

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

#MARS PEOPLE
mars_idle_left = [pygame.image.load(r"Mars_people\Idle\2.png"),
                   pygame.image.load(r"Mars_people\Idle\3.png"),
                   pygame.image.load(r"Mars_people\Idle\4.png"),
                   pygame.image.load(r"Mars_people\Idle\5.png"),
                   pygame.image.load(r"Mars_people\Idle\6.png"),
                   pygame.image.load(r"Mars_people\Idle\7.png"),
                   pygame.image.load(r"Mars_people\Idle\8.png"),
                   pygame.image.load(r"Mars_people\Idle\9.png"),
                   pygame.image.load(r"Mars_people\Idle\10.png"),
                   pygame.image.load(r"Mars_people\Idle\11.png"),
                   pygame.image.load(r"Mars_people\Idle\12.png"),
                   pygame.image.load(r"Mars_people\Idle\13.png"),
                   pygame.image.load(r"Mars_people\Idle\14.png"),
                   pygame.image.load(r"Mars_people\Idle\15.png"),
                   pygame.image.load(r"Mars_people\Idle\16.png"),
                   pygame.image.load(r"Mars_people\Idle\17.png")]

mars_idle_right = girar_imagenes(mars_idle_left, True, False)

mars_run_left = [pygame.image.load(r"Mars_people\Caminar\20.png"),
                 pygame.image.load(r"Mars_people\Caminar\21.png"),
                 pygame.image.load(r"Mars_people\Caminar\22.png"),
                 pygame.image.load(r"Mars_people\Caminar\23.png"),
                 pygame.image.load(r"Mars_people\Caminar\24.png"),
                 pygame.image.load(r"Mars_people\Caminar\25.png"),
                 pygame.image.load(r"Mars_people\Caminar\26.png"),
                 pygame.image.load(r"Mars_people\Caminar\27.png"),
                 pygame.image.load(r"Mars_people\Caminar\28.png"),
                 pygame.image.load(r"Mars_people\Caminar\29.png"),
                 pygame.image.load(r"Mars_people\Caminar\30.png"),
                 pygame.image.load(r"Mars_people\Caminar\31.png"),
                 pygame.image.load(r"Mars_people\Caminar\32.png"),
                 pygame.image.load(r"Mars_people\Caminar\33.png"),
                 pygame.image.load(r"Mars_people\Caminar\34.png"),
                 pygame.image.load(r"Mars_people\Caminar\35.png"),]

mars_run_right = girar_imagenes(mars_run_left, True, False)

mars_shoot_left = [pygame.image.load(r"Mars_people\Disparo\79.png"),
                   pygame.image.load(r"Mars_people\Disparo\80.png"),
                   pygame.image.load(r"Mars_people\Disparo\82.png"),
                   pygame.image.load(r"Mars_people\Disparo\83.png"),
                   pygame.image.load(r"Mars_people\Disparo\84.png"),
                   pygame.image.load(r"Mars_people\Disparo\100.png")]

mars_shoot_right = girar_imagenes(mars_shoot_left, True, False)

mars_bullet_left = [pygame.image.load(r"Mars_people\Disparo\436.png")]

mars_bullet_righ = girar_imagenes(mars_bullet_left, True, False)

mars_muerte_izquierda = [pygame.image.load(r"Mars_people\Muerte\281.png"),
               pygame.image.load(r"Mars_people\Muerte\282.png"),
               pygame.image.load(r"Mars_people\Muerte\283.png"),
               pygame.image.load(r"Mars_people\Muerte\284.png"),
               pygame.image.load(r"Mars_people\Muerte\285.png"),
               pygame.image.load(r"Mars_people\Muerte\286.png"),
               pygame.image.load(r"Mars_people\Muerte\287.png"),
               pygame.image.load(r"Mars_people\Muerte\288.png"),
               pygame.image.load(r"Mars_people\Muerte\289.png"),
               pygame.image.load(r"Mars_people\Muerte\290.png"),
               pygame.image.load(r"Mars_people\Muerte\291.png"),
               pygame.image.load(r"Mars_people\Muerte\293.png"),
               pygame.image.load(r"Mars_people\Muerte\294.png"),
               pygame.image.load(r"Mars_people\Muerte\295.png"),
               pygame.image.load(r"Mars_people\Muerte\296.png"),
               pygame.image.load(r"Mars_people\Muerte\297.png"),
               pygame.image.load(r"Mars_people\Muerte\298.png"),
               pygame.image.load(r"Mars_people\Muerte\299.png"),
               pygame.image.load(r"Mars_people\Muerte\300.png"),
               pygame.image.load(r"Mars_people\Muerte\301.png"),
               pygame.image.load(r"Mars_people\Muerte\302.png"),
               pygame.image.load(r"Mars_people\Muerte\303.png"),
               pygame.image.load(r"Mars_people\Muerte\304.png"),
               pygame.image.load(r"Mars_people\Muerte\305.png"),
               pygame.image.load(r"Mars_people\Muerte\306.png"),
               pygame.image.load(r"Mars_people\Muerte\307.png"),
               pygame.image.load(r"Mars_people\Muerte\310.png"),
               pygame.image.load(r"Mars_people\Muerte\311.png"),
               pygame.image.load(r"Mars_people\Muerte\315.png"),
               pygame.image.load(r"Mars_people\Muerte\319.png"),
               pygame.image.load(r"Mars_people\Muerte\330.png"),
               pygame.image.load(r"Mars_people\Muerte\334.png"),
               pygame.image.load(r"Mars_people\Muerte\335.png"),
               pygame.image.load(r"Mars_people\Muerte\336.png"),
               pygame.image.load(r"Mars_people\Muerte\337.png"),
               pygame.image.load(r"Mars_people\Muerte\338.png"),
               pygame.image.load(r"Mars_people\Muerte\339.png"),
               pygame.image.load(r"Mars_people\Muerte\340.png"),
               pygame.image.load(r"Mars_people\Muerte\341.png"),
               pygame.image.load(r"Mars_people\Muerte\342.png")]

mars_muerte_derecha = girar_imagenes(mars_muerte_izquierda, True, False)

#Mummy

momia_trap = [pygame.image.load(r"Mummy_enemy\Trampa\750.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\749.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\748.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\747.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\746.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\745.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\744.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\743.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\742.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\741.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\740.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\739.png"),
              pygame.image.load(r"Mummy_enemy\Trampa\738.png")]

momia_caminar_izquierda = [pygame.image.load(r"Mummy_enemy\Caminar\362.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\363.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\364.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\365.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\366.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\367.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\368.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\369.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\370.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\371.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\372.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\373.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\374.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\375.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\376.png"),
                           pygame.image.load(r"Mummy_enemy\Caminar\377.png")]

momia_caminar_derecha = girar_imagenes(momia_caminar_izquierda, True, False)

momia_muerte_izquierda = [pygame.image.load(r"Mummy_enemy\Muerte\1.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\2.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\3.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\4.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\5.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\6.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\7.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\8.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\9.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\10.png"),
                          pygame.image.load(r"Mummy_enemy\Muerte\11.png"),]

momia_muerte_derecha = girar_imagenes(momia_muerte_izquierda, True, False)

momia_diccionario = {}
momia_diccionario['trampa'] = momia_trap
momia_diccionario['caminar_izquierda'] = momia_caminar_izquierda
momia_diccionario['caminar_derecha'] = momia_caminar_derecha
momia_diccionario['muerte_izquierda'] = momia_muerte_izquierda
momia_diccionario['muerte_derecha'] = momia_muerte_derecha

#Pez

pez_mov_izquierda = [pygame.image.load(r"Pez_volador\Movimiento\12.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\14.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\15.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\16.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\17.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\18.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\19.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\20.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\21.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\22.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\23.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\24.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\25.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\26.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\27.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\28.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\29.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\30.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\31.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\32.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\33.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\34.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\35.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\36.png"),
                     pygame.image.load(r"Pez_volador\Movimiento\37.png"),]

pez_mov_derecha = girar_imagenes(pez_mov_izquierda, True, False)

pez_muerte_izquierda = [pygame.image.load(r"Pez_volador\Muerte\1.png"),
                        pygame.image.load(r"Pez_volador\Muerte\2.png"),
                        pygame.image.load(r"Pez_volador\Muerte\3.png"),
                        pygame.image.load(r"Pez_volador\Muerte\4.png"),
                        pygame.image.load(r"Pez_volador\Muerte\5.png"),
                        pygame.image.load(r"Pez_volador\Muerte\6.png"),
                        pygame.image.load(r"Pez_volador\Muerte\7.png"),
                        pygame.image.load(r"Pez_volador\Muerte\8.png"),
                        pygame.image.load(r"Pez_volador\Muerte\9.png"),
                        pygame.image.load(r"Pez_volador\Muerte\10.png"),]

pez_muerte_derecha = girar_imagenes(pez_muerte_izquierda, True, False)

#Boss

boss_idle_left = [pygame.image.load(r"Jefe_final\Idle\1.png"),
                  pygame.image.load(r"Jefe_final\Idle\2.png"),
                  pygame.image.load(r"Jefe_final\Idle\3.png"),
                  pygame.image.load(r"Jefe_final\Idle\4.png"),
                  pygame.image.load(r"Jefe_final\Idle\5.png"),
                  pygame.image.load(r"Jefe_final\Idle\6.png"),
                  pygame.image.load(r"Jefe_final\Idle\7.png"),
                  pygame.image.load(r"Jefe_final\Idle\8.png"),]

boss_idle_right = girar_imagenes(boss_idle_left, True, False)

boss_run_left = [pygame.image.load(r"Jefe_final\Movimiento\10.png"),
                 pygame.image.load(r"Jefe_final\Movimiento\11.png"),
                 pygame.image.load(r"Jefe_final\Movimiento\12.png"),
                 pygame.image.load(r"Jefe_final\Movimiento\13.png"),
                 pygame.image.load(r"Jefe_final\Movimiento\14.png"),
                 pygame.image.load(r"Jefe_final\Movimiento\15.png"),
                 pygame.image.load(r"Jefe_final\Movimiento\16.png"),
                 pygame.image.load(r"Jefe_final\Movimiento\17.png"),]

boss_run_right = girar_imagenes(boss_run_left, True, False)

boss_shoot_bajo_left = [pygame.image.load(r"Jefe_final\Ataque_lengua_bajo\111.png")]

boss_shoot_bajo_right = girar_imagenes(boss_shoot_bajo_left, True, False)

boss_muerte_left = [pygame.image.load(r"Jefe_final\Muerte\1.png"),
                    pygame.image.load(r"Jefe_final\Muerte\2.png"),
                    pygame.image.load(r"Jefe_final\Muerte\3.png"),
                    pygame.image.load(r"Jefe_final\Muerte\4.png"),
                    pygame.image.load(r"Jefe_final\Muerte\5.png"),
                    pygame.image.load(r"Jefe_final\Muerte\6.png"),
                    pygame.image.load(r"Jefe_final\Muerte\7.png"),
                    pygame.image.load(r"Jefe_final\Muerte\8.png"),
                    pygame.image.load(r"Jefe_final\Muerte\9.png"),
                    pygame.image.load(r"Jefe_final\Muerte\10.png"),
                    pygame.image.load(r"Jefe_final\Muerte\11.png"),
                    pygame.image.load(r"Jefe_final\Muerte\12.png"),
                    pygame.image.load(r"Jefe_final\Muerte\13.png"),
                    pygame.image.load(r"Jefe_final\Muerte\14.png"),
                    pygame.image.load(r"Jefe_final\Muerte\15.png"),
                    pygame.image.load(r"Jefe_final\Muerte\16.png"),
                    pygame.image.load(r"Jefe_final\Muerte\17.png"),
                    pygame.image.load(r"Jefe_final\Muerte\18.png"),
                    pygame.image.load(r"Jefe_final\Muerte\19.png"),
                    pygame.image.load(r"Jefe_final\Muerte\20.png"),
                    pygame.image.load(r"Jefe_final\Muerte\21.png"),
                    pygame.image.load(r"Jefe_final\Muerte\22.png"),
                    pygame.image.load(r"Jefe_final\Muerte\23.png"),]

boss_muerte_right = girar_imagenes(boss_muerte_left, True, False)

#Barril

barril = [pygame.image.load(r"Barril\1.png"),
          pygame.image.load(r"Barril\0.png")]

barril_explosion = [pygame.image.load(r"Explosiones\1.png"),
                    pygame.image.load(r"Explosiones\2.png"),
                    pygame.image.load(r"Explosiones\3.png"),
                    pygame.image.load(r"Explosiones\4.png"),
                    pygame.image.load(r"Explosiones\5.png"),
                    pygame.image.load(r"Explosiones\6.png"),
                    pygame.image.load(r"Explosiones\7.png"),
                    pygame.image.load(r"Explosiones\8.png"),
                    pygame.image.load(r"Explosiones\9.png"),
                    pygame.image.load(r"Explosiones\10.png"),
                    pygame.image.load(r"Explosiones\11.png"),
                    pygame.image.load(r"Explosiones\12.png"),
                    pygame.image.load(r"Explosiones\13.png"),
                    pygame.image.load(r"Explosiones\14.png"),
                    pygame.image.load(r"Explosiones\15.png"),
                    pygame.image.load(r"Explosiones\16.png"),
                    pygame.image.load(r"Explosiones\17.png"),
                    pygame.image.load(r"Explosiones\18.png"),
                    pygame.image.load(r"Explosiones\19.png"),
                    pygame.image.load(r"Explosiones\20.png"),
                    pygame.image.load(r"Explosiones\21.png"),
                    pygame.image.load(r"Explosiones\22.png"),
                    pygame.image.load(r"Explosiones\23.png"),
                    pygame.image.load(r"Explosiones\24.png"),]