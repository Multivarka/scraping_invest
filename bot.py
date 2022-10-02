import telebot
from keyboard import *
from category import Category
from table import Table

bot = telebot.TeleBot("5798314965:AAEYaSNzhVzWC-ZEHISch3xPhmQkh3U784A")
category = Category()
table = Table()


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, нажми 'Начать' чтобы получить информацию", reply_markup=start_kb())

@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text
    if "начать" in text.lower():
        table.set_table(category.get_category())
        msg = bot.send_message(message.chat.id, "Выберите категорию", reply_markup=categories_kb(table.get_table()))
        bot.register_next_step_handler(msg, subcategories)
    print(f"Сообщение: {text}")

@bot.callback_query_handler(func=lambda call: call.data)
def subcategories(call):
    try:
        table.set_table(category.get_category()[call.data])
        text_data = table.get_keys_dict()
        bot.send_message(call.message.chat.id, "Выберите подкатегорию", reply_markup=categories_kb(text_data))
    except:
        send_result(call, table.get_table())

def send_result(call, table):
    bot.send_message(call.message.chat.id, f"{call.data}: {table[call.data]}")

bot.polling(none_stop=True, interval=0)