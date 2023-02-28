from aiogram import types, Dispatcher

from VapeConfig.create import dp


@dp.message_handler(commands=["yo"])
async def echo(message: types.Message):
    await message.answer("И тебе привет")



def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo, commands=["yo"])
