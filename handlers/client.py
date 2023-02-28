from aiogram import types, Dispatcher

from VapeConfig.create import bot

from keyboards.client_kb import kb_client



# @dp.message_handler(commands=["start_kb"])
async def start_kb(message: types.Message):
    await bot.send_message(message.from_user.id,"Бот запустил конопки", reply_markup=kb_client)



# @dp.message_handler(commands=["hello"])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id,text="Меня зовут бот телеграм, спасибо что пользуетесь мной!)")


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>Добро пожалвать!</em>
"""

# @dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML",
                           )



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(start_kb, commands=["start_kb"])
    dp.register_message_handler(start_command, commands=["hello"])
    dp.register_message_handler(help_command, commands=["help"])

