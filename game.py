import pygame

from cryptris.constantes import get_path, SCREEN_SIZE
from cryptris.gameplay import Gameplay
from cryptris.ressouces import load_ressources
from cryptris.menu import MainMenu, ArcadeMenu
from cryptris.ui import UI


class Screen:
    def __init__(self, screen: pygame.Surface, screen_size: tuple):
        self.window = screen
        self.width = screen_size[0]
        self.height = screen_size[1]


class Game:
    def __init__(self, window: pygame.Surface):
        self.running, self.playing = True, False
        self.ressources = load_ressources()
        self.screen = Screen(window, SCREEN_SIZE)
        self.main_menu = MainMenu(self)
        self.arcade_menu = ArcadeMenu(self)
        self.gameplay = Gameplay(self)
        self.ui = UI(self)
        self.K_DOWN = self.K_UP = self.K_LEFT = self.K_RIGHT = self.K_RETURN = self.K_ESCAPE = False
        self.curr_menu = self.main_menu
        self.dialog_size = (800, 278)

    def run(self):
        self.curr_menu.display_menu()

    @staticmethod
    def init(screen_size) -> pygame.Surface:
        # initialize the pygame module
        pygame.init()
        # load and set the logo and title
        logo = pygame.image.load(f"{get_path(__file__)}/img/icons/cryptris-icon-64.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Cryptris")
        return pygame.display.set_mode(screen_size, pygame.DOUBLEBUF)

    @staticmethod
    def quit():
        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.K_RETURN = True
                if event.key == pygame.K_ESCAPE:
                    self.K_ESCAPE = True
                if event.key == pygame.K_DOWN:
                    self.K_DOWN = True
                if event.key == pygame.K_UP:
                    self.K_UP = True
                if event.key == pygame.K_DOWN:
                    self.K_DOWN = True
                if event.key == pygame.K_UP:
                    self.K_UP = True

    def reset_keys(self):
        self.K_DOWN = self.K_UP = self.K_LEFT = self.K_RIGHT = self.K_RETURN = self.K_ESCAPE = False
