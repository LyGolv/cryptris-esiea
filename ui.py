import math

import pygame

from cryptris.constantes import Color


class Point:
    # constructed using a normal tupple
    def __init__(self, point_t=(0, 0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])

    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))

    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))

    def __mul__(self, scalar):
        return Point((self.x * scalar, self.y * scalar))

    def __truediv__(self, scalar):
        return Point((self.x / scalar, self.y / scalar))

    def __len__(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    # get back values in original tuple format
    def get(self):
        return self.x, self.y


class UI:
    def __init__(self, game):
        self.game = game
        self.current_text = None

    def draw_text(self, text: str, size: int, center_x: int, center_y: int, font_name: str, color: tuple):
        font = pygame.font.Font(self.game.ressources[font_name], size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        self.current_text = text_rect
        text_rect.center = (center_x, center_y)
        self.game.screen.window.blit(text_surface, text_rect)

    @staticmethod
    def draw_dashed_line(surf: pygame.Surface, color: tuple, start_pos: Point, end_pos, width=1, dash_length=10):
        origin = Point(start_pos)
        target = Point(end_pos)
        displacement = target - origin
        length = len(displacement)
        slope = displacement / length

        for index in range(0, length // dash_length, 2):
            start = origin + (slope * index * dash_length)
            end = origin + (slope * (index + 1) * dash_length)
            pygame.draw.line(surf, color, start.get(), end.get(), width)

    @staticmethod
    def draw_solid_line(surf: pygame.Surface, color: tuple, start_pos, end_pos, width=1):
        pygame.draw.line(surf, color, start_pos, end_pos, width)

    def display_text_input(self):
        self.game.screen.window.fill(Color.BLACK.value)
        pygame.display.flip()
        user_name = ""
        active = False
        font = pygame.font.Font(self.game.ressources["font_geo_regular"], 32)
        text_choose = font.render('Choose your username:', True, Color.BLEU_AZUR.value)
        text_crypto = font.render("CryptOS 355/113", True, Color.WHITE.value)
        text_info = font.render("Press ENTER / RETURN :)", True, Color.BLEU_AZUR.value)
        text_choose_rect = text_choose.get_rect()
        text_choose_rect.center = (self.game.screen.width / 2, self.game.screen.height / 1.8)
        text_crypto_rect = text_crypto.get_rect()
        text_crypto_rect.center = (self.game.screen.width / 2, self.game.screen.height / 1.15)
        text_info_rect = text_info.get_rect()
        text_info_rect.center = (self.game.screen.width / 2, self.game.screen.height / 1.3)
        line_gap = 70
        line_y = text_choose_rect.y + text_choose_rect.h + 20
        input_rect = pygame.Rect(
            text_choose_rect.x - 50 + self.game.ressources["triangle_left"].get_rect().w + 10,
            line_y + 10,
            text_choose_rect.w + 75,
            line_gap - 20
        )
        border = 5
        input_rect_internal = pygame.Rect(
            text_choose_rect.x - 50 + self.game.ressources["triangle_left"].get_rect().w + 10,
            line_y + 10,
            15,
            line_gap - 20 - border
        )
        while self.game.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    self.game.curr_menu.run_display = False
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game.curr_menu.run_display = False
                        return
                    if active:
                        # Check for backspace
                        if event.key == pygame.K_BACKSPACE:
                            # get text input from 0 to -1 i.e. end.
                            user_name = user_name[:-1]
                        elif event.key == pygame.K_RETURN:
                            return user_name
                        # Unicode standard is used for string
                        # formation
                        else:
                            if len(user_name) + 1 < 17:
                                user_name += event.unicode
            if len(user_name) == 23:
                user_name = user_name[:-1]
            self.game.screen.window.blit(
                self.game.ressources["logo_cwi"],
                (
                    self.game.screen.width / 2 - self.game.ressources["logo_cwi"].get_rect().w / 2,
                    self.game.screen.height / 5
                )
            )
            self.game.screen.window.blit(text_choose, text_choose_rect)
            # Draw line
            pygame.draw.line(
                self.game.screen.window,
                (255, 255, 255),
                (text_choose_rect.x - 50, line_y),
                (text_choose_rect.x + text_choose_rect.w + 50, line_y),
                width=3
            )
            self.game.screen.window.blit(
                self.game.ressources["triangle_left"],
                (
                    text_choose_rect.x - 50,
                    line_y + line_gap / 2 - self.game.ressources["triangle_left"].get_rect().h / 2)
            )
            # create rectangle
            if active:
                color = Color.BLEU_AZUR.value
            else:
                color = (0, 0, 0)
            pygame.draw.rect(self.game.screen.window, (0, 0, 0), input_rect)
            text_surface = font.render(user_name, True, (255, 255, 255))
            # render at position stated in arguments
            self.game.screen.window.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
            input_rect_internal.x = input_rect.x + text_surface.get_rect().w + 2
            pygame.draw.rect(self.game.screen.window, color, input_rect_internal)

            self.draw_solid_line(
                self.game.screen.window,
                (255, 255, 255),
                (text_choose_rect.x - 50, line_y + line_gap),
                (text_choose_rect.x + text_choose_rect.w + 50, line_y + line_gap),
                width=3
            )
            self.game.screen.window.blit(text_info, text_info_rect)
            self.game.screen.window.blit(text_crypto, text_crypto_rect)

            pygame.display.flip()
        return user_name

    def dialog(self, title, text, x, y, image=None):
        if image is None:
            image = self.game.ressources["avatar_chercheuse"]
        border = 10
        dialog_rect = pygame.Surface(self.game.dialog_size, pygame.SRCALPHA)
        dialog_rect.fill(Color.WHITE.value)
        dialog_rect_inside = pygame.Surface(
            (
                self.game.dialog_size[0] - image.get_rect().w - border * 3,
                self.game.dialog_size[1] - border * 2
            ),
            pygame.SRCALPHA
        )
        dialog_rect_inside.fill(Color.GRAY.value)
        dialog_rect_inside_x = x + border * 2 + image.get_rect().w
        dialog_rect_inside_y = y + border
        self.game.screen.window.blit(dialog_rect, (x, y))
        self.game.screen.window.blit(dialog_rect_inside, (
            dialog_rect_inside_x,
            y + border
        ))
        border_inside = 20
        dialog_title = pygame.Surface((170, 40), pygame.SRCALPHA)
        dialog_title.fill(Color.BLEU_AZUR.value)
        self.game.screen.window.blit(dialog_title, (
            dialog_rect_inside_x + border_inside, dialog_rect_inside_y + border_inside
        ))
        self.game.ui.draw_text(text=title, size=24,
                               center_x=dialog_rect_inside_x + dialog_title.get_rect().w // 2 + 20,
                               center_y=dialog_rect_inside_y + dialog_title.get_rect().h // 2 + 20,
                               font_name="font_quantico_bold", color=Color.WHITE.value,
                               )
        self.game.ui.draw_text(text="press ENTER >>", size=28,
                               center_x=dialog_rect_inside_x + dialog_rect_inside.get_rect().w/1.3,
                               center_y=dialog_rect_inside_y + dialog_rect_inside.get_rect().h - 20,
                               font_name="font_quantico_bold", color=Color.BLEU_AZUR.value,
                               )

        begin_x = dialog_rect_inside_x + border_inside
        begin_y = dialog_rect_inside_y + border_inside + border + dialog_title.get_rect().h + 25
        letter_space = 10
        size = 20
        for i in range(len(text)):
            if begin_x + size >= dialog_rect_inside_x + dialog_rect_inside.get_rect().w:
                begin_y += size
                begin_x = dialog_rect_inside_x + border_inside
            self.game.ui.draw_text(text=f"{text[i]}", size=size,
                                   center_x=begin_x,
                                   center_y=begin_y,
                                   font_name="font_incosolata_regular", color=Color.BLACK.value,
                                   )
            begin_x += letter_space
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    self.game.curr_menu.run_display = False
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
            self.game.screen.window.blit(image, (
                x + border, y + border
            ))
            pygame.display.flip()


class Board:

    # constructor take (x, y, w, h) property
    def __init__(self, x, y, w, h, column=8):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.column = column
        self.move = False

    # get back value to original tuple
    def get(self) -> tuple:
        return self.x, self.y, self.w, self.h

    def size(self) -> tuple:
        return self.w, self.h
