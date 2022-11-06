import pygame

from cryptris.arcade_scene import ArcadeScene
from cryptris.constantes import Color
from cryptris.new_game_scene import NewGameScene


class Menu:
    def __init__(self, game):
        self.game = game
        self.run_display = True
        self.focus_rect = pygame.Rect(0, 0, 20, 20)
        self.offset_title = 70
        self.titles = None
        self.title_police_size = 50

    def blit_screen(self):
        self.game.screen.window.blit(self.game.ressources["logo_cryptris_large"], (
            self.game.screen.width / 2 - self.game.ressources["logo_cryptris_large"].get_rect().w / 2,
            0
        ))
        pygame.display.flip()
        self.game.reset_keys()

    def display_titles_menu(self, x, y, w, h):
        self.game.ui.draw_solid_line(self.game.screen.window, Color.WHITE.value, (x, y), (x + w, y), 5)
        self.game.ui.draw_solid_line(self.game.screen.window, Color.WHITE.value, (x, y + h), (x + w, y + h), 5)
        menu_rect = pygame.Surface((w, h), pygame.SRCALPHA)
        menu_rect.fill(Color.BLEU_AZUR_ALPHA.value)
        self.game.screen.window.blit(menu_rect, (x, y))
        title_menu_x = self.title_menu_x + w / 2
        title_menu_y = self.title_menu_y + h / self.prevent
        for i in range(len(self.titles)):
            color = Color.WHITE.value if self.state == i else Color.BLEU_AZUR.value
            self.game.ui.draw_text(self.titles[i], self.title_police_size, title_menu_x, title_menu_y,
                                   "font_geo_regular", color)
            if self.state == i:
                self.game.screen.window.blit(self.game.ressources["triangle_left"], (
                    title_menu_x - 10 - self.game.ressources[
                        "triangle_left"].get_rect().w - self.game.ui.current_text.w / 2,
                    title_menu_y - self.game.ressources[
                        "triangle_left"].get_rect().h / 2
                ))
                self.game.screen.window.blit(self.game.ressources["triangle_rigth"], (
                    title_menu_x + self.game.ui.current_text.w / 2 + 10, title_menu_y - self.game.ressources[
                        "triangle_rigth"].get_rect().h / 2
                ))

            title_menu_y += self.offset_title


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.titles = ("NEW GAME", "ARCADE")
        self.titles_menu_width = 300
        self.titles_menu_height = 200
        self.title_menu_x = self.game.screen.width / 2 - self.titles_menu_width / 2
        self.title_menu_y = self.game.screen.height / 2.1
        self.title_police_size = 50
        self.state = 0
        self.prevent = 3.5
        self.new_game = NewGameScene(self.game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.screen.window.blit(self.game.ressources["background"], (0, 0))
            self.game.screen.window.blit(self.game.ressources["logo_cwi_small"], (10, 25))
            self.game.screen.window.blit(self.game.ressources["logo_inria"], (self.game.screen.width - 200, 25))
            self.game.screen.window.blit(self.game.ressources["digital_cuisine"], (
                self.game.screen.width / 2 - self.game.ressources["digital_cuisine"].get_rect().w / 2,
                self.game.screen.height / 1.15
            ))
            self.display_titles_menu(self.title_menu_x,
                                     self.title_menu_y, self.titles_menu_width, self.titles_menu_height)
            self.blit_screen()

    def move_cursor(self):
        if self.game.K_DOWN or self.game.K_UP:
            self.state = 1 if self.state == 0 else 0

    def check_input(self):
        self.move_cursor()
        if self.game.K_RETURN:
            if self.state == 0:
                self.game.playing = True
                self.new_game.play_new_game()
            elif self.state == 1:
                self.game.curr_menu = self.game.arcade_menu
            self.run_display = False


class ArcadeMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.titles = ("CREATE KEYS", "BEGINNER - 8 BLOCKS", "EASY - 10 BLOCKS",
                       "MEDIUM - 12 BLOCKS", "HARD - 14 BLOCKS")
        self.state = 0
        self.offset_title = 50
        self.titles_menu_width = 300
        self.titles_menu_height = 300
        self.title_menu_x = self.game.screen.width / 2 - self.titles_menu_width / 2
        self.title_menu_y = self.game.screen.height / 2.5
        self.title_police_size = 30
        self.prevent = 7
        self.arcade_scene = ArcadeScene(self.game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.screen.window.blit(self.game.ressources["background"], (0, 0))
            self.display_titles_menu(self.title_menu_x,
                                     self.title_menu_y, self.titles_menu_width, self.titles_menu_height)
            self.blit_screen()

    def check_input(self):
        if self.game.K_RETURN:
            self.call_interface()
        if self.game.K_ESCAPE:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.K_UP or self.game.K_DOWN:
            if self.game.K_DOWN:
                if self.state + 1 >= len(self.titles):
                    self.state = 0
                else:
                    self.state += 1
            elif self.game.K_UP:
                if self.state - 1 < 0:
                    self.state = len(self.titles) - 1
                else:
                    self.state -= 1

    def call_interface(self):
        if self.state == 0:
            self.arcade_scene.play_create_key_scene()
        elif self.state == 1:
            self.arcade_scene.play_challenge_scene(8)
        elif self.state == 2:
            self.arcade_scene.play_challenge_scene(10)
        elif self.state == 3:
            self.arcade_scene.play_challenge_scene(12)
        elif self.state == 4:
            self.arcade_scene.play_challenge_scene(14)
