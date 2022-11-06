import pathlib
import random
from enum import Enum

# size of the window game
SCREEN_SIZE = (1250, 680)

# Character that program can manage
BOARD_SYMBOLS = " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ;.,!?&#'\\\"()+-*/|□"


# Color Enum
class Color(Enum):
    BLEU_AZUR = (0, 145, 187)
    BLEU_CLAIR = (173, 216, 230)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLEU_AZUR_ALPHA = (0, 113, 187, 64)
    GREEN = (0, 255, 0)
    GRAY = (229, 229, 229)


# define border of the board
BORDER_BOARD = 10

# define column propety on the board
COLUMN_WIDTH = 40
COLUMN_SPACE = 10
BLOCK_SPACE = 4
BLOCK_HEIGTH = 10
NUMBER_DIGIT = 4

# primary keys predefine for facilite game and avoid frustration
PRIVATE_KEYS = {
    8: [7, 1, -1, -1, 0, 0, 0, 0],
    10: [11, 1, 1, -1, -2, -1, 0, 0, 0, 0],
    12: [15, 1, 2, 1, -1, -2, -1, -1, 0, 0, 0, 0],
    14: [18, 1, 4, 1, 1, -1, -3, -2, -1, -1, 0, 0, 0, 0],
    16: [19, 1, 5, 1, 1, 1, -1, -4, -2, -1, -1, -1, 0, 0, 0, 0],
}

REPEAT_GEN_PUBLIC_KEY = {
    8: 6,
    10: 7,
    12: 8,
    14: 9,
    16: 10
}

REPEAT_ENCODE_MESSAGE = {
    8: 7,
    10: 8,
    12: 9,
    14: 10,
    16: 11
}

MESSAGE = {
    8: [
        "24", "OK", "AH", "JI", "MI", "LO", "la", "ce", "SR", "NS"
    ],
    10: [
        "DO", "RE", "MI", "FA", "SO", "LA", "SI", "PO"
    ],
    12: [
        "LOL", "ICI", "784", "OMO", "DIL", "554", "MAS", "OPs", "lav", "NAL"
    ],
    14: [
        "mri", "msi", "lof", "bof", "iss", "she", "ole", "rim", "mil", "izi"
    ],
    16: [
        "nana", "popo", "7946", "paul", "malo", "boom", "dark", "osis", "jino"
    ]
}


# Just a function to shuffle a private key
def pregenerate_private_keys(nb):
    key = PRIVATE_KEYS[nb]
    random.shuffle(key)
    return key.copy()


# Give a path of the current file, useful if u want to deploy our code like a package game
def get_path(file):
    return pathlib.Path(file).parent.resolve()
