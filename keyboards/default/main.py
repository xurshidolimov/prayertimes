from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🕋 Bugungi namoz vaqtlari"), KeyboardButton(text="🗓 Haftalik namoz vaqtlari")],
        [KeyboardButton(text="📍 Hududni o'zgartirish")]
    ], resize_keyboard=True
)


city = ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text="Toshkent"),
        KeyboardButton(text="Andijon"),
        KeyboardButton(text="Farg'ona"),
        KeyboardButton(text="Qo'qon"),
        ],
        [
        KeyboardButton(text="Qarshi"),
        KeyboardButton(text="Termiz"),
        KeyboardButton(text="Navoiy"),
        KeyboardButton(text="Guliston"),
        ],
        [
        KeyboardButton(text="Nukus"),
        KeyboardButton(text="Buxoro"),
        KeyboardButton(text="Xiva"),
        KeyboardButton(text="Zarafshon"),
        ],
        [
        KeyboardButton(text="Jizzax"),
        KeyboardButton(text="Samarqand"),
        KeyboardButton(text="Namangan"),
        ],
    ], resize_keyboard=True
)