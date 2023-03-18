from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

maiMenu = InlineKeyboardMarkup (row_wight=2)
info = InlineKeyboardButton (text="Реферальная система", callback_data="info")
url = InlineKeyboardButton (text='Перейти на канал', url='https://t.me/asdasd')
maiMenu.insert(info)
maiMenu.insert(url)

mainMenu = InlineKeyboardMarkup (row_wight=2)
info = InlineKeyboardButton (text="Реферальная система", callback_data="info")
mainMenu.insert(info)


startadmin = types.ReplyKeyboardMarkup(resize_keyboard=True) 
console = types.KeyboardButton("Топ реф")
stat = types.KeyboardButton("Стата")
startadmin.add(stat, console)

vivod = types.ReplyKeyboardMarkup()
vivod.row_width=2
vivod.resize_keyboard=True
vivid = types.KeyboardButton("Вывод голды")
nzd = types.KeyboardButton("Назад")
vivod.add(vivid, nzd)

nazad = types.ReplyKeyboardMarkup()
nazad.row_width=2
nazad.resize_keyboard=True
nazd = types.KeyboardButton("Назад")
inv = types.KeyboardButton("Инвентарь")
nazad.add(nazd, inv)

done = types.ReplyKeyboardMarkup()
done.row_width=2
done.resize_keyboard=True
don = types.KeyboardButton("✅ Выполнил")
done.add(don, nazd)

menuMenu = types.ReplyKeyboardMarkup ()
menuMenu.row_width=2
menuMenu.resize_keyboard=True
search = types.KeyboardButton("Получить приз")
profile = types.KeyboardButton("Профиль")
ref = types.KeyboardButton("Реферальная система")
vip = types.KeyboardButton("Выплаты")
kto = types.KeyboardButton("Кто мы?")
menuMenu.add(search, profile, ref, vip, kto)

mMenu = types.ReplyKeyboardMarkup ()
mMenu.row_width=2
mMenu.resize_keyboard=True
utils = types.KeyboardButton("Промокод")
state = types.KeyboardButton("Открыть кейс")
bomber = types.KeyboardButton("Получить читы")
back = types.KeyboardButton("Назад")
mMenu.add(utils, state, bomber, back)

manMenu = types.ReplyKeyboardMarkup(resize_keyboard=True) 
console = types.KeyboardButton("Реферальная система")
manMenu.insert(info)
