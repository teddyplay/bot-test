from aiogram import Bot, Dispatcher, executor, types
import string
import random


TOKEN = "5842868047:AAGGjDSh3FWzdTk01txA1rTQtnjefPrcPhg"
bot = Bot(TOKEN)

dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот был успешно запущен!")



# @dp.message_handler(commands=["start"])
# async def command_start(message: types.Message):
#     await message.reply("<em>Привет <b>добро</b> пожаловать в наш бот!</em>", parse_mode="HTML")
#
#
# @dp.message_handler(commands=["gift"])
# async def command_start(message: types.Message):
#     await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEH61tj_HUGW-93xu3i4UkMVICysQ_rQgACSwADUfywFhwds_v5xTvQLgQ")
#     await message.delete()
#
# @dp.message_handler()
# async def post_emoji(message: types.Message):
#     await message.reply(message.text + "🙂")



# HELP_COMMAND = """
# /help - список команд
# /start - начать работу с ботом
# """
# count = 0
#
# @dp.message_handler()
# async def check(message: types.Message):
#     if "0" in message.text:
#         await message.reply("YES!")
#         await message.delete()
#     else:
#         await message.reply("NO!")
#         await message.delete()
#
#
# @dp.message_handler(commands=["count"])
# async def count_int(message: types.Message):
#     global count
#     await message.reply(f"Count: {count}")
#     count += 1
#
# @dp.message_handler(commands=["description"])
# async def commands(message: types.Message):
#     await message.reply("Данный бот уммет что то там писать и это круто!")
#     await message.delete()
#
#
# @dp.message_handler()
# async def send_random_word(message: types.Message):
#     await message.reply(random.choice(string.ascii_letters))
#
#
#
# @dp.message_handler(commands=["help"])
# async def echo(message: types.Message):
#     # if message.text.count(" ") >= 1:
#     await message.reply(text=HELP_COMMAND)
#     await message.delete()
#
# @dp.message_handler(commands=["start"])
# async def echo(message: types.Message):
#     # if message.text.count(" ") >= 1:
#     await message.answer(text="Добро пожаловать в наш telegram bot")
#     await message.delete()



if __name__ == "__main__":
    executor.start_polling(dp)
