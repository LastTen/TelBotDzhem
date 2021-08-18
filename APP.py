import telebot
from dataConect import dataConect
from locationSort import d
import reg_funk

import psycopg2
from dataConect import dataConect
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
def calendar(message):
  cursor.execute(f"SELECT CONCAT(title, ' відбудеться  ', EXTRACT(day FROM DATE), '-', EXTRACT(month FROM date), '  детальніше...    ', category) FROM events WHERE date >= CURRENT_DATE")
  res = ()
  for k in cursor.fetchall():
    res += k
  for mess in res:
    bot.send_message(message.chat.id, mess)


#########################__TEXT__#####################
# @bot.message_handler(content_types= ['text'])
# def send_helper(message):
#   print(message.chat.id)
#   print(message.chat.username)
#   print(message.text)
#   bot.send_message(message.chat.id, 'hello')


@bot.message_handler(content_types= ['text'])
def send_helper(message):
  for k in d:
    if k == message.text:
      # mess_text = f"Координата обєкта {d[k]['li']}широти {d[k]['lo']}довготи"
      bot.send_location(message.chat.id, d[k]['li'],d[k]['lo'])





####################______END______#####################

bot.polling(none_stop = True , interval = 1)
cursor.close()
print('stop')
