import pygame


class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text: str, size: int, color: tuple[int, int, int], x: int, y: int):
        super().__init__()
        self.color = color
        self.font = pygame.font.SysFont("segoeui", size)
        self.text = text
        self.x = x
        self.y = y
        self.image = self.font.render(str(self.text), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x, self.y]

    def update_text(self, text):
        self.text = text
        self.image = self.font.render(str(self.text), True, self.color)
        self.rect.topleft = [self.x, self.y]

