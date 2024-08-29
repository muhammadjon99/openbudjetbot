from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

bottoken = '7101094041:AAH5GFfuiSnyf-72s2hoBTXgY1tXyDBQJAE'
bot = Bot(bottoken)
dp = Dispatcher(bot)

knopka = InlineKeyboardMarkup()
knopka.add(
    InlineKeyboardButton(text='Ovoz berish', url='https://t.me/ochiqbudjet_4_bot?start=048350475011')
)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Botimizga Xush Kelibsiz, Ovoz berish uchun knopkani bosing',
                           reply_markup=knopka)





executor.start_polling(dp, skip_updates=True)