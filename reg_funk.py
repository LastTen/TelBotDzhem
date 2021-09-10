
from typing import Text
import psycopg2
from dataConect import dataConect


connection = psycopg2.connect(
  database = dataConect["pg_name"],
  user = dataConect["pg_user"],
  password = dataConect["pg_password"],
  host = dataConect["pg_host"],
  port = dataConect['pg_port']
)


## REGISTRATION##

def registration(idtg, nametg, first_name, last_name):
  cursor = connection.cursor()
  into = f"insert into user_name (id, first_name, last_name, nick_name, game_loc_num) values ({idtg}, '{first_name}', '{last_name}', '{nametg}', 1)"
  cursor.execute(into)
  connection.commit()
  cursor.close()

def selReg(idtg, nametg, first_name, last_name):
  cursor = connection.cursor()
  select = f"SELECT id FROM user_name WHERE id = {idtg}"
  cursor.execute(select)
  if cursor.fetchall():
    return(f"З поверненням {first_name}, чим можу допомогти?")
  elif cursor.fetchone() == None:
     registration(idtg, nametg, first_name, last_name)
     cursor.close()
     return(f'Вітаю з реєстрацією чим можу допомогти');

###QWEST FOR LOCATION##
def ansv_qwest(message):
  cursor = connection.cursor()
  into = f"update public.user_name set game_loc_num = 1 Where id = {message.chat.id}"
  cursor.execute(into)
  connection.commit()
  cursor.close()
  return 1
 


####SEND LOCATION##
def user_answer_num(message):
  cursor = connection.cursor()
  select = f"select game_loc_num from public.user_name WHERE id = {message.chat.id}"
  cursor.execute(select)
  res =  cursor.fetchone()[0]
  cursor.close()
  return res

def us_location(message):
  num_l = user_answer_num(message)
  cursor = connection.cursor()
  select = f"select location from public.qwestions where num_loc = {num_l}"
  cursor.execute(select)
  res =  cursor.fetchone()[0].split(' ')
  cursor.close()
  loc = []
  for k in res:
    loc.append(float(k))
  return loc


def us_qwest(message):
  num_l = user_answer_num(message)
  cursor = connection.cursor()
  select = f"select qwest from public.qwestions where num_loc = {num_l}"
  cursor.execute(select)
  res =  cursor.fetchone()[0].split('\\n')
  res1 = "\n".join(res)
  cursor.close()
  return res1


def qwest_loc_ans(num_loc, message):
  text = f"{message.text}".upper()
  cursor = connection.cursor()
  select = f"select answer from public.qwestions  where num_loc = {num_loc} and answer = '{text}'"
  cursor.execute(select)
  res = cursor.fetchone()
  cursor.close()
  return res



def next_qwest(message):
  cursor = connection.cursor()
  into = f"update public.user_name set game_loc_num = game_loc_num + 1 Where id = {message.chat.id}"
  cursor.execute(into)
  connection.commit()
  cursor.close()



# #### ОБРОБКА ТЕКСТА #####
# def qwest_user(text):
#   message_qwest = []
#   text_user = text.lower().replace('?', '').replace('.', '').replace(',', '')
#   list_text = text_user.split(' ')
#   for len_text in list_text:
#     if len(len_text) > 3:
#       message_qwest.append(len_text)
#   return message_qwest


# def message_category(text):
#   qwest = qwest_user(text)
#   message_answer = []
#   for key in qwest:
#     if key[0] == '/':
#       cursor = connection.cursor()
#       cursor.execute("SELECT category_name, description FROM category")
#       category_data = cursor.fetchall()
#       cursor.close()
#       for n_category in category_data:
#         if n_category[0] == key:
#           message_answer.append(n_category[1])
#   return message_answer
  

# def message_text(text):
#   qwest = qwest_user(text)
#   message_answer = []
#   for key in qwest:
#     cursor = connection.cursor()
#     like_qwest = f"'{key}%'"
#     cursor.execute(f"SELECT answer FROM answer WHERE qwest LIKE {like_qwest}")
#     answer_text = cursor.fetchall()
#     cursor.close()
#     if answer_text != []:
#       message_answer.append(answer_text[0][0])
#   return(message_answer)


# def message_user(text):
#   category = message_category(text)
#   answer = message_text(text)
#   gener_answer = answer + category
#   if len(gener_answer):
#     return"\n".join(gener_answer)
#   else:
#     return "Не зрозумів питання для допомлги натисни /help"

