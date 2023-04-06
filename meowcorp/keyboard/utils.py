from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from meowcorp.exceptions.keyboard import *


def create_keyboard(buttons: list, rows: list = None) -> ReplyKeyboardMarkup:
    if rows is None:
        rows = [1] * len(buttons)

    if len(buttons) != sum(rows):
        raise BadButtonsAmount(f"Bad amount of button. Button: {len(buttons)}, rows: {sum(rows)}")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    new_buttons = [KeyboardButton(x) for x in buttons]

    index = 0
    for amount in rows:
        keyboard.row(*new_buttons[index: index + amount])
        index += amount

    return keyboard


def create_inline_keyboard(buttons: list, rows: list = None) -> InlineKeyboardMarkup:
    if rows is None:
        rows = [1] * len(buttons)

    if len(buttons) != sum(rows):
        raise BadButtonsAmount(f"Bad amount of button. Button: {len(buttons)}, rows: {sum(rows)}")

    keyboard = InlineKeyboardMarkup()
    new_buttons = []
    for x in buttons:
        if isinstance(x, str) or isinstance(x, int):
            new_buttons.append(InlineKeyboardButton(str(x), callback_data=str(x)))
        elif isinstance(x, list) and len(x) == 1:
            new_buttons.append(InlineKeyboardButton(x[0], callback_data=' '))
        else:
            new_buttons.append(InlineKeyboardButton(x[0], callback_data=x[1]))

    index = 0
    for amount in rows:
        if not amount:
            continue
        keyboard.row(*new_buttons[index: index + amount])
        index += amount

    return keyboard
