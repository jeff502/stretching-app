import pygame
from button import Button
from text_sprites import TextSprite


class StretchTimer:
    def __init__(self):
        self.game_started = False
        self.pause_game = False
        self.game_running = True
        self.fps = 60
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Stretch Timer")
        self.background = (0, 0, 0)
        self.font = pygame.font.SysFont("segoeui", 16)

        self.waiting_time = None
        self.clock_display = 5000

        self.current_time = 0
        self.start_button_time = 0

        self.timer_sprite = pygame.sprite.GroupSingle()
        self.text_sprite = pygame.sprite.GroupSingle()
        self.stretch_or_rest_sprite = pygame.sprite.GroupSingle()

        self.stretch_noise = pygame.mixer.Sound("assets/45083__matiasreccius__tom10_2.wav")
        self.relax_noise = pygame.mixer.Sound("assets/50963__matiasreccius__ride_rimv2-3.wav")

        self.rest = True
        self.small = False
        self.medium = False
        self.large = False

        self.small_timer = 7000
        self.medium_timer = 15000
        self.large_timer = 30000
        self.break_timer = 5000

        self.start_button = None
        self.stop_button = None
        self.pause_button = None

    def create_ui(self):
        self.create_buttons()
        self.create_text()
        self.create_stretch_or_rest()
        self.create_timer()

    def create_buttons(self):
        self.start_button = Button((100, 400), 75, 75, "Start", self.window)
        self.pause_button = Button((200, 400), 75, 75, "Pause", self.window)
        self.stop_button = Button((300, 400), 75, 75, "Stop", self.window)

    def create_timer(self):
        text_sprite = TextSprite(f"{0}", 60, (255, 255, 255), 225, 250)
        self.timer_sprite.add(text_sprite)

    def create_text(self):
        text_sprite = TextSprite("Press Start to begin", 30, (255, 255, 255), 120, 100)
        self.text_sprite.add(text_sprite)

    def create_stretch_or_rest(self):
        text_sprite = TextSprite("Rest for: ", 30, (255, 255, 255), 80, 275)
        self.stretch_or_rest_sprite.add(text_sprite)

    def draw_ui(self):
        self.text_sprite.draw(self.window)
        self.timer_sprite.draw(self.window)
        self.stretch_or_rest_sprite.draw(self.window)
        self.start_button.draw_button()
        self.pause_button.draw_button()
        self.stop_button.draw_button()

    def update_text(self, text, x, y):
        self.text_sprite.empty()
        new_text_sprite = TextSprite(text, 24, (255, 255, 255), x, y)
        self.text_sprite.add(new_text_sprite)

    def update_timer(self):
        self.timer_sprite.empty()
        new_timer_sprite = TextSprite(f"{self.clock_display // 1000}", 60, (255, 255, 255), 225, 250)
        self.timer_sprite.add(new_timer_sprite)

    def update_stretch_or_rest(self, text):
        self.stretch_or_rest_sprite.empty()
        new_text_sprite = TextSprite(f"{text} for: ", 30, (255, 255, 255), 80, 275)
        self.stretch_or_rest_sprite.add(new_text_sprite)

    def start_button_logic(self):
        self.start_button_time = pygame.time.get_ticks()
        self.game_started = True
        self.waiting_time = 5000
        self.update_text(
            text="Rest after cymbals and stretch after snare drum", x=10, y=100
        )

    def pause_button_logic(self):
        if self.pause_game is False:
            self.pause_game = True
            self.update_text(
                text="Paused", x=210, y=100
            )
        else:
            self.update_text(
                text="Rest after cymbals and stretch after snare drum", x=10, y=100
            )
            self.pause_game = False

    def start(self):
        self.window.fill(self.background)
        self.create_ui()
        clock = pygame.time.Clock()

        while self.game_running:
            self.event_handler()
            self.window.fill(self.background)
            if self.game_started:
                if self.current_time - self.start_button_time > self.waiting_time:
                    if self.rest:
                        self.update_stretch_or_rest("Stretch")
                        self.rest = False
                        if self.small:
                            self.medium, self.small = True, False
                            self.waiting_time = self.medium_timer
                        elif self.medium:
                            self.large, self.medium = True, False
                            self.waiting_time = self.large_timer
                        elif self.large:
                            self.small, self.large = True, False
                            self.waiting_time = self.small_timer
                        else:
                            self.small = True
                            self.waiting_time = self.small_timer
                        self.stretch_noise.play()
                    else:
                        self.rest = True
                        self.update_stretch_or_rest("Relax")
                        self.waiting_time = self.break_timer
                        self.relax_noise.play()

                    self.clock_display = self.waiting_time
                    self.start_button_time = pygame.time.get_ticks()

                if not self.pause_game:
                    self.current_time = pygame.time.get_ticks()
                    self.update_timer()
                    self.clock_display -= 16
            self.draw_ui()
            pygame.display.flip()
            clock.tick(self.fps)
        pygame.quit()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_running = False
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.check_button_clicked():
                    if self.game_started:
                        self.pause_button_logic()
                    else:
                        self.start_button_logic()
                elif self.stop_button.check_button_clicked():
                    if self.game_started:
                        self.clean_up()
                elif self.pause_button.check_button_clicked():
                    if self.game_started:
                        self.pause_button_logic()

    def clean_up(self):
        self.game_started = False
        self.pause_game = False
        self.rest = True
        self.small = False
        self.medium = False
        self.large = False
        self.clock_display = 5000
        self.current_time = 0
        self.start_button_time = 0
        self.window.fill(self.background)
        self.create_ui()
