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

def registration(idtg, nametg):
  into = f"insert into tgusers (id, user_name) values ({idtg}, '{nametg}')"
  cursor.execute(into)
  connection.commit()

def selReg(idtg, nametg):
  select = f"SELECT id FROM tgusers WHERE id = {idtg}"
  cursor.execute(select)
  if cursor.fetchall():
    return(f"З поверненням {nametg} чим можу допомогти?")
  elif cursor.fetchone() == None:
     registration(idtg, nametg)
     return(f'Вітаю чим можу допомогти');

