import math
import random

import pygame

from cryptris import crypto
from cryptris.constantes import SCREEN_SIZE, Color, BORDER_BOARD, COLUMN_SPACE, COLUMN_WIDTH, \
    BLOCK_HEIGTH, BLOCK_SPACE, pregenerate_private_keys, NUMBER_DIGIT, REPEAT_GEN_PUBLIC_KEY, MESSAGE
from cryptris.crypto import encode_message
from cryptris.ui import Board


class Gameplay:
    def __init__(self, game):
        self.game = game
        self.private_key: list = []
        self.bottom_array: list = []
        self.public_key: list = []
        self.board_column: int = 0
        self.counter = 0
        self.state = True
        self.create_key = False
        self.message = ""

    @staticmethod
    def create_board(board_x: int, board_y: int, board_w: int, board_h: int, column: int):
        return Board(x=board_x, y=board_y, w=board_w, h=board_h, column=column)

    def display_game_items(self, start_x, start_y, current_time, create_key=False):
        """
        Display all statics images on the screen
        :param current_time:
        :param create_key:
        :param start_y:
        :param start_x:
        :return:
        """
        self.game.screen.window.blit(self.game.ressources["background"], (0, 0))
        position = [start_x - self.game.ressources["cryptris_board"].get_rect().width / 2, start_y]
        self.game.screen.window.blit(self.game.ressources["cryptris_board"], position)
        position[1] += 110
        self.game.screen.window.blit(
            self.game.ressources["lcd_board_game"],
            (start_x - self.game.ressources["lcd_board_game"].get_rect().width / 2, position[1])
        )
        self.game.ui.draw_text(
            self.convert_time(current_time),
            28,
            start_x,
            position[1] + 20,
            "font_geo_regular",
            Color.GREEN.value
        )
        position[1] += 80
        self.game.screen.window.blit(
            self.game.ressources["btn_pause_game"],
            (start_x - self.game.ressources["btn_pause_game"].get_rect().width - 10, position[1])
        )
        self.game.screen.window.blit(
            self.game.ressources["btn_interrogation_game"],
            (start_x + 10, position[1])
        )
        position[1] += 80
        if create_key:
            self.gauge_info(start_x, position[1])
            position[1] += 90
        self.game.screen.window.blit(
            self.game.ressources["btn_direction_full"],
            (start_x - self.game.ressources["btn_direction_full"].get_rect().width / 2, position[1])
        )

    @staticmethod
    def convert_time(game_time):
        time_in_second = math.floor(game_time / 1000)
        hours = math.floor(time_in_second / 3600)
        minute_in_second = time_in_second % 3600
        minutes = math.floor(minute_in_second / 60)
        seconds = minute_in_second % 60
        hours_str = f"{hours}"
        if hours < 10:
            hours_str = "0" + hours_str
        minutes_str = f"{minutes}"
        if minutes < 10:
            minutes_str = "0" + minutes_str
        seconds_str = f"{seconds}"
        if seconds < 10:
            seconds_str = "0" + seconds_str
        return hours_str + ":" + minutes_str + ":" + seconds_str

    def gauge_info(self, start_x, position_y):
        score = crypto.cal_score(self.bottom_array)
        if score == 0:
            self.game.screen.window.blit(
                self.game.ressources["gauge_indetermine"],
                (start_x - self.game.ressources["gauge_indetermine"].get_rect().width / 2, position_y)
            )
        elif score < 1.5:
            self.game.screen.window.blit(
                self.game.ressources["gauge_mauvaise"],
                (start_x - self.game.ressources["gauge_mauvaise"].get_rect().width / 2, position_y)
            )
        elif 1.5 <= score < 2:
            self.game.screen.window.blit(
                self.game.ressources["gauge_mediocre"],
                (start_x - self.game.ressources["gauge_mediocre"].get_rect().width / 2, position_y)
            )
        elif 2 <= score < 2.5:
            self.game.screen.window.blit(
                self.game.ressources["gauge_faible"],
                (start_x - self.game.ressources["gauge_faible"].get_rect().width / 2, position_y)
            )
        elif 2.5 <= score < 3:
            self.game.screen.window.blit(
                self.game.ressources["gauge_correct"],
                (start_x - self.game.ressources["gauge_correct"].get_rect().width / 2, position_y)
            )
        elif 3 <= score < 4:
            self.game.screen.window.blit(
                self.game.ressources["gauge_bonne"],
                (start_x - self.game.ressources["gauge_bonne"].get_rect().width / 2, position_y)
            )
        else:
            self.game.screen.window.blit(
                self.game.ressources["gauge_excellente"],
                (start_x - self.game.ressources["gauge_excellente"].get_rect().width / 2, position_y)
            )

    def draw_player_board(self, board, user_name):
        self.draw_board(board, color=(0, 113, 187, 64))
        self.print_user_name(board, user_name)
        self.draw_all_blocks(board)
        self.draw_numbers(board)
        self.draw_finish_line(board)
        if not self.create_key:
            self.draw_decrypt_info(board)

    def create_public_key(self, user_name, board_column):
        self.create_key = True
        board = self.create_board(
            board_x=SCREEN_SIZE[0] / 7,
            board_y=100,
            board_w=board_column * COLUMN_WIDTH + COLUMN_SPACE * (board_column - 1) + BORDER_BOARD * 2,
            board_h=500,
            column=board_column
        )
        self.board_column = board_column
        self.bottom_array = [0] * board_column
        self.private_key = pregenerate_private_keys(board_column)
        # afficher les elements sur lequelle sera posé la boite de dialogue
        self.display_interface(board, user_name, 0)
        text = "Here is your private key, use the keys LEFT and RIGHT to manipulate it according to your desire. " \
               "Press UP or SPACE to invert your key and when you are ready, press DOWN to confirm your choice. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        text = "To generate your public key, drop your private key six or seven times. If the security level is " \
               "sufficient, your public key will be saved, otherwise the computer will complete it. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        clock = pygame.time.Clock()
        current_time = 0
        while self.game.running and self.game.curr_menu.run_display and self.state:
            self.check_input(board, user_name, current_time)
            self.display_interface(board, user_name, current_time)
            if self.counter > 7:
                self.state = False
            pygame.display.flip()
            current_time = pygame.time.get_ticks()
            clock.tick(60)
        if not self.state:
            text = "Congratulations, you understood how it works!"
            self.game.ui.dialog(
                "RESEARCHER",
                text,
                self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
                self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
            )
            text = "Perfect! Here you are, ready! I have your public key, we can move on."
            self.game.ui.dialog(
                "RESEARCHER",
                text,
                self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
                self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
            )
        self.public_key = self.bottom_array
        self.state = True

    def decrypt_my_message(self, user_name, board_column):
        self.create_key = False
        board = self.create_board(
            board_x=50,
            board_y=100,
            board_w=board_column * COLUMN_WIDTH + COLUMN_SPACE * (board_column - 1) + BORDER_BOARD * 2,
            board_h=500,
            column=board_column
        )
        self.board_column = board_column
        self.private_key = pregenerate_private_keys(board_column)
        text = "Here is the message I encrypted using your public key, to decrypt it you have to use your private " \
               "key. Manipulate your key like everything else with LEFT and RIGHT to move the columns and UP or SPACE" \
               " to invert the colors of the blocks. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        text = "When you press DOWN your key is sent to the message to decrypt and the blocks will cancel if they are" \
               " opposite colors or stack if they are the same color. The message is decrypted when you have only one" \
               " row of blocks down. Your turn ! "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        self.game_core(board, user_name)

    def game_core(self, board, user_name):
        self.init_battle()
        clock = pygame.time.Clock()
        current_time = 0
        while self.game.running and self.game.curr_menu.run_display and not self.is_message_decypted():
            self.check_input(board, user_name, current_time)
            self.display_interface(board, user_name, current_time)
            pygame.display.flip()
            current_time = pygame.time.get_ticks()
            clock.tick(60)

        if self.is_message_decypted():
            text = f"You decrypted the message: {self.message}"
            self.game.ui.dialog(
                "RESOLVE !!",
                text,
                self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
                self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
                image=self.game.ressources["message_decript"]
            )
        self.counter = 0

    def play_vs_ia(self, user_name, board_column):
        self.create_key = False
        board = self.create_board(
            board_x=50,
            board_y=100,
            board_w=board_column * COLUMN_WIDTH + COLUMN_SPACE * (board_column - 1) + BORDER_BOARD * 2,
            board_h=500,
            column=board_column
        )
        self.board_column = board_column
        self.bottom_array = [0] * board_column
        self.private_key = pregenerate_private_keys(board_column)
        self.public_key = crypto.generated_public_key(
            self.board_column, self.private_key, REPEAT_GEN_PUBLIC_KEY[self.board_column])
        self.game_core(board, user_name)

    def is_message_decypted(self):
        test = True
        for i in self.bottom_array:
            if i not in [-1, 0, 1]:
                test = False
                break
        return test

    def init_battle(self):
        random.shuffle(MESSAGE[self.board_column])
        self.message = MESSAGE[self.board_column][random.randint(0, len(MESSAGE[self.board_column])-1)]
        message = crypto.string_to_ternary(self.message)
        self.bottom_array = encode_message(self.board_column, message, self.public_key, self.private_key)

    def check_input(self, board, user_name, game_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                self.game.curr_menu.run_display = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.curr_menu.run_display = False
                    return
                if event.key == pygame.K_LEFT:
                    self.private_key = crypto.toggle_key_to_left(self.private_key)
                if event.key == pygame.K_RIGHT:
                    self.private_key = crypto.toggle_key_to_right(self.private_key)
                if event.key == pygame.K_UP:
                    self.private_key = crypto.inverse_key(self.private_key)
                if event.key == pygame.K_DOWN:
                    private_key = self.private_key.copy()
                    self.move_key_down(board, self.private_key, self.bottom_array, user_name, game_time=game_time)
                    self.private_key = private_key
                    self.counter += 1

    def display_interface(self, board: Board, user_name: str, current_time: int):
        self.display_game_items(start_x=board.x + board.w + 250, start_y=100, create_key=self.create_key,
                                current_time=current_time)
        self.draw_player_board(board, user_name)

    def move_key_down(self, board: Board, top_array: list, bottom_array: list, user_name: str, game_time: int):
        incr = 0
        count = []
        clock = pygame.time.Clock()
        current_time = 0
        old_time = 0
        board.move = False
        while len(count) < board.column and self.game.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.running = False
                    self.game.curr_menu.run_display = False
                    break

            if current_time - old_time > 30:
                incr += BLOCK_HEIGTH
                old_time = current_time
                board.move = True
            for i in collision_test(top_array, bottom_array, board, incr):
                if i not in count:
                    count += [i]
            if board.move:
                # reset element on the screen
                self.display_interface(board, user_name, game_time)

            self.draw_blocks(board, top_array, lambda _: board.y + BORDER_BOARD + incr)

            self.draw_blocks(board, bottom_array,
                             lambda pos: board.y + board.h - BORDER_BOARD - abs(bottom_array[pos]) * BLOCK_HEIGTH - (
                                     abs(bottom_array[pos]) - 1) * BLOCK_SPACE)

            current_time = pygame.time.get_ticks()
            pygame.display.flip()
            clock.tick(60)
        board.move = False

    def draw_board(self, board: Board, color: tuple):
        board_surf = pygame.Surface((board.w, board.h), pygame.SRCALPHA)
        board_surf.fill(color)
        self.game.screen.window.blit(board_surf, (board.x, board.y))
        lcd_position = (board.x, board.y - self.game.ressources["lcd_board_game_big"].get_rect().height - 10)
        self.game.screen.window.blit(
            self.game.ressources["lcd_board_game_big"],
            lcd_position
        )
        self.game.screen.window.blit(
            self.game.ressources["key_priv_left"],
            (board.x + board.w - 10, board.y)
        )
        key_chain = pygame.transform.rotate(self.game.ressources["key_priv_keychain_left"], -45)
        self.game.screen.window.blit(
            key_chain,
            (
                board.x + board.w - 10 + self.game.ressources["key_priv_left"].get_rect().w / 2 - 5,
                board.y + self.game.ressources["key_priv_left"].get_rect().h / 3
            )
        )
        self.draw_columns(board)

    def draw_columns(self, board: Board):
        start_column_x = board.x + BORDER_BOARD
        start_column_y = board.y + BORDER_BOARD
        for i in range(board.column):
            rect = pygame.Surface((COLUMN_WIDTH, board.h - 20), pygame.SRCALPHA)
            rect.fill((0, 113, 187, 100))
            self.game.screen.window.blit(rect, (start_column_x, start_column_y))
            start_column_x += COLUMN_SPACE + COLUMN_WIDTH

    def draw_finish_line(self, board: Board):
        dashed_line_y = board.y + board.h - BORDER_BOARD - 10 - BLOCK_SPACE / 2
        self.game.ui.draw_dashed_line(self.game.screen.window, (0, 255, 0), (board.x, dashed_line_y),
                                      (board.x + board.w, dashed_line_y))

    def print_user_name(self, board: Board, user_name: str):
        font = pygame.font.Font(self.game.ressources["font_geo_regular"], 24)
        text_surface = font.render(user_name, True, (0, 255, 0))
        # render at position stated in arguments
        self.game.screen.window.blit(text_surface, (
            board.x + 40, board.y - self.game.ressources["lcd_board_game_big"].get_rect().height
        ))

    def draw_blocks(self, board: Board, array: list, y_sliding):
        block_w = COLUMN_WIDTH
        first_block_x = board.x + BORDER_BOARD
        for i in range(len(array)):
            color = Color.BLEU_AZUR.value if array[i] < 0 else Color.BLEU_CLAIR.value if array[i] > 0 else None
            first_block_y = y_sliding(i)
            for _ in range(abs(array[i])):
                if first_block_y >= board.y + BORDER_BOARD:
                    rect = pygame.Surface((block_w, BLOCK_HEIGTH), pygame.SRCALPHA)
                    rect.fill(color)
                    self.game.screen.window.blit(rect, (first_block_x, first_block_y))
                first_block_y += BLOCK_SPACE + BLOCK_HEIGTH
            first_block_x += COLUMN_SPACE + COLUMN_WIDTH

    def draw_all_blocks(self, board: Board):
        if not board.move:
            self.draw_blocks(board, self.private_key, lambda i: board.y + BORDER_BOARD)
        self.draw_blocks(board, self.bottom_array,
                         lambda i: board.y + board.h - BORDER_BOARD - abs(self.bottom_array[i]) * BLOCK_HEIGTH - (
                                 abs(self.bottom_array[i]) - 1) * BLOCK_SPACE)

    def draw_numbers(self, board: Board):
        font = pygame.font.Font(self.game.ressources["font_incosolata_regular"], 16)
        first_number_pos_y = board.y + board.h + 5
        count = 0
        for i in self.bottom_array:
            text_surface = font.render(f"{i}", True, (0, 255, 0))
            # render at position stated in arguments
            first_number_pos_x = board.x + BORDER_BOARD + count * COLUMN_WIDTH + (count - 1) * COLUMN_SPACE
            self.game.screen.window.blit(
                text_surface, (
                    first_number_pos_x + COLUMN_WIDTH / 2 - text_surface.get_rect().w / 2 + 5,
                    first_number_pos_y
                )
            )
            count += 1

    def draw_decrypt_info(self, board: Board):
        begin_x = board.x + BORDER_BOARD
        pseude_crypted = crypto.easy_crypt(self.bottom_array)
        decrypted = crypto.easy_decrypt(pseude_crypted)
        for i in range(0, len(self.bottom_array), NUMBER_DIGIT):
            if len(self.bottom_array) - i >= NUMBER_DIGIT:
                decode_rect_w = self.draw_decrypt_rectangle(
                    board, NUMBER_DIGIT, begin_x, Color.GREEN.value, decrypted[i // NUMBER_DIGIT])
                begin_x += COLUMN_SPACE + decode_rect_w
            else:
                remind_number = len(self.bottom_array) - i
                self.draw_decrypt_rectangle(board, remind_number, begin_x, Color.GRAY.value, "...")

    def draw_decrypt_rectangle(self, board: Board, size: int, begin_x: int, color: tuple, letter: str):
        border = 5
        decode_rect = pygame.Surface((COLUMN_WIDTH * size + COLUMN_SPACE * (size - 1), 30),
                                     pygame.SRCALPHA)
        decode_rect.fill(color)
        decode_rect_inside = pygame.Surface((
            decode_rect.get_rect().w - border * 2, decode_rect.get_rect().h - border * 2), pygame.SRCALPHA)
        decode_rect_inside.fill(Color.BLACK.value)
        decode_rect_y = board.y + board.h + 25
        self.game.screen.window.blit(decode_rect, (
            begin_x, decode_rect_y
        ))
        self.game.screen.window.blit(decode_rect_inside, (
            begin_x + border, decode_rect_y + border
        ))
        self.game.ui.draw_text(
            letter,
            20,
            begin_x + border + decode_rect_inside.get_rect().w / 2,
            decode_rect_y + border + decode_rect_inside.get_rect().h / 2,
            "font_incosolata_regular",
            color
        )
        return decode_rect.get_rect().w


def collision_test(top_array, bottom_array, board, incr) -> list:
    test = []
    for i in range(board.column):
        block_top_y = board.y + BORDER_BOARD + \
                      abs(top_array[i]) * BLOCK_HEIGTH + (abs(top_array[i]) - 1) * BLOCK_SPACE + incr
        block_bottom_y = board.y + board.h - BORDER_BOARD - abs(bottom_array[i]) * BLOCK_HEIGTH - (
                abs(bottom_array[i]) - 1) * BLOCK_SPACE
        if block_bottom_y - block_top_y < 10:
            bottom_array[i] += top_array[i]
            top_array[i] = 0
            test += [i]
    return test
