import telebot
import os
from dotenv import load_dotenv
from pytz import timezone
from datetime import datetime

idss =[]
ss = []
tz = timezone("Asia/Kuala_Lumpur")
today = datetime.now(tz)
date = today.strftime("%d")
day = today.strftime("%d / %B / %Y")

load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)


def refresh_date():
    global today, date, day
    today = datetime.now(tz)
    date = today.strftime("%d")
    day = today.strftime("%d / %B / %Y")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id, "Welcome to MenuDs Bot.Type /menu to see the ds menu."
    )

@bot.message_handler(commands=["call"])
def call(message):
    if idss != "":
        bot.send_message(message.chat.id, idss)
    else:
        bot.send_message(message.chat.id, "nothing yet to see")


@bot.message_handler(commands=["menu"])
def menu(message):
    refresh_date()
    h = date.lstrip("0")
    send = f"menus/{h}.png"
    try:
        with open(send, "rb") as photo:
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, f"This is the menu for : {day}")

    except FileNotFoundError:
        bot.send_message(message.chat.id, "No photo 'yet'..")
    snd = "menus/first.png"
    if message.chat.id in ss:
        pass
    else:
        bot.send_message("giving up? -quiz-")
        ss.append(message.chat.id)
    try:
        with open(snd, "rb") as photos:
            if message.chat.id in idss:
                pass
            else:
               # bot.send_document(message.chat.id, photos)
                #bot.send_message(message.chat.id, "A mere quiz.")
                #idss.append(message.chat.id)
                pass
    except FileNotFoundError:
        pass
       # bot.send_message(message.chat.id, "none")


@bot.message_handler(commands=["dd56"])
def quiz(message):
    bot.send_message(message.chat.id, "Impressive..though it is not flexible")
    send = "menus/secon3d.png"
    try:
        with open(send, "rb") as photo:
            if message.chat.id in idss:
               pass
            else:
                bot.send_document(message.chat.id, photo)
                bot.send_message(message.chat.id, "from stegano import lsb\nj = reveal(\"./secon3d.png\")\nprint(j)")
                idss.append(message.chat.id)
    except FileNotFoundError:
        pass
        bot.send_message(message.chat.id, "No clue 'yet'..")
    

@bot.message_handler(commands=["kukla08"])
def kukla(message):
    bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAEMx0Rm3RBGkprf69n8056dHpa7X1w6uAACXQMAAu8XYAl5iuzISQP6fjYE")
    bot.send_message(message.chat.id, "Impressive, The quiz has been effectively completed. Kindly capture a screeshot of this message thus share it with me")


@bot.message_handler(commands=["tmr"])
def tmr(message):
    refresh_date()
    h = date.lstrip("0")
    n = int(h) + 1
    if n == 32:
        n = 1
    send = f"menus/{n}.png"
    try:
        with open(send, "rb") as photo:
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, f"This is the menu for tomorrow.")

    except FileNotFoundError:
        bot.send_message(message.chat.id, "No photo 'yet'..")


bot.infinity_polling()
