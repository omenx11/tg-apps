from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7820216850:AAHW3HqfkLH3hc4euNFnNx5-q48_XoD9qt8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://omenx11.github.io/tg-apps/index.html')))
    await message.answer('Привет, мой друг!', reply_markup=markup)



executor.start_polling(dp)