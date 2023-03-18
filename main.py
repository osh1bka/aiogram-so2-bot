from aiogram import Bot, types, asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import keyboard
import func
import time
import fileinput
import sqlite3 as sql
import random
from aiogram.utils.markdown import hlink
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled

captcha = ''
for x in range(4):
  captcha = captcha + random.choice(list('123456789'))

TOKEN='token' #токен бота
bot = Bot(TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
adminid = 600257122 #админ ид
link = "link" # юзернейм бота, пример – freegoldsbot (писать без @ и без https://t.me просто юзернейм)
error = "error" # канал с фейк ошибками в работе бота
viplat = "viplat" # канал с фейк выплатами
async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Не флуди! Попробуй через 3 секунды!")
class meinfo(StatesGroup):
    Q1 = State()
    Q2 = State()
    Q3 = State()

@dp.message_handler(Command("promo"), state=None)
async def enter_meinfo(message: types.Message):
    if message.chat.id == adminid:               
        await message.answer("Введи текст для раздела промокодов")

        await meinfo.Q3.set()
@dp.message_handler(state=meinfo.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer3=answer)
    await message.answer("Сохранил")
    data = await state.get_data()                #
    answer3 = data.get("answer3")

    joinedFile = open("promo.txt","w", encoding="utf-8")
    joinedFile.write(str(answer3))

    await message.answer(f'Ваш текст: {answer3}')
 
    await state.finish()

@dp.message_handler(Command("cheats"), state=None)
async def enter_meinfo(message: types.Message):
    if message.chat.id == adminid:               
        await message.answer("Введи текст для раздела с читами")

        await meinfo.Q1.set()

@dp.message_handler(state=meinfo.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)
    await message.answer("Сохранил")
    data = await state.get_data()                #
    answer1 = data.get("answer1")

    joinedFile = open("cheats.txt","w", encoding="utf-8")
    joinedFile.write(str(answer1))

    await message.answer(f'Ваш текст: {answer1}')
 
    await state.finish()
    
@dp.message_handler(commands=["start"])
async def welcome(message):
    if ' ' in message.text and message.chat.id!=message.text[7:]:
        info=func.user(message.chat.id)
        if info is None:
            func.add_ref(message.text[7:])
            await bot.send_message(message.text[7:], f"У вас новый реферал, голда начислится на баланс в течении 12 часов.")
    else:
        info=func.user(message.chat.id)
        if info is None:
            con = sql.connect('users.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS `users` (id INT PRIMARY KEY, Nick TEXT, ref INT)")
                cur.execute(f"INSERT OR IGNORE INTO `users` VALUES ('{message.chat.id}', '{message.from_user.first_name}', {0})")
                media = types.MediaGroup() 
                media.attach_photo(types.InputFile('welcome.jpg'), 'Привет, судя по всему ты хочешь получить нож, или скачать читы на Standoff 2. Перед тем как ты получишь то что хочешь, пройди каптчу.') 
                await bot.send_media_group(message.chat.id, media=media)
                await bot.send_message(message.chat.id, f"*{captcha} \n\nПросто напиши число выше.*", parse_mode='Markdown')
                print ('+1 user')
        elif message.chat.id==60025712:
            await bot.send_message(message.chat.id, f"Привет, *{message.from_user.first_name},*  любимый админ)", reply_markup=keyboard.startadmin, parse_mode='Markdown')
        else:
                await bot.send_message(message.chat.id, f"*Я рад что ты вернулся.*", reply_markup=keyboard.menuMenu, parse_mode='Markdown')

@dp.message_handler(commands=['alert'])
async def alert(message):
    try:
        if message.chat.id==adminid:
            await bot.send_message(message.chat.id, f"*Рассылка началась*", parse_mode='Markdown')
            receive_users, block_users = 0, 0
            spisok=func.spisok()
            for user1 in spisok:
                try:
                    await bot.send_message(user1[0], message.text[message.text.find(' '):])
                    receive_users += 1
                except:
                    block_users += 1
                await asyncio.sleep(0.4)
            await bot.send_message(message.chat.id, f"*Рассылка завершена *\n"
                                                    f"Сообщение получили: *{receive_users}*\n"
                                                    f"Сообщение не получили: *{block_users}*", parse_mode='Markdown')
    except Exception as e:
        print('Ошибка 1', e)

@dp.message_handler(commands=['admin'])
async def apanel(message):
  if message.chat.id==adminid:
    await bot.send_message(message.chat.id, f"*Лови APANEL*", reply_markup=keyboard.startadmin, parse_mode='Markdown')

@dp.message_handler(content_types=['text'])
async def get_message(message):
    if message.text == "Топ реф" and message.chat.id==adminid:
        top=func.top()
        await message.answer(text = f"{top}", parse_mode='HTML')
    elif message.text == "Реферальная система":
        await message.answer(text = f"Приглошай людей по этой ссылке и получай голду на баланс в боте.\n\nВаша реферальная ссылка: "+'https://t.me/freagoldso2bot?start='+str(message.chat.id), parse_mode='HTML')
    if message.text == f"{captcha}":
       await message.answer('Ты успешно прошёл каптчу. 🥳 \n\nТеперь ты можешь получить свой нож в Standoff 2, или скачать читы.', parse_mode='Markdown')
       await message.answer('⏬ Регестрирую тебя в программе. \n\n10%', parse_mode='Markdown')
       await asyncio.sleep(2)
       await message.answer('⏬ Генирирую ссылку на чит. \n\n30%', parse_mode='Markdown')
       await asyncio.sleep(2)
       await message.answer('⏬ Получаю промокод из базы данных. \n\n50%', parse_mode='Markdown')
       await asyncio.sleep(2)
       await message.answer('⏬ Закупаю скины для передачи голды. \n\n90%', parse_mode='Markdown')
       await asyncio.sleep(2)
       await message.answer('✅ Успешно, используй меню для выбора раздела. \n\n100%', reply_markup=keyboard.menuMenu, parse_mode='Markdown')
    if message.text == "Мои рефералы":
        ref=func.ref()
        await message.answer(text = f"{ref}", parse_mode='HTML')
    if message.text == "Получить читы":
        link1 = open('cheats.txt', encoding="utf-8")
        cheats = link1.read()

        await bot.send_message(message.chat.id, text = f"*{cheats}*", parse_mode='Markdown', disable_web_page_preview=True)
    if message.text == "Открыть кейс":
        await bot.send_message(message.chat.id, text = f"⏬ Открытие кейса!\n\n!!!ОТКРЫТЬ КЕЙС МОЖНО ТОЛЬКО 1 РАЗ, В СЛЕДУЮЩИЙ РАЗ БУДЕТ ВЫПАДАТЬ ТО ЖЕ САМОЕ ОРУЖИЕ, НО ИНВЕНТАРЬ ОСТАНЕТСЯ ТАКИМ ЖЕ!!!")
        await asyncio.sleep(2)
        media = types.MediaGroup() 
        media.attach_photo(types.InputFile('case.jpg'), '✅ Ты успешно открыл кейс!\n\nТебе выпал – FAMAS "FURY"') 
        await bot.send_media_group(message.chat.id, media=media)
        await asyncio.sleep(2)
        await bot.send_message(message.chat.id, text = f"✅ Для получения скина, нажми на кнопку ниже!", reply_markup=keyboard.vivod)
    if message.text == "Промокод":
        link1 = open('promo.txt', encoding="utf-8")
        promo = link1.read()

        await bot.send_message(message.chat.id, text = f"*{promo}*", reply_markup=keyboard.done, parse_mode='Markdown', disable_web_page_preview=True)
    if message.text == "Получить приз":
      await bot.send_message(message.chat.id, text = f"*Ты попал в раздел по  получению приза, выбери свой приз!*", reply_markup=keyboard.mMenu, parse_mode='Markdown')
    if message.text == "Назад":
      await bot.send_message(message.chat.id, text = f"*Ты вернулся в главное меню*", reply_markup=keyboard.menuMenu, parse_mode='Markdown')
    if message.text == "Профиль":
      ref = func.ref(message)
      await bot.send_message(message.chat.id, text = f"*Имя: {message.from_user.first_name}\nID: {message.from_user.id}\n\nГолды: {ref}0*", reply_markup=keyboard.vivod, parse_mode='Markdown')
    if message.text == "Инвентарь":
      ref = func.ref(message)
      await bot.send_message(message.chat.id, text = f"*FAMAS 'FURY'\n\nГолды: {ref}0*", reply_markup=keyboard.vivod, parse_mode='Markdown')
    if message.text == "✅ Выполнил":
      await bot.send_message(message.chat.id, text = f"❌ Похоже ты не выполнил одно из условий.\n\nЕсли ты все выполнил, попробуй через 5 минут.")
    if message.text == "Выплаты":
      await bot.send_message(message.chat.id, text = f"✅ Канал с выплатами голды нашим пользователям.\n\n{viplat}")
    if message.text == "Кто мы?":
      await bot.send_message(message.chat.id, text = f"✅ Мы начинающая команда трейдеров.\n\nНаш охват на данный момент, около 300.000 голды.\nВыдали бы более 100.000 голды и более 100 промокодов.")
    if message.text == "Вывод голды":
      await bot.send_message(message.chat.id, text = f"⏬ Получаю голду на баланс бота, для передачи пользователю. 10%")
      await asyncio.sleep(2)
      await bot.send_message(message.chat.id, text = f"⏬ Проверяю баланс пользователя. 30%")
      await asyncio.sleep(2)
      await bot.send_message(message.chat.id, text = f"❌ ERROR #1204 ❌\n\n Ошибка вывода голды.\n\nПопробуйте позже, или найдите решение вашей ошибки тут – {error}", reply_markup=keyboard.nazad)
    if message.text == "Стата" and message.chat.id==adminid:
      users = func.select_all_users()
      await bot.send_message(message.chat.id, text = f"""
📊 Статистика:

👤‍ Пользователей: <b>{users}</b>
   """, parse_mode='HTML')
   
@dp.callback_query_handler(text_contains='info')
async def join(call: types.CallbackQuery):
        await bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text = f"Ваша реферальная ссылка: "+'https://t.me/{link}?start='+str(call.message.chat.id), parse_mode='HTML')
if __name__ == '__main__':
 executor.start_polling(dp)
    