import pygame


class Button:
    def __init__(self, pos, width, height, text, window):
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.window = window

        self.font = pygame.font.SysFont("segoeui", 16)
        self.button_color = (87, 155, 177)
        self.hover_color = (225, 215, 198)
        self.click_color = (236, 232, 221)
        self.text_color = (0, 0, 0)

        self.top_rect = pygame.Rect(self.pos, (self.width, self.height))
        self.top_color = self.button_color

        self.bottom_rect = pygame.Rect(self.pos, (width, height))
        self.bottom_color = self.hover_color

        self.text_surf = self.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

        self.clicked = False

    def draw_button(self):
        pygame.draw.rect(self.window, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(self.window, self.top_color, self.top_rect, border_radius=12)
        self.window.blit(self.text_surf, self.text_rect)
        self.check_button_clicked()

    def check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
                return True
            else:
                if self.clicked:
                    self.clicked = False
                    return True
        else:
            self.top_color = self.button_color
        return False
