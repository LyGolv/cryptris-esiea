class ArcadeScene:
    def __init__(self, game):
        self.game = game

    def create_key_scene(self, user_name):
        self.game.screen.window.blit(self.game.ressources["background"], (0, 0))
        text = "You will create your private key / public key pair but ... do not forget, this private key " \
               "is ... private! You alone must know it! Your public key will be disseminated on the network " \
               "to all the researchers of the Institute. "
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
        self.game.gameplay.create_public_key(user_name, board_column=8)

    def play_create_key_scene(self):
        user_name = self.game.ui.display_text_input()
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
        self.create_key_scene(user_name)

    def play_challenge_scene(self, column):
        user_name = self.game.ui.display_text_input()
        if not self.game.running:
            return
        if not self.game.curr_menu.run_display:
            return
        self.game.screen.window.blit(self.game.ressources["background"], (0, 0))
        text = "If you need help, press the '?' and I will give you all the necessary information."
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
        self.game.gameplay.play_vs_ia(user_name, column)
