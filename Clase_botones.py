import pygame

class Boton: # Clase Boton.
    def __init__(self, x, y, imagen, ancho, alto):
        self.imagen = imagen # Defino texto
        self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        self.recta = self.imagen.get_rect()
        self.recta.topleft = (x, y)
        self.clicked = False

    def draw(self, pantalla):
        pantalla.blit(self.imagen, (self.recta.x, self.recta.y))
        
    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.recta.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                return True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return False