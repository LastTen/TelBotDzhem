import telebot
from telebot.types import PhotoSize
from dataConect import dataConect
import reg_funk

bot = telebot.TeleBot(dataConect['Token_TG'])
print('start')


######################____БОТ____###################
###################################__КОМАНДИ__################
@bot.message_handler(commands=['start'])
def send_welcome(message):
  start_message = reg_funk.selReg(message.chat.id, message.chat.username, message.chat.first_name, message.chat.last_name)
  bot.send_message(message.chat.id, start_message)


@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.send_message(message.chat.id, "Для наступного кроку натисни /game \n Підказки про відповідь знаходяться на локації")

# @bot.message_handler(commands=['heppy'])
# def send_welcome(message):
#   text = f'Квест розпочинається для початку натисни /game і слідуй інструкції'
#   if message.chat.id == 469891609:
#     bot.send_message(650665525, f"{text}")
#     bot.send_location(650665525, 50.071007916968064, 31.46478637184649)
#     bot.send_message(491374102, f"{text}")
#     bot.send_location(491374102, 50.071007916968064, 31.46478637184649)
#     bot.send_message(469891609, f"{text}")
#     bot.send_location(469891609, 50.071007916968064, 31.46478637184649)

### GAME####

@bot.message_handler(commands=['game', 'Game'])
def answer(message):
  print(message.text)
  print(message.chat.id)
  loc = reg_funk.us_location(message)
  bot.send_location(message.chat.id, loc[0], loc[1])
  bot.send_message(message.chat.id, reg_funk.us_qwest(message))
  bot.register_next_step_handler(message, answer_loc)



def answer_loc(message):
  num_loc = reg_funk.user_answer_num(message)
  answer = reg_funk.qwest_loc_ans(num_loc, message)
  if answer:
    reg_funk.next_qwest(message)
    print(message.text)
    print(message.chat.id)
    loc = reg_funk.us_location(message)
    bot.send_location(message.chat.id, loc[0], loc[1])
    bot.send_message(message.chat.id, reg_funk.us_qwest(message))
    bot.register_next_step_handler(message, answer_loc)
  elif message.text == '/stop':
    bot.send_message(message.chat.id, 'Ви вишли з гри для старту натисни /game \nдля навігації натисни /help')
  elif message.text == '/new_game':
    reg_funk.ansv_qwest(message)
    bot.send_message(message.chat.id, 'Ви починаєте гру спочатку. /game')
  else:
    print(message.text)
    print(message.chat.id)
    bot.send_message(message.chat.id, 'Відповідь невірна, спробуй ще раз для, виходу з гри натисни /stop \nдля зкидання ігрового процесу натисни /new_game')
    bot.register_next_step_handler(message, answer_loc)






########################__TEXT__#####################
# @bot.message_handler(content_types= ['text'])
# def send_message(message):
#   print(message.chat.id)
#   print(message.chat.username)
#   print(message.text)
#   bot.send_message(message.chat.id, reg_funk.message_user(message.text))
# @bot.message_handler(content_types=['text'])
# def send_message(message):
#   bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
    print(message.chat.id)
    print(message.chat.username)
    print(message.text)
    bot.send_message(message.chat.id, 'Ви вишли з поля гри для того щоб повернутись натични /game')





####################______END______#####################

bot.polling(interval = 1)
print('stop')
