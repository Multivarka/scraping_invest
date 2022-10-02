from telebot import types

def start_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Начать")
    markup.add(btn1)
    return markup

def categories_kb(text_data):
    markup = types.InlineKeyboardMarkup()
    for k in text_data:
        button1 = types.InlineKeyboardButton(k, callback_data=k)
        markup.add(button1)
    return markup

def return_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Вернуться")
    markup.add(btn1)
    return markup
