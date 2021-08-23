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


def message_user(text):
  text_user = f"'{text}%'"
  cursor = connection.cursor()
  cursor.execute(f"Select * FROM answer Where qwest LIKE{text_user}")
  answer = cursor.fetchone()[2]
  cursor.close()
  return(answer)
