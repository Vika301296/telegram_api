import os
import telegram

from dotenv import load_dotenv


load_dotenv()
bot = telegram.Bot(token=os.getenv('TOKEN'))
chat_id = 986055024
chat_id_1 = '@nasa_and_spacex_pictures'
bot.send_message(text='Hi Vika!', chat_id=chat_id_1)

updates = bot.get_updates()
print(updates[0])
