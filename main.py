from aiogram import Bot, Dispatcher, executor, types
import wikipedia
from deep_translator import GoogleTranslator


bot = Bot(token='6074500148:AAGvYEZZGZZWWbCRjBpxVJ82YFBu4N1zQRc')
dp = Dispatcher(bot)
wikipedia.set_lang('en')


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Salom siz siz Stady_hack tomonidan yaratilgan botni ishga tushirdingiz")


@dp.message_handler(commands=['Stady_Hack'])
async def Me(message: types.Message):
    await message.reply("FarPI  🏛   \n Energetika Fakulteti 2 kurs talabasi  👨‍🎓 \n  Solijonov O`lmasxo`ja 👨‍💻  ")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:

        one = GoogleTranslator(source='uz', target='en').translate(message.text)
        respond = wikipedia.summary(one)
        await message.answer(GoogleTranslator(source='en', target='uz').translate(respond))
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

