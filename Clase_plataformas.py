import pygame

class Plataforma:
    def __init__(self, ancho, alto, x, y, es_visible, imagen = ""):
        if imagen != "":
            self.superficie = pygame.image.load(imagen)
            self.superficie = pygame.transform.scale(self.superficie, (ancho, alto))
        else:
            self.superficie = pygame.Surface((ancho, alto))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.topleft = (x, y)
        self.es_visible = es_visible

    def draw(self, pantalla):
        if self.es_visible:
            pantalla.blit(self.superficie, (self.rectangulo.x, self.rectangulo.y))

    def update(self, mov_x):
        self.rectangulo.x = mov_x
    
