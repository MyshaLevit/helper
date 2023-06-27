import sqlite3
import datetime

# Подключение к базе данных SQLite3
conn = sqlite3.connect('messages.db')
c = conn.cursor()

# Создание таблицы, если ее нет
c.execute('''CREATE TABLE IF NOT EXISTS messages
             (user_id INTEGER PRIMARY KEY, username TEXT, message_count INTEGER, last_updated TEXT)''')

# Функция для обновления количества сообщений пользователя
def update_message_count(user_id, username):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    c.execute("SELECT * FROM messages WHERE user_id=?", (user_id,))
    result = c.fetchone()
    if result:
        message_count = result[2] + 1
        last_updated = today
        c.execute("UPDATE messages SET message_count=?, last_updated=? WHERE user_id=?", (message_count, last_updated, user_id))
    else:
        message_count = 1
        last_updated = today
        c.execute("INSERT INTO messages (user_id, username, message_count, last_updated) VALUES (?, ?, ?, ?)", (user_id, username, message_count, last_updated))
    conn.commit()




# Функция для проверки количества сообщений пользователя
def check_message_count(user_id):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    c.execute("SELECT * FROM messages WHERE user_id=?", (user_id,))
    result = c.fetchone()
    if result:
        message_count = result[2]
        last_updated = result[3]
        if last_updated != today:
            message_count = 0
            c.execute("UPDATE messages SET message_count=? WHERE user_id=?", (message_count, user_id))
            conn.commit()
        return message_count
    else:
        return 0