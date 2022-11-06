import pygame

from cryptris.constantes import Color


class NewGameScene:
    def __init__(self, game):
        self.game = game

    def play_new_game(self):
        self.start_entry_animation()
        self.start_entry_dialog()
        user_name = self.game.ui.display_text_input()
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
        self.dialog_after_name_given(user_name)
        # create public key
        self.game.gameplay.create_public_key(user_name, board_column=8)
        self.after_public_key_created()
        # decrypt first message
        self.game.gameplay.decrypt_my_message(user_name, board_column=8)
        self.after_first_message_decrypt(user_name)

    def start_entry_animation(self):
        self.game.screen.window.fill(Color.BLACK.value)
        self.game.ui.draw_text(text="You are an intern in a research team at CWI_", size=32,
                               center_x=self.game.screen.width / 2 - 40,
                               center_y=self.game.screen.height / 2 - 16,
                               font_name="font_quantico_bold", color=Color.WHITE.value,
                               )
        pygame.display.flip()
        clock = pygame.time.Clock()
        current_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - current_time < 3000:
            clock.tick(60)
        self.game.screen.window.fill(Color.BLACK.value)
        self.game.ui.draw_text(text="First day at the institute_", size=32,
                               center_x=self.game.screen.width / 2 - 40,
                               center_y=self.game.screen.height / 2 - 16,
                               font_name="font_quantico_bold", color=Color.WHITE.value,
                               )
        pygame.display.flip()
        current_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - current_time < 3000:
            clock.tick(60)
        # remove event, cause the user can be impatient
        for _ in pygame.event.get():
            pygame.event.clear()

    def start_entry_dialog(self):
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
        self.game.screen.window.blit(self.game.ressources["background_institut"], (0, 0))
        text = "Welcome to the Institute! So you're my new intern, perfect! Let's start at the beginning, " \
               "you will need a user account to connect to the network, you just have to choose your username."
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
        pygame.display.flip()

    def dialog_after_name_given(self, user_name):
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
        self.game.screen.window.blit(self.game.ressources["background_institut"], (0, 0))
        text = f"Perfect < {user_name} >, your account is now created. In order to secure the exchanges " \
               f"on the network, we use an asymmetric cryptography protocol. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        pygame.display.flip()
        text = "You are now going to create your private key / public key pair but ... do not forget, this private " \
               "key is ... private! You alone must know it! Your public key will be disseminated on the network to " \
               "all the researchers of the Institute. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        pygame.display.flip()
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return

    def after_public_key_created(self):
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
        self.game.screen.window.blit(self.game.ressources["background_institut"], (0, 0))
        text = "Perfect! Here you are, ready! I have your public key ... Let's check everything works. I send you a " \
               "first encrypted message. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        pygame.display.flip()
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return

    def after_first_message_decrypt(self, user_name):
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
        self.game.screen.window.blit(self.game.ressources["background_institut"], (0, 0))
        text = "Perfect! You understood how to decrypt a message using your private key, I did not expect any less of" \
               " you! You're ready and you're now a member of the Institute. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        pygame.display.flip()
        text = "It's weird, the server has reported a failure, I have to go to the machine room to check that " \
               "everything is in order. You will have to plug or unplug some cables. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        pygame.display.flip()
        text = f"{user_name}! Do you receive me? It's really weird, our server stubbornly refuses to re-configure " \
               f"itself and prevents me from getting out of the room of the machines. Try to unplug the nr.42 cable " \
               f"from the main electrical board. "
        self.game.ui.dialog(
            "RESEARCHER",
            text,
            self.game.screen.width / 2 - self.game.dialog_size[0] / 2,
            self.game.screen.height / 2 - self.game.dialog_size[1] / 2,
        )
        pygame.display.flip()
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
