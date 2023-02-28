from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


b1 = KeyboardButton('/hello')
b2 = KeyboardButton('/help')

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1).add(b2)

