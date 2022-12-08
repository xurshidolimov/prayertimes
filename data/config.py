from environs import Env
import datetime

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5473423088:AAH_f6Z1Tg-OtN6Y7BgoVm4BJUq3p3DNXfU"  # Bot toekn
ADMINS = 679932311  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")

month_now = datetime.datetime.now().month
day_now = datetime.datetime.now().day
year_now = datetime.datetime.now().year
