import telebot
import psycopg2
from dataConect import dataConect
import reg_funk


connection = psycopg2.connect(
  database = dataConect["pg_name"],
  user = dataConect["pg_user"],
  password = dataConect["pg_password"],
  host = dataConect["pg_host"],
  port = dataConect['pg_port']
)
cursor = connection.cursor()

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
  bot.send_message(message.chat.id, "Для початку вибери напрямок /calendar")

@bot.message_handler(commands=['calendar'])
def send_calendar(message):
  text_calendar = reg_funk.calendar()
  bot.send_message(message.chat.id, text_calendar)

@bot.message_handler(commands=['location'])
def send_location1(message):
  bot.send_message(message.chat.id, 'Введіть порядковий номер бажаной локації')
  bot.register_next_step_handler(message, answer_loc)

def answer_loc(message):
  bot.send_location(message.chat.id, reg_funk.send_location_li(message.text), reg_funk.send_location_lo(message.text))




########################__TEXT__#####################
@bot.message_handler(content_types= ['text'])
def send_helper(message):
  print(message.chat.id)
  print(message.chat.username)
  print(message.text)
  bot.send_message(message.chat.id, 'hello')



####################______END______#####################

bot.polling(none_stop = True , interval = 1)
cursor.close()
print('stop')
