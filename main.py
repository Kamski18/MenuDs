import telebot 
import os
from dotenv import load_dotenv
from pytz import timezone
from datetime import datetime, timedelta
from telebot.types import InlineKeyboardButton as kb
from telebot.types import InlineKeyboardMarkup as km
from telebot.types import CallbackQuery
#--- All variable are stated here ---#

idss =[]
tz = timezone("Asia/Kuala_Lumpur")
today = datetime.now(tz)
date = today.strftime("%d")
day = today.strftime("%d / %B / %Y")

tmr = today + timedelta(days=1)
tmrw = tmr.strftime("%d").lstrip("0")


def create_keyboard():
    keyboard = km()
    button1 = kb("Menu", callback_data="btn1")
    button2 = kb("Tomorrow", callback_data="btn2")
    keyboard.add(button1, button2)
    return keyboard

load_dotenv()
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)


#--- Refresh date function ---#

def refresh_date():
    global today, date, day, tmr, tmrw
    today = datetime.now(tz)
    date = today.strftime("%d")
    day = today.strftime("%d : %B : %Y")
    tmr = today + timedelta(days=1)
    tmrw = tmr.strftime("%d").lstrip("0")

#--- Start command function ---#

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = create_keyboard()
    bot.send_message(message.chat.id, "Welcome to MenuDs Bot.Type /menu to see the ds menu.", reply_markup=keyboard)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)




#--- Call command function ---#

@bot.message_handler(commands=["call"])
def call(message):
    if 1 == 1:
        bot.send_message(message.chat.id, tmr)
    else:
        bot.send_message(message.chat.id, "nothing yet to see")

#--- Menu command function ---#

@bot.message_handler(commands=["menu"])
def menu(message):
    refresh_date()
    h = date.lstrip("0")
    send = f"menus/{h}.png"
    try:
        with open(send, "rb") as photo:
            keyboard = create_keyboard()
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, f"This is the menu for: {day}", reply_markup=keyboard)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

    except FileNotFoundError:
        keyboard = create_keyboard()
        bot.send_message(message.chat.id, "File are not to be found :(", reply_markup=keyboard)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

#--- dd56 command function ---#


@bot.message_handler(func=lambda message: message.text.startswith("/"))
def dynamic_date_menu(message):
    try:
        command = message.text.lstrip("/")
        if command.isdigit():
            date_num = int(command)
            
            if 1 <= date_num <= 31: 
                send = f"menus/{date_num}.png"
                try:
                    with open(send, "rb") as photo:
                        bot.send_photo(message.chat.id, photo)
                        bot.send_message(message.chat.id, f"This is the menu for: {date_num}")
                except FileNotFoundError:
                    bot.send_message(message.chat.id, "Menu for the specified date is not found.")
            else:
                bot.send_message(message.chat.id, "Please provide a valid date between 1 and 31.")
        else:
            bot.send_message(message.chat.id, "Invalid command. Use a date number like '/15'.")
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred. Please try again.")


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
    

#--- kukla08 command function ---#

@bot.message_handler(commands=["kukla08"])
def kukla(message):
    bot.send_sticker(message.chat.id, "CAACAgUAAxkBAAEMx0Rm3RBGkprf69n8056dHpa7X1w6uAACXQMAAu8XYAl5iuzISQP6fjYE")
    bot.send_message(message.chat.id, "Impressive, The quiz has been effectively completed. Kindly capture a screeshot of this message thus share it with me")

#--- tmr command function ---#

@bot.message_handler(commands=["tmr"])
def tmrr(message):
    refresh_date()
    h = date.lstrip("0")
    n = tmrw
    if n == 32:
        n = 1
    send = f"menus/{n}.png"
    try:
        with open(send, "rb") as photo:
            bot.send_photo(message.chat.id, photo)
            keyboard = create_keyboard()
            bot.send_message(message.chat.id, f"This is the menu for tomorrow.", reply_markup=keyboard)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

    except FileNotFoundError:
        bot.send_message(message.chat.id, "No photo 'yet'..")


#---callback responds---#

@bot.callback_query_handler(func=lambda call: call.data in ['btn1', 'btn2'])
def handle_query(call: CallbackQuery):
    bot.answer_callback_query(call.id)
    refresh_date()
    
    h = date.lstrip("0")
    
    if call.data == 'btn1':
        send = f"menus/{h}.png"
        try:
            with open(send, "rb") as photo:
                keyboard = create_keyboard()
                bot.send_photo(call.message.chat.id, photo)
                bot.send_message(call.message.chat.id, f"This is the menu for: {day}", reply_markup=keyboard)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        except FileNotFoundError:
            keyboard = create_keyboard()
            bot.send_message(call.message.chat.id, "File not found :(", reply_markup=keyboard)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    
    elif call.data == 'btn2':
        n = tmrw
        if n == 32:
            n = 1
          # Assuming the menus reset after 31
        send = f"menus/{n}.png"
        try:
            with open(send, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
                keyboard = create_keyboard()
                bot.send_message(call.message.chat.id, "This is the menu for tomorrow.", reply_markup=keyboard)
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
        except FileNotFoundError:
            keyboard = create_keyboard()
            bot.send_message(call.message.chat.id, "No photo 'yet'..", reply_markup=keyboard)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)

##
bot.infinity_polling()
