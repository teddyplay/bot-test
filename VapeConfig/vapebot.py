from aiogram import Bot, Dispatcher, executor, types
import string
import random


TOKEN = "5842868047:AAGGjDSh3FWzdTk01txA1rTQtnjefPrcPhg"
bot = Bot(TOKEN)

dp = Dispatcher(bot)


async def on_startup(_):
    print("Бот был успешно запущен!")

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>Добро пожалвать!</em>
<b>/give</b> - <em>отправка сообщения</em>
<b>/картина</b> - <em>отправка фотография</em>
<b>/картина</b> - <em>отправка фотография</em>
<b>location</b> - <em>отправка местоположения</em>
"""

@dp.message_handler(commands=["help"])
async def reply_message(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=HELP_COMMAND, parse_mode="HTML")


@dp.message_handler(commands=["give"])
async def get_heart(message: types.Message):
    await message.reply("Смотри какой котик 🖤")
    await bot.send_sticker(message.chat.id , sticker="CAACAgIAAxkBAAEH61tj_HUGW-93xu3i4UkMVICysQ_rQgACSwADUfywFhwds_v5xTvQLgQ")

@dp.message_handler(content_types=["sticker"])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
    await bot.send_sticker(message.from_user.id , sticker="CAACAgIAAxkBAAPmY_x_MH3jeHLYxPV8w99GXMU02QkAAiUAA1H8sBbysevWLkTmZy4E")


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(text="Меня зовут бот телеграм, спасибо что пользуетесь мной!)")


@dp.message_handler(commands="картина")
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://www.google.com/imgres?imgurl=https%3A%2F%2Fyt3.googleusercontent.com%2FifZJFKoXaasijKlvMxM43d1lXCsvTjJgujLvEWCvv68e8rHKSg2OmixwdRBp_L_50uQBviQOHA%3Ds900-c-k-c0x00ffffff-no-rj&imgrefurl=https%3A%2F%2Fm.youtube.com%2Fc%2FSinsTV%2Fvideos&tbnid=dmKggxhhpwRohM&vet=12ahUKEwi3nt-my7X9AhXGsyoKHajaAVMQMygAegUIARCVAQ..i&docid=le-xNc8nOa7TUM&w=900&h=900&q=johny%20sins&ved=2ahUKEwi3nt-my7X9AhXGsyoKHajaAVMQMygAegUIARCVAQ")



@dp.message_handler(commands="location")
async def send_loc(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=55,
                            longitude=74,
                            )
# @dp.message_handler()
# async def message_give(message: types.Message):
#     await message.reply(text=str(message.text.count("🌟")))



#
#
# @dp.message_handler()
# async def post_heart(message: types.Message):
#     if message.text == '🖤':
#         await message.reply("❤️")
#         await message.delete()




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
    executor.start_polling(dp, skip_updates=True)

