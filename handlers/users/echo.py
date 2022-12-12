import datetime
from aiogram import types
from keyboards.default.main import main, city
from loader import dp, db, bot
from .functions import times, city_code
from data.config import month_now, day_now, year_now



@dp.message_handler(text="🕋 Bugungi namoz vaqtlari")
async def today_prayertimes(message: types.Message):
    # foydalanuvchi manzilini aniqash
    user = await db.select_user(telegram_id=message.from_user.id)
    user_address = user[2]
    user_address_id = await city_code(user_address)

    # namoz vaqtlar
    result = await times(user_address_id, month_now, day_now)
    bomdod = result['bomdod']
    quyosh = result['quyosh']
    peshin = result['peshin']
    asr = result['asr']
    shom = result['shom']
    xufton = result['xufton']

    # foydalanuvchida xabar yuborish
    await message.answer(f'{day_now}.{month_now}.{year_now}\n\n'
                         f'<b>{user_address}</b> shahri vaqti bilan\n{message.text}\n\n'
                         f'🌅 {bomdod}     Bomdod<i> (saharlik)</i>\n\n'
                         f'🌞 {quyosh}     Quyosh chiqishi\n\n'
                         f'🏞 {peshin}     Peshin\n\n'
                         f'🌇 {asr}     Asr\n\n'
                         f'🏙 {shom}     Shom<i> (iftorlik)</i>\n\n'
                         f'🌃 {xufton}     Xufton\n\n'
                         f'@namoz_vaqtii_bot', reply_markup=main)




@dp.message_handler(text="🗓 Haftalik namoz vaqtlari")
async def week_prayertimes(message: types.Message):
    # foydalanuvchi manzilini aniqlash
    user = await db.select_user(telegram_id=message.from_user.id)
    user_address = user[2]
    user_address_id = await city_code(user_address)

    # xabarni tayyorlash va yuborish

    m = await message.answer('⌛ ')
    txt = f'<b>{user_address}</b> shahri vaqti bilan\n{message.text}\n\n'
    for n in range(1, 8):
        d = datetime.datetime.today() + datetime.timedelta(days=n-1)
        day, month, year = d.day, d.month, d.year
        result = await times(user_address_id, month, day)

        bomdod = result['bomdod']
        quyosh = result['quyosh']
        peshin = result['peshin']
        asr = result['asr']
        shom = result['shom']
        xufton = result['xufton']

        txt += f'{day}.{month}.{year}\n' \
            f'🌅 <b>{bomdod}</b>     Bomdod<i> (saharlik)</i>\n' \
            f'🌞 <b>{quyosh}</b>     Quyosh chiqishi\n' \
            f'🏞 <b>{peshin}</b>     Peshin\n' \
            f'🌇 <b>{asr}</b>     Asr\n' \
            f'🏙 <b>{shom}</b>     Shom<i> (iftorlik)</i>\n' \
            f'🌃 <b>{xufton}</b>     Xufton\n\n'
    txt += '@namoz_vaqtii_bot'
    await message.answer(txt)
    await m.delete()




@dp.message_handler(text="📍 Hududni o'zgartirish")
async def update_address(message: types.Message):
    await message.answer("Hududni tanlang:", reply_markup=city)


@dp.message_handler(state=None)
async def prayertimes(message: types.Message):
    try:
        # foydalanuvchini adresini saqlash
        rest = await city_code(message.text)
        await db.update_user_address(telegram_id=message.from_user.id, Address=message.text)


        # namoz vaqtlar
        result = await times(rest, month_now, day_now)
        bomdod = result['bomdod']
        quyosh = result['quyosh']
        peshin = result['peshin']
        asr = result['asr']
        shom = result['shom']
        xufton = result['xufton']

        # xabarni foydalanuvchiga yuborish
        await message.answer(f'{day_now}.{month_now}.{year_now}\n\n'
                             f'<b>{message.text} vaqti bilan namoz vaqtlari</b>\n\n'
                             f'🌅 {bomdod}     Bomdod<i> (saharlik)</i>\n\n'
                             f'🌞 {quyosh}     Quyosh chiqishi\n\n'
                             f'🏞 {peshin}     Peshin\n\n'
                             f'🌇 {asr}     Asr\n\n'
                             f'🏙 {shom}     Shom<i> (iftorlik)</i>\n\n'
                             f'🌃 {xufton}     Xufton\n\n'
                             f'@namoz_vaqtii_bot', reply_markup=main)

    except:
        await message.answer("Noto'g'ri buyruq")
