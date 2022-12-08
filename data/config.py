from environs import Env
import datetime

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5473423088:AAH_f6Z1Tg-OtN6Y7BgoVm4BJUq3p3DNXfU"  # Bot toekn
ADMINS = 679932311  # adminlar ro'yxati
IP = 'localhost'  # Xosting ip manzili

DB_USER = 'xurshid'
DB_PASS = 'xurshid_olimov'
DB_NAME = 'prayertimes'
DB_HOST = 'localhost'

month_now = datetime.datetime.now().month
day_now = datetime.datetime.now().day
year_now = datetime.datetime.now().year
