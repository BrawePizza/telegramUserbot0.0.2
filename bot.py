import time
from pyrogram import Client, filters
from configparser import ConfigParser

# Чтение значений из файла data.ini
config = ConfigParser()
config.read("data.ini", encoding="utf-8")

api_id = config.getint("pyrogram", "api_id")
api_hash = config.get("pyrogram", "api_hash")

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Извлечение значения your_user_id из файла data.ini
your_user_id = config.getint("pyrogram", "your_user_id")

@app.on_message(filters.command("пинг", prefixes=["с ", "С "]) & filters.user(your_user_id))
def respond_ping(client, message):
    start_time = time.time()
    reply_message = message.edit_text("пон г")
    end_time = time.time()
    elapsed_time = int((end_time - start_time) * 1000)
    reply_message.edit_text(f"пон г\nВремя приключений {elapsed_time} мс")

app.run()
