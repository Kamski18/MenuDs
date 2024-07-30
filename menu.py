import telebot
import datetime
import os
from dotenv import load_dotenv


today = datetime.datetime.now()
date = today.strftime("%d")
day = today.strftime("%d / %B / %Y")

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)



@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id,"Welcome to MenuDs Bot.Type /menu to see the ds menu.")
  

@bot.message_handler(commands=['menu'])
def menu(message):
  send = f'{date}.jpg'
  if date == date:
    try:
      with open(send, 'rb') as photo:
       bot.send_photo(message.chat.id, photo)
       bot.send_message(message.chat.id, f"This is the menu for : {day}")
      
    except FileNotFoundError:
      bot.send_message(message.chat.id, "No photo 'yet'..")

@bot.message_handler(commands=['tmr'])
def tmr(message):
  n = int(date) + 1
  send = f'menus/{n}.png'
  if date == date:
    try:
      with open(send, 'rb') as photo:
       bot.send_photo(message.chat.id, photo)
       bot.send_message(message.chat.id, f"This is the menu for tomorrow.")
      
    except FileNotFoundError:
      bot.send_message(message.chat.id, "No photo 'yet'..")
      
bot.polling()
