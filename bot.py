import telebot
from keyboard import *
from table import Table
from investing import Investing
from category import Category
from connectrequests import NewConnect
from connectselen import GetHtmlPage

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
    elif "вернуться" in text.lower():
        bot.send_message(message.chat.id, "Вы вернулись в начало", reply_markup=start_kb())
    print(f"Сообщение: {text}")

@bot.callback_query_handler(func=lambda call: call.data)
def subcategories(call):
    if type(call) == telebot.types.CallbackQuery:
        try:
            table.set_table(category.get_category()[call.data])
            text_data = table.get_keys_dict()
            table.set_cat(call.data)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию", reply_markup=categories_kb(text_data))
        except:
            table.set_cat(call.data)
            send_result(call, table.get_cat()[-2:])
        print(f"Выбрано: {call.data}")
    else:
        handle_text(call)


def send_result(call, cat):
    info = get_info(*cat)
    bot.send_message(call.message.chat.id, beautify(info), reply_markup=return_kb())

def get_info(cat, subcat):
    url = 'https://ru.investing.com'
    category = Category()
    newconect = NewConnect()
    invest = Investing()
    if category.get_check():
        invest.set_html_page()
        return invest.get_info1(cat, subcat)
    else:
        html_page = newconect.connect(url)
        if html_page:
            invest.set_html_page(html_page=html_page)
            return invest.get_info1(cat, subcat)
        else:
            ghp = GetHtmlPage()
            html_page = ghp.get_sourcepage(url)
            invest.set_html_page(html_page=html_page)
            return invest.get_info1(cat, subcat)

def beautify(res):
    s = ""
    if len(res.keys()) > 1:
        for i in res.keys():
            s += f"\n{i}:\n\n"
            for j in res[i].keys():
                s += f"{j}\n{',   '.join([n for n in res[i][j] if n != ''])}\n\n"
    else:
        for i in res.keys():
            s += i + "\n" + ',   '.join([n for n in res[i] if n != ''])
    return s

print("Бот запущен")
bot.polling(none_stop=True, interval=0)