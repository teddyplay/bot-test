from aiogram import executor

from VapeConfig.create import dp
from handlers import admin, other, client


async def on_startup(_):
    print("Бот был успешно запущен!")


client.register_handlers_client(dp)
other.register_handlers_other(dp)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

