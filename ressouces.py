import pygame

from cryptris.constantes import get_path, SCREEN_SIZE


def load_ressources():
    """
    This function load all ressources that we need to avoid to load them localy\n
    * it return a dictionary whick map name of the ressource and real ressource.
    :return: {}
    """
    current_file_path = get_path(__file__)
    background = pygame.image.load(f"{current_file_path}/img/bg/bg-circuits.png").convert()
    background = pygame.transform.smoothscale(background, SCREEN_SIZE)
    cryptris_board = pygame.image.load(f"{current_file_path}/img/board/cryptris.png").convert_alpha()
    lcd_board_game = pygame.image.load(f"{current_file_path}/img/lcd.png").convert_alpha()
    lcd_board_game_big = pygame.image.load(f"{current_file_path}/img/lcd@2x.png").convert_alpha()
    lcd_board_game_big = pygame.transform.scale(lcd_board_game_big, (240, 50))
    btn_pause_game = pygame.image.load(f"{current_file_path}/img/board/btn-pause.png").convert_alpha()
    btn_pause_game_border = pygame.image.load(f"{current_file_path}/img/board/btn-pause-border.png").convert_alpha()
    btn_interrogation_game = pygame.image.load(f"{current_file_path}/img/board/btn-interrogation.png").convert_alpha()
    btn_interrogation_game_border = pygame.image\
        .load(f"{current_file_path}/img/board/btn-interrogation-border.png")\
        .convert_alpha()
    btn_direction_full = pygame.image\
        .load(f"{current_file_path}/img/board/btn-circle-direction-full.png")\
        .convert_alpha()
    btn_direction_left = pygame.image \
        .load(f"{current_file_path}/img/board/btn-circle-direction-left.png") \
        .convert_alpha()
    btn_direction_right = pygame.image \
        .load(f"{current_file_path}/img/board/btn-circle-direction-right.png") \
        .convert_alpha()
    btn_direction_up = pygame.image \
        .load(f"{current_file_path}/img/board/btn-circle-direction-up.png") \
        .convert_alpha()
    btn_direction_down = pygame.image \
        .load(f"{current_file_path}/img/board/btn-circle-direction-down.png") \
        .convert_alpha()
    logo_cwi = pygame.image \
        .load(f"{current_file_path}/img/logo-cwi.png") \
        .convert_alpha()
    logo_cwi = pygame.transform.smoothscale(logo_cwi, (logo_cwi.get_rect().w/6, logo_cwi.get_rect().h/6))
    logo_cwi_small = pygame.transform.smoothscale(logo_cwi, (logo_cwi.get_rect().w / 2, logo_cwi.get_rect().h / 2))
    logo_inria = pygame.image \
        .load(f"{current_file_path}/img/logo-inria.png") \
        .convert_alpha()
    logo_inria = pygame.transform.smoothscale(logo_inria, (logo_inria.get_rect().w / 2, logo_inria.get_rect().h / 2))
    digital_cuisine = pygame.image \
        .load(f"{current_file_path}/img/digital-cuisine.png") \
        .convert_alpha()
    triangle_left = pygame.image \
        .load(f"{current_file_path}/img/board/triangle-left.png") \
        .convert_alpha()
    triangle_rigth = pygame.image \
        .load(f"{current_file_path}/img/board/triangle-right.png") \
        .convert_alpha()
    key_priv_keychain_left = pygame.image \
        .load(f"{current_file_path}/img/keys/key-priv-keychain-left.png") \
        .convert_alpha()
    key_priv_keychain_right = pygame.image \
        .load(f"{current_file_path}/img/keys/key-priv-keychain-right.png") \
        .convert_alpha()
    key_priv_left = pygame.image \
        .load(f"{current_file_path}/img/keys/key-priv-left.png") \
        .convert_alpha()
    key_priv_right = pygame.image \
        .load(f"{current_file_path}/img/keys/key-priv-right.png") \
        .convert_alpha()
    key_pub_keychain_left = pygame.image \
        .load(f"{current_file_path}/img/keys/key-pub-keychain-left.png") \
        .convert_alpha()
    key_pub_keychain_right = pygame.image \
        .load(f"{current_file_path}/img/keys/key-pub-keychain-right.png") \
        .convert_alpha()
    key_pub_left = pygame.image \
        .load(f"{current_file_path}/img/keys/key-pub-left.png") \
        .convert_alpha()
    key_pub_right = pygame.image \
        .load(f"{current_file_path}/img/keys/key-pub-right.png") \
        .convert_alpha()
    gauge_indetermine = pygame.image \
        .load(f"{current_file_path}/img/gauge/00.png") \
        .convert_alpha()
    gauge_mauvaise = pygame.image \
        .load(f"{current_file_path}/img/gauge/01.png") \
        .convert_alpha()
    gauge_mediocre = pygame.image \
        .load(f"{current_file_path}/img/gauge/02.png") \
        .convert_alpha()
    gauge_faible = pygame.image \
        .load(f"{current_file_path}/img/gauge/03.png") \
        .convert_alpha()
    gauge_correct = pygame.image \
        .load(f"{current_file_path}/img/gauge/04.png") \
        .convert_alpha()
    gauge_bonne = pygame.image \
        .load(f"{current_file_path}/img/gauge/05.png") \
        .convert_alpha()
    gauge_excellente = pygame.image \
        .load(f"{current_file_path}/img/gauge/06.png") \
        .convert_alpha()

    logo_cryptris_large = pygame.image \
        .load(f"{current_file_path}/img/logo/cryptris/logo-cryptris-large.png") \
        .convert_alpha()

    avatar_chercheuse = pygame.image \
        .load(f"{current_file_path}/img/avatar-chercheuse.png") \
        .convert_alpha()

    message_decript = pygame.image \
        .load(f"{current_file_path}/img/avatar-new-message-decrypted.jpg") \
        .convert_alpha()

    background_institut = pygame.image \
        .load(f"{current_file_path}/img/bg-institut.jpg") \
        .convert_alpha()

    # define fonts
    font_geo_oblique = f"{current_file_path}/fonts/geo-oblique.ttf"
    font_geo_regular = f"{current_file_path}/fonts/geo-regular.ttf"
    font_incosolata_regular = f"{current_file_path}/fonts/inconsolata-regular.ttf"
    font_quantico_bold = f"{current_file_path}/fonts/quantico-bold.ttf"

    return {
        "background": background,
        "cryptris_board": cryptris_board,
        "lcd_board_game": lcd_board_game,
        "btn_pause_game": btn_pause_game,
        "btn_pause_game_border": btn_pause_game_border,
        "btn_interrogation_game": btn_interrogation_game,
        "btn_interrogation_game_border": btn_interrogation_game_border,
        "btn_direction_full": btn_direction_full,
        "btn_direction_left": btn_direction_left,
        "btn_direction_right": btn_direction_right,
        "btn_direction_up": btn_direction_up,
        "btn_direction_down": btn_direction_down,
        "lcd_board_game_big": lcd_board_game_big,
        "logo_cwi": logo_cwi,
        "logo_inria": logo_inria,
        "digital_cuisine": digital_cuisine,
        "logo_cwi_small": logo_cwi_small,
        "font_geo_oblique": font_geo_oblique,
        "font_geo_regular": font_geo_regular,
        "font_quantico_bold": font_quantico_bold,
        "triangle_left": triangle_left,
        "triangle_rigth": triangle_rigth,
        "key_priv_keychain_left": key_priv_keychain_left,
        "key_priv_keychain_right": key_priv_keychain_right,
        "key_priv_left": key_priv_left,
        "key_priv_right": key_priv_right,
        "key_pub_keychain_left": key_pub_keychain_left,
        "key_pub_keychain_right": key_pub_keychain_right,
        "key_pub_left": key_pub_left,
        "key_pub_right": key_pub_right,
        "gauge_indetermine": gauge_indetermine,
        "gauge_mauvaise": gauge_mauvaise,
        "gauge_mediocre": gauge_mediocre,
        "gauge_faible": gauge_faible,
        "gauge_correct": gauge_correct,
        "gauge_bonne": gauge_bonne,
        "gauge_excellente": gauge_excellente,
        "font_incosolata_regular": font_incosolata_regular,
        "logo_cryptris_large": logo_cryptris_large,
        "avatar_chercheuse": avatar_chercheuse,
        "message_decript": message_decript,
        "background_institut": background_institut
    }
