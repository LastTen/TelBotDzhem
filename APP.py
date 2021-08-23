import telebot
from dataConect import dataConect
import reg_funk

bot = telebot.TeleBot(dataConect['Token_TG'])
print('start')


######################____БОТ____###################
###################################__КОМАНДИ__################
@bot.message_handler(commands=['start'])
def send_welcome(message):
  textStart = reg_funk.selReg(message.chat.id, message.chat.username)
  bot.send_message(message.chat.id, textStart)

@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.send_message(message.chat.id, "Для початку вибери напрямок \n /calendar \n /location")

@bot.message_handler(commands=['calendar'])
def send_calendar(message):
  text_calendar = reg_funk.calendar()
  bot.send_message(message.chat.id, text_calendar)

@bot.message_handler(commands=['location'])
def send_location_qwest(message):
  bot.send_message(message.chat.id, 'Введіть порядковий номер бажаной локації')
  bot.register_next_step_handler(message, answer_loc)

def answer_loc(message):
  if reg_funk.send_location_li(message.text):
    bot.send_location(message.chat.id, reg_funk.send_location_li(message.text), reg_funk.send_location_lo(message.text))
  else:
    bot.send_message(message.chat.id, 'Не вірний номер локації, спробуй ще раз \n /location')


########################__TEXT__#####################
@bot.message_handler(content_types= ['text'])
def send_message(message):
  print(message.chat.id)
  print(message.chat.username)
  print(message.text)
  text_message = reg_funk.message_user(message.text)
  bot.send_message(message.chat.id, text_message)


####################______END______#####################

bot.polling(none_stop = True , interval = 1)
print('stop')
