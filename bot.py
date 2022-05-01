import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from parser import get_wall
from datetime import date
step = 0.25

bot = Bot(token = '5379398135:AAEawA_-7Y_3YmawDEoIbQS7Sg1d-DHnaIU',parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
@dp.message_handler(commands='start')
async def start_func(message=types.Message):
    # chat_id = message.chat.id
    # buttons = ['Узнать расписание']
    # keyboard =types.ReplyKeyboardMarkup(resize_keyboard = True)
    # keyboard.add(*buttons)
    await message.answer('Для того чтобы узнать расписание, просто напишите день недели')

@dp.message_handler()
async def get_timetable(message:types.Message):
    if message.text=='Пятница' or message.text=='пятница':
        day = 'пятницу'
    elif message.text=='Среда' or message.text=='среда':
        day = 'среду'
    elif message.text=='Четверг' or message.text=='четверг':
        day = 'четверг'
    elif message.text=='Понедельник' or message.text=='понедельник':
        day = 'понедельник'
    elif message.text=='Вторник' or message.text=='вторник':
        day = 'вторник'
    else:
        day=''
        await message.answer('Вы неправильно ввели день недели')
    if day!='':
        photos=get_wall(day)
        if photos!='Расписание еще не выложили':
            await message.answer_photo(photos,caption=f'Расписание на {day}')
        else:
            await message.answer('Расписание еще не выложили')
def main():
    executor.start_polling(dp)
if __name__=='__main__':
    main()
#@Standoff2_gold_clickBot
#GOLDADLGSO2BOT