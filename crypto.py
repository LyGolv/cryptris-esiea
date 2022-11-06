# symbol to represent -1 value
import math
import random

from cryptris.constantes import BOARD_SYMBOLS, REPEAT_GEN_PUBLIC_KEY, REPEAT_ENCODE_MESSAGE

symbols1 = "0123456789abcdefghijklmnop"

# symbol to represent 0 value
symbols2 = "qrstuvwxyzABCDEFGHIJKLMNOP"

# symbol to represent 1 value
symbols3 = "QRSTUVWXYZ"


# pseudo scripting fonction
# message is represent by {-1, 0, 1} in a list
def easy_crypt(message) -> str:
    """
    This is a pseudo crypting function
    This function generate a random message base on the key encoded by public key
    :param message:
    :return:
    """
    crypt_message = ""
    for nb in message:
        crypt_message += symbols1[math.floor(random.random() * len(symbols1))] if nb == -1 \
            else symbols2[math.floor(random.random() * len(symbols2))] if nb == 0 \
            else symbols3[math.floor(random.random() * len(symbols3))]
    return crypt_message


def easy_decrypt(crypt_message) -> str:
    """
    Decrypt message encode by easy_crypt method and return an original message
    :param crypt_message:
    :return:
    """
    ternary_message = []
    for c in crypt_message:
        for char in symbols1:
            if c == char:
                ternary_message += [-1]
                break
        for char in symbols2:
            if c == char:
                ternary_message += [0]
                break
        for char in symbols3:
            if c == char:
                ternary_message += [1]
                break
    message = ""
    count = 0
    while len(ternary_message) % 4 != 0:
        count += 1
        ternary_message += [0]
    for i in range(0, len(ternary_message), 4):
        message += ternary_to_symbol(ternary_message[i], ternary_message[i + 1], ternary_message[i + 2],
                                     ternary_message[i + 3])

    return message


def positive_modulo(x1, nbr) -> int:
    """
    Return a modulo of "x1" base on "nbr"
    :param x1:
    :param nbr:
    :return:
    """
    return ((x1 % nbr) + nbr) % nbr


# Helper shortcut
pm = positive_modulo


def ternary_to_symbol(x1, x2, x3, x4):
    """
    Return a symbol contain in "board_symbol"
    cause number is represent by four ternary digit which means
    that we can have 3^4 = 3*3*3*3 = 81 symbols
    So to determines position of one symbol, take reverse path use
    in function "symbol_to_ternary".
    :param x1:
    :param x2:
    :param x3:
    :param x4:
    :return:
    """
    i = pm(x1, 3) + 3 * pm(x2, 3) + 9 * pm(x3, 3) + 27 * pm(x4, 3)
    return BOARD_SYMBOLS[i]


def integer_mod3_to_ternary(x) -> int:
    y = pm(x, 3)
    return -1 if y == 2 else y


i3t = integer_mod3_to_ternary


# convert letter to its ternary representation
def symbol_to_ternary(s) -> list:
    """
    Convert symbol and return its ternary representation
    :param s:
    :return:
    """
    i = BOARD_SYMBOLS.index(s)
    x1 = pm(i, 3)
    i = (i - x1) / 3
    x2 = pm(i, 3)
    i = (i - x2) / 3
    x3 = pm(i, 3)
    i = (i - x3) / 3
    x4 = pm(i, 3)
    return [i3t(x1), i3t(x2), i3t(x3), i3t(x4)]


# convert the whole string to the ternary representation
def string_to_ternary(string: str) -> list:
    """
    Give a ternary representation base on string parameter
    :param string:
    :return:
    """
    html_string = string
    ternaries = []
    for c in html_string:
        ternary = symbol_to_ternary(c)
        for ter in ternary:
            ternaries.append(ter)
    return ternaries


def toggle_key_to_left(key: list) -> list:
    return key[1:] + [key[0]]


def toggle_key_to_right(key: list) -> list:
    return [key[-1]] + key[0:-1]


def inverse_key(key: list) -> list:
    return [-1 * nb for nb in key]


def l2(v):
    result = 0
    for i in v:
        result += i ** 2
    return result


def cal_score(public_key: list):
    max_pk = max(public_key)
    min_pk = min(public_key)
    t = max(min_pk * min_pk, max_pk * max_pk)
    distance = l2(public_key)
    return 0 if t == 0 else distance / t


# "Rotate" columns to the left (i) times
# According to the size (dim) of the current board
def rotate(array: list, i: int):
    return array[i:] + array[0:i]


def mult(a: int, array: list):
    return [a * i for i in array]


def sum_list(array_1: list, array_2: list):
    return [array_1[i] + array_2[i] for i in range(len(array_1))]


def generated_public_key(column, private_key: list, repeat):
    public_key = private_key.copy()
    for i in range(repeat):
        k = math.floor(random.random() * (column + 1))
        r = -1
        if math.floor(random.random() * 2) == 1:
            r = 1
        public_key = sum_list(public_key, mult(r, rotate(private_key, k)))
        return public_key


def encode_message(column: int, message: list, public_key: list, private_key: list) -> list[int]:
    # cipher
    cipher = message.copy()
    # if the message is not multiple of column, we are going to add it some padding
    while len(cipher) % column != 0:
        cipher += [0]
    # check if our public_key is empty or not
    while sum(public_key) == 0:
        public_key = generated_public_key(column, private_key, REPEAT_GEN_PUBLIC_KEY[column])

    # crypt the message
    right = r = 1
    left = 0
    invert = 2
    down = 3
    key_hidden = 4
    move = []
    last_k = 0
    test_crypted = False
    while not test_crypted:
        for i in range(REPEAT_ENCODE_MESSAGE[column]):
            k = math.floor(random.random() * (column + 1))
            latteral_move = k - last_k
            if latteral_move > 0:
                for z in range(latteral_move):
                    move += [left]
            else:
                latteral_move *= -1
                for z in range(latteral_move):
                    move += [right]
            if math.floor(random.random() * 2) == 1:
                r *= -1
                move += [invert]
            cipher = sum_list(cipher, mult(r, rotate(private_key, k)))

            if i == REPEAT_ENCODE_MESSAGE[column] - 1:
                move += [key_hidden]
            move += [down]
            last_k = k
        # validate if the message has been crypted
        for i in range(len(cipher)):
            if cipher[i] > 1 or cipher[i] < -1:
                test_crypted = True
                break

    return list(map(int, cipher))
