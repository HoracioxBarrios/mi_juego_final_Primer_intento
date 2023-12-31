import pygame
import sys
from configuracion import *
from clase_personaje import Personaje
from clase_piso import Piso
from modo_dev import *

def level_1():
    
    #pygame 2.4.0 (SDL 2.26.4, Python 3.11.2)
    pygame.init()


    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Db Z")
    relog = pygame.time.Clock()

    fondo = pygame.image.load("location\game_background_1.png")
    fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))
    pygame.mixer.music.load('sounds\epic-battle-153400.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)



    color_blue = (0,0,255)
    color_rojo = (255,0,0)
    color_green = (0,255,0)
    jugador = Personaje(pos_init_x_personaje, pos_init_y_personaje,
                        speed_caminar_personaje, speed_correr_personaje, gravedad, potencia_salto)

    # piso = Piso('sprites\StoneBlock.png',0,700)
    path_piso = 'sprites\StoneBlock.png'

    lista_pisos: list[Piso] = []

    for x in range(0, ANCHO, 100):
        lista_pisos.append(Piso(path_piso, x, 500))
    # print(lista_pisos)

    while (True):

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit() 
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_x:
                    cambiar_modo()

            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_RIGHT]:
                if teclas[pygame.K_SPACE]:
                    jugador.control("saltar")
                else:
                    jugador.control("caminar_r")
            elif teclas[pygame.K_LEFT]:
                if teclas[pygame.K_SPACE]:
                    jugador.control("saltar")
                else:
                    jugador.control("caminar_l")
            elif teclas[pygame.K_SPACE]:
                jugador.control("saltar")
            else:
                jugador.control("quieto")

        jugador.update_personaje(lista_pisos)
        jugador.draw_personaje(screen, lista_pisos)

        if get_modo():
            for piso in lista_pisos:
                pygame.draw.rect(screen, color_blue, piso.rectangulo_principal, 3)
                pygame.draw.rect(screen, color_rojo, piso.dicc_rectangulo_y_sub_rectangulos_col["lado_arriba"], 3)
                pygame.draw.rect(screen, color_rojo, piso.dicc_rectangulo_y_sub_rectangulos_col["lado_abajo"], 3)
                pygame.draw.rect(screen, color_rojo, piso.dicc_rectangulo_y_sub_rectangulos_col["lado_izquierda"], 3)
                pygame.draw.rect(screen, color_rojo, piso.dicc_rectangulo_y_sub_rectangulos_col["lado_derecha"], 3)     

            pygame.draw.rect(screen, color_rojo, jugador.colisiones_rectangulo_princial["lado_arriba"], 3)
            pygame.draw.rect(screen, color_rojo, jugador.colisiones_rectangulo_princial["lado_abajo"], 3)
            pygame.draw.rect(screen, color_rojo, jugador.colisiones_rectangulo_princial["lado_izquierda"], 3)
            pygame.draw.rect(screen, color_rojo, jugador.colisiones_rectangulo_princial["lado_derecha"], 3)
            pygame.draw.rect(screen, color_green, jugador.rectangulo_principal, 3)

        pygame.display.flip()
        screen.blit(fondo, fondo.get_rect())

        delta_ms = relog.tick(FPS)
