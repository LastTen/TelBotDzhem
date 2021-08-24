import psycopg2
from dataConect import dataConect
from locationSort import location


connection = psycopg2.connect(
  database = dataConect["pg_name"],
  user = dataConect["pg_user"],
  password = dataConect["pg_password"],
  host = dataConect["pg_host"],
  port = dataConect['pg_port']
)


def registration(idtg, nametg):
  cursor = connection.cursor()
  into = f"insert into tgusers (id, user_name) values ({idtg}, '{nametg}')"
  cursor.execute(into)
  connection.commit()
  cursor.close()

def selReg(idtg, nametg):
  cursor = connection.cursor()
  select = f"SELECT id FROM tgusers WHERE id = {idtg}"
  cursor.execute(select)
  if cursor.fetchall():
    return(f"З поверненням {nametg} чим можу допомогти?")
  elif cursor.fetchone() == None:
     registration(idtg, nametg)
     cursor.close()
     return(f'Вітаю чим можу допомогти');

def calendar():
  cursor = connection.cursor()
  cursor.execute(f"SELECT CONCAT(title, ' відбудеться  ', EXTRACT(day FROM DATE), '-', EXTRACT(month FROM date), '  детальніше...    ', category) FROM events WHERE date >= CURRENT_DATE")
  res = ()
  for k in cursor.fetchall():
    res += k
  cursor.close()
  return('\n'.join(res))



def send_location_li(num_location):
  for k in location:
    if k == num_location:
      return location[k]['li']
    

def send_location_lo(num_location):
  for k in location:
    if k == num_location:
      return location[k]['lo']



#### ОБРОБКА ТЕКСТА #####
def qwest_user(text):
  message_qwest = []
  text_user = text.lower().replace('?', '').replace('.', '').replace(',', '')
  list_text = text_user.split(' ')
  for len_text in list_text:
    if len(len_text) > 3:
      message_qwest.append(len_text)
  return message_qwest


def message_category(text):
  qwest = qwest_user(text)
  message_answer = []
  for key in qwest:
    if key[0] == '/':
      cursor = connection.cursor()
      cursor.execute("SELECT category_name, description FROM category")
      category_data = cursor.fetchall()
      cursor.close()
      for n_category in category_data:
        if n_category[0] == key:
          message_answer.append(n_category[1])
  return message_answer
  

def message_text(text):
  qwest = qwest_user(text)
  message_answer = []
  for key in qwest:
    cursor = connection.cursor()
    like_qwest = f"'{key}%'"
    cursor.execute(f"SELECT answer FROM answer WHERE qwest LIKE {like_qwest}")
    answer_text = cursor.fetchall()
    cursor.close()
    if answer_text != []:
      message_answer.append(answer_text[0][0])
  return(message_answer)


def message_user(text):
  category = message_category(text)
  answer = message_text(text)
  print(category)
  print(answer)




message_user('Прfhfh fffhfhf fkfkfkf приві погода /strit /disco ')
