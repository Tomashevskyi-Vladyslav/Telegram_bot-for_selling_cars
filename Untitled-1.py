import telebot
from telebot import types
from aiogram.utils.markdown import hlink

token = '6814834703:AAF29vump_g4FKPsON2nNBAMq4Xs8aO6XI4'
bot_pay_token = "333605228:LIVE:26826_EBD3DA83A476EA3E3F8B1A20C9B7A40B998323E5"
bot_pay_token_2 = "387026696:LIVE:668cec16dfc2f3ca9022c91e"
bot = telebot.TeleBot(token)

user_avto_list = {}
user_avto_list_UZ_RU = {}
free_addvetesment = {}
users_advetesment = {}
counter = 0
leng_switcher = 0
terif = ""
var = 0

link_1 = hlink('#', '#')
link_2 = hlink('#', '#')
link_3 = hlink('#', '#')
link_4 = hlink('#', '#')

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_avto_list, users_advetesment
    bot.send_message(message.chat.id, text = 'Avtomarket Uzbekistan xush kelibsiz!\n\nBu yerda siz hohlagan avtomobilingizni eng yaxshi narxlarda sotishingiz va xarid qilishingiz, shuningdek, bozordagi joriy narxlar bilan tanishishingiz mumkin.\n\n-------------------------------------\n\nДобро пожаловать на Avtomarket Uzbekistan!\n\nТут вы можете продать и купить любую вами желаемую машину по самым выгодным ценам, а так же ознакомиться с актуальными ценами на рынке.')

    bot.send_message("#", text = f'Клиент запустил бот\n\nЮзернейм: @{message.from_user.username}')

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🇷🇺Русский", callback_data="🇷🇺Русский"))
    markup.add(types.InlineKeyboardButton("🇺🇿O'zbekcha", callback_data="🇺🇿O'zbekcha"))
    
    bot.send_message(message.chat.id, text = 'Kerakli tilni tanlang.\n\n-------------------------------------\n\nВыберите желаемый язык.', reply_markup=markup)
    
    try :
        if users_advetesment[message.chat.id]["advetesment"] == "True":
            users_advetesment.update({message.chat.id:{'advetesment:':"True"}})
    except Exception as err:
        users_advetesment.update({message.chat.id:{'advetesment:':"True"}})
        print(users_advetesment)

    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton("Дать рекламное обьявление🛍", callback_data="Дать рекламное обьявление🛍"))
    # markup.add(types.InlineKeyboardButton("Нужна помощь с другим вопросом❓", callback_data="Нужна помощь с другим вопросом ❓"))
    # user_avto_list.update({message.chat.id:{"leng":"RU"}})

    print(user_avto_list)
    # bot.send_message(message.chat.id, text = 'Добро пожаловать на Avtomarket Uzbekistan!\n\nТут вы можете продать и купить любую вами желаемую машину по самым выгодным ценам, а так же ознакомиться с актуальными ценами на рынке.', reply_markup=markup)
    bot.send_message("#", text = f'Клиент запустил бот\n\nЮзернейм: @{message.from_user.username}')

@bot.message_handler(commands=['support'])
def support_message(message):
        event_help = bot.send_message(message.chat.id, text = "Iltimos, xabaringizni qoldiring, biz siz bilan 24 soat ichida bog'lanamiz 🤓.\n\n-------------------------------------\n\nПожалуйста оставьте свое сообщение и в течении 24 часов мы свяжемся с вами 🤓.")
        bot.register_next_step_handler(event_help, event_help_help)

def event_help_help(message):
    bot.send_message("#", text = f"{message.text} Имя пользователя: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------
    bot.send_message(message.chat.id, text = "Xabar yuborildi, administrator tez orada siz bilan bog'lanadi.\n\n-------------------------------------\n\nСообщение было отправлено с вами скоро свяжеться администратор.")

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    global leng_switcher, user_avto_list, terif, user_avto_list_UZ_RU, free_addvetesment, link_1, link_2, link_3, link_4, users_advetesment, var

    if callback.data == "🇷🇺Русский":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Дать рекламное обьявление🛍", callback_data="Дать рекламное обьявление🛍"))
        markup.add(types.InlineKeyboardButton("Нужна помощь с другим вопросом❓", callback_data="Нужна помощь с другим вопросом❓"))
        user_avto_list.update({callback.message.chat.id:{"leng":"RU"}})
        user_avto_list_UZ_RU.update({callback.message.chat.id:{"leng":"RU"}})

        print(user_avto_list)
        bot.send_message(callback.message.chat.id, text = 'Выберете опцию', reply_markup=markup)

    if callback.data == "Нужна помощь с другим вопросом❓":
        event_help = bot.send_message(callback.message.chat.id, text = "Пожалуйста оставьте свое сообщение и в течении 24 часов мы свяжемся с вами 🤓.")
        bot.register_next_step_handler(event_help, event_help_1)

    if callback.data == "Эконом":
        terif = "Эконом"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Эконом"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Эконом"))

        bot.send_message(callback.message.chat.id, text = "Выберете способ оплаты.", reply_markup=markup)

    if callback.data == "CLICK Uzbekistan Эконом":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Эконом" с помощью сервеса CLICK Uzbekistan""", """Покупка тарифа "Эконом" """, "invoice", bot_pay_token, "UZS", [types.LabeledPrice("""Покупка тарифа "Эконом" """, 49000*100)])

    if callback.data == "Pey Me Эконом":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Эконом" с помощью сервеса Pey Me""", """Покупка тарифа "Эконом" """, "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice("""Покупка тарифа "Эконом" """, 49000*100)])

    if callback.data == "Стандарт":
        terif = "Стандарт"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Стандарт"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Стандарт"))

        bot.send_message(callback.message.chat.id, text = "Выберете способ оплаты.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Стандарт":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Стандарт" с помощью сервеса CLICK Uzbekistan""", """Покупка тарифа "Стандарт" """, "invoice", bot_pay_token, "UZS", [types.LabeledPrice("""Покупка тарифа "Стандарт" """, 59000*100)])

    if callback.data == "Pey Me Стандарт":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Стандарт" с помощью сервеса Pey Me""", """Покупка тарифа "Стандарт" """, "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice("""Покупка тарифа "Стандарт" """, 59000*100)])

    if callback.data == "Премиум":
        terif = "Премиум"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Премиум"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Премиум"))

        bot.send_message(callback.message.chat.id, text = "Выберете способ оплаты.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Премиум":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Премиум" с помощью сервеса CLICK Uzbekistan""", """Покупка тарифа "Премиум" """, "invoice", bot_pay_token, "UZS", [types.LabeledPrice("""Покупка тарифа "Премиум" """, 69000*100)])

    if callback.data == "Pey Me Премиум":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Премиум" с помощью сервеса Pey Me""", """Покупка тарифа "Премиум" """, "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice("""Покупка тарифа "Премиум" """, 69000*100)])

    if callback.data == "Элитный":
        terif = "Элитный"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Элитный"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Элитный"))

        bot.send_message(callback.message.chat.id, text = "Выберете способ оплаты.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Элитный":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Элитный" с помощью сервеса CLICK Uzbekistan""", """Покупка тарифа "Элитный" """, "invoice", bot_pay_token, "UZS", [types.LabeledPrice("""Покупка тарифа "Элитный" """, 89000*100)])

    if callback.data == "Pey Me Элитный":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Элитный" с помощью сервеса Pey Me""", """Покупка тарифа "Элитный" """, "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice("""Покупка тарифа "Элитный" """, 89000*100)])

    if callback.data == "Эксклюзив":
        terif = "Эксклюзив"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Эксклюзив"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Эксклюзив"))

        bot.send_message(callback.message.chat.id, text = "Выберете способ оплаты.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Эксклюзив":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Эксклюзив" с помощью сервеса CLICK Uzbekistan""", """Покупка тарифа "Эксклюзив" """, "invoice", bot_pay_token, "UZS", [types.LabeledPrice("""Покупка тарифа "Эксклюзив" """, 129000*100)])

    if callback.data == "Pey Me Эксклюзив":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Эксклюзив" с помощью сервеса Pey Me""", """Покупка тарифа "Эксклюзив" """, "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice("""Покупка тарифа "Эксклюзив" """, 129000*100)])
        
    if callback.data == "Экстрим":
        terif = "Экстрим"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Экстрим"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Экстрим"))

        bot.send_message(callback.message.chat.id, text = "Выберете способ оплаты.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Экстрим":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Экстрим" с помощью сервеса CLICK Uzbekistan""", """Покупка тарифа "Экстрим" """, "invoice", bot_pay_token, "UZS", [types.LabeledPrice("""Покупка тарифа "Экстрим" """, 199000*100)])

    if callback.data == "Pey Me Экстрим":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Экстрим" с помощью сервеса Pey Me""", """Покупка тарифа "Экстрим" """, "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice("""Покупка тарифа "Экстрим" """, 199000*100)])


    if callback.data == "БЕСПЛАТНОЕ объявление  по Акции 🔉":

        try:
            var = len(users_advetesment[callback.message.chat.id])
            users_advetesment[callback.message.chat.id].update({var+1:user_avto_list[callback.message.chat.id]["Модель и марка машины:"]})

        except Exception as err:
            var = len(users_advetesment[callback.message.chat.id])
            users_advetesment[callback.message.chat.id].update({var+1:user_avto_list[callback.message.chat.id]["Avtomobil modeli va markasi:"]})

        print(users_advetesment)

        if user_avto_list[callback.message.chat.id]['leng'] == "RU":
            free_addvetesment.update({callback.message.chat.id:{"free-advetesment":"БЕСПЛАТНОЕ объявление  по Акции"}})
            bot.send_media_group("#", [telebot.types.InputMediaPhoto(user_avto_list[callback.message.chat.id]["Foto_1:"]), telebot.types.InputMediaPhoto(user_avto_list[callback.message.chat.id]["Foto_2:"]), telebot.types.InputMediaPhoto(user_avto_list[callback.message.chat.id]["Foto_3:"]), telebot.types.InputMediaPhoto(user_avto_list[callback.message.chat.id]["Foto_4:"]), telebot.types.InputMediaPhoto(user_avto_list[callback.message.chat.id]["Foto_5:"]), telebot.types.InputMediaPhoto(user_avto_list[callback.message.chat.id]["Foto_6:"], f"""🔥{user_avto_list[callback.message.chat.id]["Модель и марка машины:"]}-{user_avto_list[callback.message.chat.id]["Цена:"]}🔥\n\n▪️Модель и марка машины: {user_avto_list[callback.message.chat.id]["Модель и марка машины:"]}\n▪️Цена: {user_avto_list[callback.message.chat.id]["Цена:"]}\n▪️Тип кузова: {user_avto_list[callback.message.chat.id]["Тип кузова:"]}\n▪️Год выпуска: {user_avto_list[callback.message.chat.id]["Год выпуска:"]}\n▪️Пробег: {user_avto_list[callback.message.chat.id]["Пробег:"]}\n▪️Тип коробки передач: {user_avto_list[callback.message.chat.id]["Тип коробки передач:"]}\n▪️Цвет: {user_avto_list[callback.message.chat.id]["Цвет:"]}\n▪️Объем двигателя: {user_avto_list[callback.message.chat.id]["Объем двигателя:"]}\n▪️Вид топлива: {user_avto_list[callback.message.chat.id]["Вид топлива:"]}\n▪️Состояние машины: {user_avto_list[callback.message.chat.id]["Состояние машины:"]}\n▪️Количество владельцев: {user_avto_list[callback.message.chat.id]["Количество владельцев:"]}\n▪️Телефон для связи: {user_avto_list[callback.message.chat.id]["Телефон для связи:"]}\n▪️Город: {user_avto_list[callback.message.chat.id]["Город:"]}\n▪️Вид оплаты: {user_avto_list[callback.message.chat.id]["Вид оплаты:"]}""")])
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Сообщить о продаже машины 🚘")
            btn2 = types.KeyboardButton("Дать рекламное обьявление 🛍")
            btn3 = types.KeyboardButton("Нужна помощь с другим вопросом ❓")
            markup.add(btn1, btn2, btn3)
            bot.send_message(callback.message.chat.id, """Спасибо за доверие! Ваше объявление о продаже автомобиля будет опубликовано в кратчайшие сроки.\n\nПожалуйста, сообщите нам после продажи автомобиля 🙏🏻\n\nЕсли ваш пост не будет опубликован в течении 24 часов, прошу связаться с Админом.""", reply_markup=markup)
            bot.send_message(callback.message.chat.id, text = f"Мы активно развиваем наш канал AvtoMarket Uzbekistan, и будем очень признательны, если вы поделитесь ссылкой с друзьями и близкими на наш канал!\n\n• {link_1}\n• {link_2}\n• {link_3}\n• {link_4}", parse_mode='HTML')
        
        if user_avto_list[callback.message.chat.id]['leng'] == "OZ":
            free_addvetesment.update({callback.message.chat.id:{"free-advetesment":"БЕСПЛАТНОЕ объявление  по Акции"}})
            bot.send_media_group("#", [telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[callback.message.chat.id]["Foto_1:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[callback.message.chat.id]["Foto_2:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[callback.message.chat.id]["Foto_3:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[callback.message.chat.id]["Foto_4:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[callback.message.chat.id]["Foto_5:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[callback.message.chat.id]["Foto_6:"], f"""🔥{user_avto_list_UZ_RU[callback.message.chat.id]["Модель и марка машины:"]}-{user_avto_list_UZ_RU[callback.message.chat.id]["Цена:"]}🔥\n\n▪️Модель и марка машины: {user_avto_list_UZ_RU[callback.message.chat.id]["Модель и марка машины:"]}\n▪️Цена: {user_avto_list_UZ_RU[callback.message.chat.id]["Цена:"]}\n▪️Тип кузова: {user_avto_list_UZ_RU[callback.message.chat.id]["Тип кузова:"]}\n▪️Год выпуска: {user_avto_list_UZ_RU[callback.message.chat.id]["Год выпуска:"]}\n▪️Пробег: {user_avto_list_UZ_RU[callback.message.chat.id]["Пробег:"]}\n▪️Тип коробки передач: {user_avto_list_UZ_RU[callback.message.chat.id]["Тип коробки передач:"]}\n▪️Цвет: {user_avto_list_UZ_RU[callback.message.chat.id]["Цвет:"]}\n▪️Объем двигателя: {user_avto_list_UZ_RU[callback.message.chat.id]["Объем двигателя:"]}\n▪️Вид топлива: {user_avto_list_UZ_RU[callback.message.chat.id]["Вид топлива:"]}\n▪️Состояние машины: {user_avto_list_UZ_RU[callback.message.chat.id]["Состояние машины:"]}\n▪️Количество владельцев: {user_avto_list_UZ_RU[callback.message.chat.id]["Количество владельцев:"]}\n▪️Телефон для связи: {user_avto_list_UZ_RU[callback.message.chat.id]["Телефон для связи:"]}\n▪️Город: {user_avto_list_UZ_RU[callback.message.chat.id]["Город:"]}\n▪️Вид оплаты: {user_avto_list_UZ_RU[callback.message.chat.id]["Вид оплаты:"]}""")])
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
            btn1 = types.KeyboardButton("Avtomobil sotilgani haqida xabar bering 🚘")
            btn2 = types.KeyboardButton("E'lon qo'ying 🛍")
            btn3 = types.KeyboardButton("Boshqa savol bo'yicha yordam kerak ❓")
            markup.add(btn1, btn2, btn3)
            bot.send_message(callback.message.chat.id, """Spasibo za doverie! Vashe ob'yavlenie o prodaje avtomobilya budet opublikovano v kratchayshie sroki.\n\nPojaluysta, soobshchite nam posle prodaji avtomobilya 🙏🏻\n\nEsli vash post ne budet opublikovan v techenii 24 soat, proshu svyazatsya s Administratorom.""", reply_markup=markup)
            bot.send_message(callback.message.chat.id, text = f"My aktivno razvivaem nash kanal AvtoMarket Uzbekistan, i budem ochen priznatelny, esli vy podelites ssylkoy s druzyami i blizkimi na nash kanal!\n\nSsylka na kanal:\n\n• {link_1}\n• {link_2}\n• {link_3}\n• {link_4}", parse_mode='HTML')

    if callback.data == "Iqtisodiyot":
        terif = "Iqtisodiyot"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Iqtisodiyot"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Iqtisodiyot"))

        bot.send_message(callback.message.chat.id, text = "Toʻlov usulini tanlang.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Iqtisodiyot":
        bot.send_invoice(callback.message.chat.id, """CLICK Uzbekistan xizmatidan foydalangan holda "Iqtisodiy" tarifini xarid qilish""", """ "Iqtisodiy" xarid tarifi""", "invoice", bot_pay_token, "UZS", [types.LabeledPrice(""" "Iqtisodiy" xarid tarifi""", 49000*100)])
   
    if callback.data == "Pey Me Iqtisodiyot":
        bot.send_invoice(callback.message.chat.id, """Pey Me xizmatidan foydalangan holda "Iqtisodiy" tarifini xarid qilish""", """ "Iqtisodiy" xarid tarifi""", "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice(""" "Iqtisodiy" xarid tarifi""", 49000*100)])

    if callback.data == "Standart":
        terif = "Standart"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Standart"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Standart"))

        bot.send_message(callback.message.chat.id, text = "Toʻlov usulini tanlang.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Standart":
        bot.send_invoice(callback.message.chat.id, """CLICK Uzbekistan xizmatidan foydalangan holda “Standart” tarifini xarid qilish""", """ "Standart" tarifini xarid qilish""", "invoice", bot_pay_token, "UZS", [types.LabeledPrice(""" "Standart" tarifini xarid qilish""", 59000*100)])

    if callback.data == "Pey Me Standart":
        bot.send_invoice(callback.message.chat.id, """Pey Me xizmatidan foydalangan holda “Standart” tarifini xarid qilish""", """ "Standart" tarifini xarid qilish""", "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice(""" "Standart" tarifini xarid qilish""", 59000*100)])

    if callback.data == "Premium":
        terif = "Premium"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Premium"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Premium"))

        bot.send_message(callback.message.chat.id, text = "Toʻlov usulini tanlang.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Premium":
        bot.send_invoice(callback.message.chat.id, """CLICK Uzbekistan xizmatidan foydalangan holda “Premium” tarifini xarid qilish""", """ “Premium” tarifini xarid qilish""", "invoice", bot_pay_token, "UZS", [types.LabeledPrice(""" “Premium” tarifini xarid qilish""", 69000*100)])

    if callback.data == "Pey Me Premium":
        bot.send_invoice(callback.message.chat.id, """Pey Me xizmatidan foydalangan holda “Premium” tarifini xarid qilish""", """ “Premium” tarifini xarid qilish""", "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice(""" “Premium” tarifini xarid qilish""", 69000*100)])

    if callback.data == "Elite":
        terif = "Elite"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Elite"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Elite"))

        bot.send_message(callback.message.chat.id, text = "Toʻlov usulini tanlang.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Elite":
        bot.send_invoice(callback.message.chat.id, """CLICK Uzbekistan xizmatidan foydalangan holda “Elite” tarifini xarid qilish""", """ “Elite” tarifini xarid qilish""", "invoice", bot_pay_token, "UZS", [types.LabeledPrice(""" “Elite” tarifini xarid qilish""", 89000*100)])
        
    if callback.data == "Pey Me Elite":
        bot.send_invoice(callback.message.chat.id, """Pey Me xizmatidan foydalangan holda “Elite” tarifini xarid qilish""", """ “Elite” tarifini xarid qilish""", "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice(""" “Elite” tarifini xarid qilish""", 89000*100)])

    if callback.data == "Eksklyuziv":
        terif = "Eksklyuziv"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Eksklyuziv"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Eksklyuziv"))

        bot.send_message(callback.message.chat.id, text = "Toʻlov usulini tanlang.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Eksklyuziv":
        bot.send_invoice(callback.message.chat.id, """CLICK Uzbekistan xizmatidan foydalangan holda “Eksklyuziv” tarifini xarid qilish""", """ “Eksklyuziv” tarifini xarid qilish""", "invoice", bot_pay_token, "UZS", [types.LabeledPrice(""" “Eksklyuziv” tarifini xarid qilish""", 129000*100)])

    if callback.data == "Pey Me Eksklyuziv":
        bot.send_invoice(callback.message.chat.id, """Pey Me xizmatidan foydalangan holda “Eksklyuziv” tarifini xarid qilish""", """ “Eksklyuziv” tarifini xarid qilish""", "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice(""" “Eksklyuziv” tarifini xarid qilish""", 129000*100)])

    if callback.data == "Ekstremal":
        terif = "Ekstremal"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Ekstremal"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Ekstremal"))

        bot.send_message(callback.message.chat.id, text = "Toʻlov usulini tanlang.", reply_markup=markup)
        
    if callback.data == "CLICK Uzbekistan Ekstremal":
        bot.send_invoice(callback.message.chat.id, """CLICK Uzbekistan xizmatidan foydalangan holda “Ekstremal” tarifini xarid qilish""", """ “Ekstremal” tarifini xarid qilish""", "invoice", bot_pay_token, "UZS", [types.LabeledPrice(""" “Ekstremal” tarifini xarid qilish""", 199000*100)])

    if callback.data == "Pey Me Ekstremal":
        bot.send_invoice(callback.message.chat.id, """Pey Me xizmatidan foydalangan holda “Ekstremal” tarifini xarid qilish""", """ “Ekstremal” tarifini xarid qilish""", "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice(""" “Ekstremal” tarifini xarid qilish""", 199000*100)])

    if callback.data == "🇺🇿O'zbekcha":
        
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Reklama berish🛍", callback_data="Reklama berish🛍"))
        markup.add(types.InlineKeyboardButton("Boshqa savol bo'yicha yordam kerak❓", callback_data="Boshqa savol bo'yicha yordam kerak❓"))
        user_avto_list.update({callback.message.chat.id:{"leng":"OZ"}})
        user_avto_list_UZ_RU.update({callback.message.chat.id:{"leng":"OZ"}})

        bot.send_message(callback.message.chat.id, text = "Aytingchi, sizning savolingiz nima bilan bog'liq?", reply_markup=markup)

    if callback.data == "Boshqa savol bo'yicha yordam kerak❓":
        event_help = bot.send_message(callback.message.chat.id, text = "Iltimos, xabaringizni qoldiring, biz siz bilan 24 soat ichida bog'lanamiz 🤓.")
        bot.register_next_step_handler(event_help, event_help_2)

    if callback.data == "Все верно✅":
        bot.send_message(callback.message.chat.id, text = "Для того чтобы продолжить отправьте 6 фотографий автомобиля📸.")
        leng_switcher = 1

    if callback.data == "Hammasi to'g'ri✅":
        bot.send_message(callback.message.chat.id, text = "Davom etish uchun mashinaning 6 ta fotosuratini yuboring📸.")
        leng_switcher = 2

    if callback.data == "Дать рекламное обьявление🛍":
        bot.send_message(callback.message.chat.id, text = "Пожалуйста, заполните пошагово анкету об автомобиле для рекламы о продаже 🚘.")
            
        msg_1 = bot.send_message(callback.message.chat.id, text = "Модель и марка машины:")
        bot.register_next_step_handler(msg_1, message_review_1)

    if callback.data == "Reklama berish🛍":
        bot.send_message(callback.message.chat.id, text = "Sotish haqida e'lon qilish uchun mashina haqida bosqichma-bosqich anketani to'ldiring 🚘.")
            
        msg_01 = bot.send_message(callback.message.chat.id, text = "Avtomobil modeli va markasi:")
        bot.register_next_step_handler(msg_01, message_review_01)

    if callback.data == "coment_Ru":
        event_help = bot.send_message(callback.message.chat.id, text = "Пожалуйста оставьте отзыв о нашем канале 🙏🏻:")
        bot.register_next_step_handler(event_help, event_help_3)

    if callback.data == "coment_OZ":
        event_help = bot.send_message(callback.message.chat.id, text = "Kanalimiz haqida sharh qoldiring 🙏🏻:")
        bot.register_next_step_handler(event_help, event_help_4)

    if callback.data == "Седан":
        
        user_avto_list[callback.message.chat.id].update({'Тип кузова:':"Седан"})
        bot.send_message(callback.message.chat.id, text = "Седан")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_3(callback.message)
        
    if callback.data == "Купе":
        
        user_avto_list[callback.message.chat.id].update({'Тип кузова:':"Купе"})
        bot.send_message(callback.message.chat.id, text = "Купе")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_3(callback.message)

    if callback.data == "Хэтчбек":
        
        user_avto_list[callback.message.chat.id].update({'Тип кузова:':"Хэтчбек"})
        bot.send_message(callback.message.chat.id, text = "Хэтчбек")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_3(callback.message)

    if callback.data == "Универсал":
        
        user_avto_list[callback.message.chat.id].update({'Тип кузова:':"Универсал"})
        bot.send_message(callback.message.chat.id, text = "Универсал")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_3(callback.message)

    if callback.data == "Кроссовер":
        
        user_avto_list[callback.message.chat.id].update({'Тип кузова:':"Кроссовер"})
        bot.send_message(callback.message.chat.id, text = "Кроссовер")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_3(callback.message)

    if callback.data == "Внедорожник":
        
        user_avto_list[callback.message.chat.id].update({'Тип кузова:':"Внедорожник"})
        bot.send_message(callback.message.chat.id, text = "Внедорожник")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_3(callback.message)

    if callback.data == "Другое_кузов":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_1(callback.message)

    if callback.data == "Автоматическая":
        user_avto_list[callback.message.chat.id].update({'Тип коробки передач:':"Автоматическая"})
        bot.send_message(callback.message.chat.id, text = "Автоматическая")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_14(callback.message)

    if callback.data == "Механическая":
        user_avto_list[callback.message.chat.id].update({'Тип коробки передач:':"Механическая"})
        bot.send_message(callback.message.chat.id, text = "Механическая")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_14(callback.message)

    if callback.data == "Другое_коробка":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_3(callback.message)

    if callback.data == "Черный":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Черный"})
        bot.send_message(callback.message.chat.id, text = "Черный")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Белый":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Белый"})
        bot.send_message(callback.message.chat.id, text = "Белый")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Серый":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Серый"})
        bot.send_message(callback.message.chat.id, text = "Серый")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Голубой":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Голубой"})
        bot.send_message(callback.message.chat.id, text = "Голубой")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Красный":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Красный"})
        bot.send_message(callback.message.chat.id, text = "Красный")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Синий":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Синий"})
        bot.send_message(callback.message.chat.id, text = "Синий")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Серебристый":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Серебристый"})
        bot.send_message(callback.message.chat.id, text = "Серебристый")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Бежевый":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Бежевый"})
        bot.send_message(callback.message.chat.id, text = "Бежевый")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Зеленый":
        user_avto_list[callback.message.chat.id].update({'Цвет:':"Зеленый"})
        bot.send_message(callback.message.chat.id, text = "Зеленый")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_5(callback.message)

    if callback.data == "Другой_цвет":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_5(callback.message)

    if callback.data == "Бензин":
        user_avto_list[callback.message.chat.id].update({'Вид топлива:':"Бензин"})
        bot.send_message(callback.message.chat.id, text = "Бензин")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_7(callback.message)

    if callback.data == "Газ":
        user_avto_list[callback.message.chat.id].update({'Вид топлива:':"Газ"})
        bot.send_message(callback.message.chat.id, text = "Газ")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_7(callback.message)

    if callback.data == "Электро":
        user_avto_list[callback.message.chat.id].update({'Вид топлива:':"Электро"})
        bot.send_message(callback.message.chat.id, text = "Электро")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_7(callback.message)

    if callback.data == "Гибрид":
        user_avto_list[callback.message.chat.id].update({'Вид топлива:':"Гибрид"})
        bot.send_message(callback.message.chat.id, text = "Гибрид")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_7(callback.message)
    
    if callback.data == "Газ/Бензин":
        user_avto_list[callback.message.chat.id].update({'Вид топлива:':"Газ/Бензин"})
        bot.send_message(callback.message.chat.id, text = "Газ/Бензин")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_7(callback.message)

    if callback.data == "Отличное":
        user_avto_list[callback.message.chat.id].update({'Состояние машины:':"Отличное"})
        bot.send_message(callback.message.chat.id, text = "Отличное")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_8(callback.message)

    if callback.data == "Хорошее":
        user_avto_list[callback.message.chat.id].update({'Состояние машины:':"Хорошее"})
        bot.send_message(callback.message.chat.id, text = "Хорошее")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_8(callback.message)

    if callback.data == "Среднее":
        user_avto_list[callback.message.chat.id].update({'Состояние машины:':"Среднее"})
        bot.send_message(callback.message.chat.id, text = "Среднее")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_8(callback.message)

    if callback.data == "Требует ремонта":
        user_avto_list[callback.message.chat.id].update({'Состояние машины:':"Требует ремонта"})
        bot.send_message(callback.message.chat.id, text = "Требует ремонта")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_8(callback.message)

    if callback.data == "1_владелец":
        user_avto_list[callback.message.chat.id].update({'Количество владельцев:':"1"})
        bot.send_message(callback.message.chat.id, text = "1")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_9(callback.message)

    if callback.data == "2_владелец":
        user_avto_list[callback.message.chat.id].update({'Количество владельцев:':"2"})
        bot.send_message(callback.message.chat.id, text = "2")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_9(callback.message)
    
    if callback.data == "3_владелец":
        user_avto_list[callback.message.chat.id].update({'Количество владельцев:':"3"})
        bot.send_message(callback.message.chat.id, text = "3")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_9(callback.message)

    if callback.data == "Другое_владелец":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_7(callback.message)

    if callback.data == "Наличными":
        user_avto_list[callback.message.chat.id].update({'Вид оплаты:':"Наличными"})
        bot.send_message(callback.message.chat.id, text = "Наличными")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_111(callback.message)

    if callback.data == "Лизинг":
        user_avto_list[callback.message.chat.id].update({'Вид оплаты:':"Лизинг"})
        bot.send_message(callback.message.chat.id, text = "Лизинг")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_111(callback.message)

    if callback.data == "Перечисление":
        user_avto_list[callback.message.chat.id].update({'Вид оплаты:':"Перечисление"})
        bot.send_message(callback.message.chat.id, text = "Перечисление")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_111(callback.message)

    if callback.data == "Кредит":
        user_avto_list[callback.message.chat.id].update({'Вид оплаты:':"Кредит"})
        bot.send_message(callback.message.chat.id, text = "Кредит")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_111(callback.message)

    if callback.data == "Рассрочка":
        user_avto_list[callback.message.chat.id].update({'Вид оплаты:':"Рассрочка"})
        bot.send_message(callback.message.chat.id, text = "Рассрочка")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_111(callback.message)

    if callback.data == "Ташкент":
        user_avto_list[callback.message.chat.id].update({'Город:':"Ташкент"})
        bot.send_message(callback.message.chat.id, text = "Ташкент")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_11(callback.message)

    if callback.data == "Самарканд":
        user_avto_list[callback.message.chat.id].update({'Город:':"Самарканд"})
        bot.send_message(callback.message.chat.id, text = "Самарканд")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_11(callback.message)

    if callback.data == "Андижан":
        user_avto_list[callback.message.chat.id].update({'Город:':"Андижан"})
        bot.send_message(callback.message.chat.id, text = "Андижан")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_11(callback.message)

    if callback.data == "Фергана":
        user_avto_list[callback.message.chat.id].update({'Город:':"Фергана"})
        bot.send_message(callback.message.chat.id, text = "Фергана")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_11(callback.message)

    if callback.data == "Бухара":
        user_avto_list[callback.message.chat.id].update({'Город:':"Бухара"})
        bot.send_message(callback.message.chat.id, text = "Бухара")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_11(callback.message)

    if callback.data == "Другой_город":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_9(callback.message)

    if callback.data == "Sedan":
        
        user_avto_list[callback.message.chat.id].update({'Tana turi:':"Sedan"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Тип кузова:':"Седан"})
        bot.send_message(callback.message.chat.id, text = "Sedan")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_03(callback.message)
        
    if callback.data == "Kupe":
        
        user_avto_list[callback.message.chat.id].update({'Tana turi:':"Kupe"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Тип кузова:':"Купе"})
        bot.send_message(callback.message.chat.id, text = "Kupe")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_03(callback.message)

    if callback.data == "Xetchbek":
        
        user_avto_list[callback.message.chat.id].update({'Tana turi:':"Xetchbek"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Тип кузова:':"Хэтчбек"})
        bot.send_message(callback.message.chat.id, text = "Xetchbek")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_03(callback.message)

    if callback.data == "Stansiya vagoni":
        
        user_avto_list[callback.message.chat.id].update({'Tana turi:':"Stansiya vagoni"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Тип кузова:':"Универсал"})
        bot.send_message(callback.message.chat.id, text = "Stansiya vagoni")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_03(callback.message)

    if callback.data == "Krossover":
        
        user_avto_list[callback.message.chat.id].update({'Tana turi:':"Krossover"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Тип кузова:':"Кроссовер"})
        bot.send_message(callback.message.chat.id, text = "Krossover")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_03(callback.message)

    if callback.data == "SUV":
        
        user_avto_list[callback.message.chat.id].update({'Tana turi:':"SUV"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Тип кузова:':"Внедорожник"})
        bot.send_message(callback.message.chat.id, text = "SUV")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_03(callback.message)

    if callback.data == "Boshqa_кузов":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_01(callback.message)

    if callback.data == "Avtomatik":
        user_avto_list[callback.message.chat.id].update({'Vites qutisi turi:':"Avtomatik"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Тип коробки передач:':"Автоматическая"})
        bot.send_message(callback.message.chat.id, text = "Avtomatik")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_014(callback.message)

    if callback.data == "qo'lda uzatish":
        user_avto_list[callback.message.chat.id].update({'Vites qutisi turi:':"qo'lda uzatish"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Тип коробки передач:':"Механическая"})
        bot.send_message(callback.message.chat.id, text = "qo'lda uzatish")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_014(callback.message)

    if callback.data == "Boshqa_коробка":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_03(callback.message)

    if callback.data == "Qora":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Qora"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Черный"})
        bot.send_message(callback.message.chat.id, text = "Qora")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Oq":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Oq"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Белый"})
        bot.send_message(callback.message.chat.id, text = "Oq")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Kulrang":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Kulrang"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Серый"})
        bot.send_message(callback.message.chat.id, text = "Kulrang")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Moviy":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Moviy"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Голубой"})
        bot.send_message(callback.message.chat.id, text = "Moviy")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Qizil":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Qizil"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Красный"})
        bot.send_message(callback.message.chat.id, text = "Qizil")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Moviy":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Moviy"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Синий"})
        bot.send_message(callback.message.chat.id, text = "Moviy")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Bej":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Bej"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Серебристый"})
        bot.send_message(callback.message.chat.id, text = "Bej")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Kumush":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Kumush"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Бежевый"})
        bot.send_message(callback.message.chat.id, text = "Kumush")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Yashil":
        user_avto_list[callback.message.chat.id].update({'Rang:':"Yashil"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Цвет:':"Зеленый"})
        bot.send_message(callback.message.chat.id, text = "Yashil")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_05(callback.message)

    if callback.data == "Boshqa_цвет":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_05(callback.message)

    if callback.data == "Benzin":
        user_avto_list[callback.message.chat.id].update({"Yoqilg'i turi:":"Benzin"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид топлива:':"Бензин"})
        bot.send_message(callback.message.chat.id, text = "Benzin")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_07(callback.message)

    if callback.data == "Gaz":
        user_avto_list[callback.message.chat.id].update({"Yoqilg'i turi:":"Gaz"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид топлива:':"Газ"})
        bot.send_message(callback.message.chat.id, text = "Gaz")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_07(callback.message)

    if callback.data == "Elektro":
        user_avto_list[callback.message.chat.id].update({"Yoqilg'i turi:":"Elektro"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид топлива:':"Электро"})
        bot.send_message(callback.message.chat.id, text = "Elektro")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_07(callback.message)

    if callback.data == "Gibrid":
        user_avto_list[callback.message.chat.id].update({"Yoqilg'i turi:":"Gibrid"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид топлива:':"Гибрид"})
        bot.send_message(callback.message.chat.id, text = "Gibrid")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_07(callback.message)
    
    if callback.data == "Gaz/Benzin":
        user_avto_list[callback.message.chat.id].update({"Yoqilg'i turi:":"Gaz/Benzin"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид топлива:':"Газ/Бензин"})
        bot.send_message(callback.message.chat.id, text = "Gaz/Benzin")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_07(callback.message)

    if callback.data == "A’lo":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Состояние машины:':"Отличное"})
        user_avto_list[callback.message.chat.id].update({'Mashina holati:':"A’lo"})
        bot.send_message(callback.message.chat.id, text = "A’lo")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_08(callback.message)

    if callback.data == "Yaxshi":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Состояние машины:':"Хорошее"})
        user_avto_list[callback.message.chat.id].update({'Mashina holati:':"Yaxshi"})
        bot.send_message(callback.message.chat.id, text = "Yaxshi")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_08(callback.message)

    if callback.data == "O'rtacha":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Состояние машины:':"Среднее"})
        user_avto_list[callback.message.chat.id].update({'Mashina holati:':"O'rtacha"})
        bot.send_message(callback.message.chat.id, text = "O'rtacha")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_08(callback.message)

    if callback.data == "Ta'mirlash kerak":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Состояние машины:':"Требует ремонта"})
        user_avto_list[callback.message.chat.id].update({'Mashina holati:':"Ta'mirlash kerak"})
        bot.send_message(callback.message.chat.id, text = "Ta'mirlash kerak")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_08(callback.message)

    if callback.data == "1_":
        user_avto_list[callback.message.chat.id].update({'Egalari soni:':"1"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Количество владельцев:':"1"})
        bot.send_message(callback.message.chat.id, text = "1")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_09(callback.message)

    if callback.data == "2_":
        user_avto_list[callback.message.chat.id].update({'Egalari soni:':"2"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Количество владельцев:':"2"})
        bot.send_message(callback.message.chat.id, text = "2")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_09(callback.message)
    
    if callback.data == "3_":
        user_avto_list[callback.message.chat.id].update({'Egalari soni:':"3"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Количество владельцев:':"3"})
        bot.send_message(callback.message.chat.id, text = "3")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_09(callback.message)

    if callback.data == "Boshqa_влад":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_07(callback.message)

    if callback.data == "Toshkent":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Город:':"Ташкент"})
        user_avto_list[callback.message.chat.id].update({'Shahar:':"Toshkent"})
        bot.send_message(callback.message.chat.id, text = "Toshkent")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_011(callback.message)

    if callback.data == "Samarqand":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Город:':"Самарканд"})
        user_avto_list[callback.message.chat.id].update({'Shahar:':"Samarqand"})
        bot.send_message(callback.message.chat.id, text = "Samarqand")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_011(callback.message)

    if callback.data == "Andijon":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Город:':"Андижан"})
        user_avto_list[callback.message.chat.id].update({'Shahar:':"Andijon"})
        bot.send_message(callback.message.chat.id, text = "Andijon")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_011(callback.message)

    if callback.data == "Farg'ona":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Город:':"Фергана"})
        user_avto_list[callback.message.chat.id].update({'Shahar:':"Farg'ona"})
        bot.send_message(callback.message.chat.id, text = "Farg'ona")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_011(callback.message)

    if callback.data == "Buxoro":
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Город:':"Бухара"})
        user_avto_list[callback.message.chat.id].update({'Shahar:':"Buxoro"})
        bot.send_message(callback.message.chat.id, text = "Buxoro")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_011(callback.message)

    if callback.data == "Boshqa_город":
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        message_review_none_09(callback.message)

    if callback.data == "Naqd pul":
        user_avto_list[callback.message.chat.id].update({'Toʻlov shakli:':"Naqd pul"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид оплаты:':"Наличными"})
        bot.send_message(callback.message.chat.id, text = "Naqd pul")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_0111(callback.message)

    if callback.data == "Lizing":
        user_avto_list[callback.message.chat.id].update({'Toʻlov shakli:':"Lizing"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид оплаты:':"Лизинг"})
        bot.send_message(callback.message.chat.id, text = "Lizing")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_0111(callback.message)

    if callback.data == "Perechisleniye":
        user_avto_list[callback.message.chat.id].update({'Toʻlov shakli:':"Perechisleniye"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид оплаты:':"Перечисление"})
        bot.send_message(callback.message.chat.id, text = "Perechisleniye")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_0111(callback.message)

    if callback.data == "Kredit":
        user_avto_list[callback.message.chat.id].update({'Toʻlov shakli:':"Kredit"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид оплаты:':"Кредит"})
        bot.send_message(callback.message.chat.id, text = "Kredit")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_0111(callback.message)

    if callback.data == "Rassrochka":
        user_avto_list[callback.message.chat.id].update({'Toʻlov shakli:':"Rassrochka"})
        user_avto_list_UZ_RU[callback.message.chat.id].update({'Вид оплаты:':"Рассрочка"})
        bot.send_message(callback.message.chat.id, text = "Rassrochka")
        bot.edit_message_reply_markup(callback.message.chat.id, message_id = callback.message.message_id, reply_markup = None)
        message_review_0111(callback.message)

def event_help_1(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дать рекламное обьявление🛍", callback_data="Дать рекламное обьявление🛍"))
    markup.add(types.InlineKeyboardButton("Нужна помощь с другим вопросом❓", callback_data="Нужна помощь с другим вопросом❓"))

    bot.send_message("#", text = f"{message.text} Имя пользователя: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------
    bot.send_message(message.chat.id, text = "Сообщение было отправлено с вами скоро свяжеться администратор.", reply_markup=markup)

def event_help_2(message):
    bot.send_message("#", text = f"{message.text} Foydalanuvchi nomi: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------
    bot.send_message(message.chat.id, text = "Xabar yuborildi, administrator tez orada siz bilan bog'lanadi.")

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True, error_message="Toʻlov amalga oshmadi – qayta urinib koʻring yoki bot administratoriga murojaat qiling.\n\n--------------------------\n\nОплата не прошла - попробуйте пожалуйста е ще раз, или свяжитесь с администратором бота.")

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):

    try:
        var = len(users_advetesment[message.chat.id])
        users_advetesment[message.chat.id].update({var+1:user_avto_list[message.chat.id]["Модель и марка машины:"]})

    except Exception as err:
        var = len(users_advetesment[message.chat.id])
        users_advetesment[message.chat.id].update({var+1:user_avto_list[message.chat.id]["Avtomobil modeli va markasi:"]})


    bot.send_message("#", f"""Клиет купил тариф: {terif} Имя пользователя @{message.from_user.username}""")

    if user_avto_list[message.chat.id]['leng'] == "RU":

        bot.send_media_group("#", [telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_1:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_2:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_3:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_4:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_5:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_6:"], f"""🔥{user_avto_list[message.chat.id]["Модель и марка машины:"]}-{user_avto_list[message.chat.id]["Цена:"]}🔥\n\n▪️Модель и марка машины: {user_avto_list[message.chat.id]["Модель и марка машины:"]}\n▪️Цена: {user_avto_list[message.chat.id]["Цена:"]}\n▪️Тип кузова: {user_avto_list[message.chat.id]["Тип кузова:"]}\n▪️Год выпуска: {user_avto_list[message.chat.id]["Год выпуска:"]}\n▪️Пробег: {user_avto_list[message.chat.id]["Пробег:"]}\n▪️Тип коробки передач: {user_avto_list[message.chat.id]["Тип коробки передач:"]}\n▪️Цвет: {user_avto_list[message.chat.id]["Цвет:"]}\n▪️Объем двигателя: {user_avto_list[message.chat.id]["Объем двигателя:"]}\n▪️Вид топлива: {user_avto_list[message.chat.id]["Вид топлива:"]}\n▪️Состояние машины: {user_avto_list[message.chat.id]["Состояние машины:"]}\n▪️Количество владельцев: {user_avto_list[message.chat.id]["Количество владельцев:"]}\n▪️Телефон для связи: {user_avto_list[message.chat.id]["Телефон для связи:"]}\n▪️Город: {user_avto_list[message.chat.id]["Город:"]}\n▪️Вид оплаты: {user_avto_list[message.chat.id]["Вид оплаты:"]}""")])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Сообщить о продаже машины 🚘")
        btn2 = types.KeyboardButton("Дать рекламное обьявление 🛍")
        btn3 = types.KeyboardButton("Нужна помощь с другим вопросом ❓")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, """Спасибо за доверие! Ваше объявление о продаже автомобиля будет опубликовано в кратчайшие сроки.\n\nПожалуйста, сообщите нам после продажи автомобиля 🙏🏻\n\nЕсли ваш пост не будет опубликован в течении 24 часов, прошу связаться с Админом.""", reply_markup=markup)
        bot.send_message(message.chat.id, text = f"Мы активно развиваем наш канал AvtoMarket Uzbekistan, и будем очень признательны, если вы поделитесь ссылкой с друзьями и близкими на наш канал!\n\nСсылка на канал:\n\n• {link_1}\n• {link_2}\n• {link_3}\n• {link_4}", parse_mode='HTML')

    if user_avto_list[message.chat.id]["leng"] == "OZ":
        
        bot.send_media_group("#", [telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[message.chat.id]["Foto_1:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[message.chat.id]["Foto_2:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[message.chat.id]["Foto_3:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[message.chat.id]["Foto_4:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[message.chat.id]["Foto_5:"]), telebot.types.InputMediaPhoto(user_avto_list_UZ_RU[message.chat.id]["Foto_6:"], f"""🔥{user_avto_list_UZ_RU[message.chat.id]["Модель и марка машины:"]}-{user_avto_list_UZ_RU[message.chat.id]["Цена:"]}🔥\n\n▪️Модель и марка машины: {user_avto_list_UZ_RU[message.chat.id]["Модель и марка машины:"]}\n▪️Цена: {user_avto_list_UZ_RU[message.chat.id]["Цена:"]}\n▪️Тип кузова: {user_avto_list_UZ_RU[message.chat.id]["Тип кузова:"]}\n▪️Год выпуска: {user_avto_list_UZ_RU[message.chat.id]["Год выпуска:"]}\n▪️Пробег: {user_avto_list_UZ_RU[message.chat.id]["Пробег:"]}\n▪️Тип коробки передач: {user_avto_list_UZ_RU[message.chat.id]["Тип коробки передач:"]}\n▪️Цвет: {user_avto_list_UZ_RU[message.chat.id]["Цвет:"]}\n▪️Объем двигателя: {user_avto_list_UZ_RU[message.chat.id]["Объем двигателя:"]}\n▪️Вид топлива: {user_avto_list_UZ_RU[message.chat.id]["Вид топлива:"]}\n▪️Состояние машины: {user_avto_list_UZ_RU[message.chat.id]["Состояние машины:"]}\n▪️Количество владельцев: {user_avto_list_UZ_RU[message.chat.id]["Количество владельцев:"]}\n▪️Телефон для связи: {user_avto_list_UZ_RU[message.chat.id]["Телефон для связи:"]}\n▪️Город: {user_avto_list_UZ_RU[message.chat.id]["Город:"]}\n▪️Вид оплаты: {user_avto_list_UZ_RU[message.chat.id]["Вид оплаты:"]}""")])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Avtomobil sotilgani haqida xabar bering 🚘")
        btn2 = types.KeyboardButton("E'lon qo'ying 🛍")
        btn3 = types.KeyboardButton("Boshqa savol bo'yicha yordam kerak ❓")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, """Spasibo za doverie! Vashe ob'yavlenie o prodaje avtomobilya budet opublikovano v kratchayshie sroki.\n\nPojaluysta, soobshchite nam posle prodaji avtomobilya 🙏🏻\n\nEsli vash post ne budet opublikovan v techenii 24 soat, proshu svyazatsya s Administratorom.""", reply_markup=markup)
        bot.send_message(message.chat.id, text = f"My aktivno razvivaem nash kanal AvtoMarket Uzbekistan, i budem ochen priznatelny, esli vy podelites ssylkoy s druzyami i blizkimi na nash kanal!\n\nSsylka na kanal:\n\n• {link_1}\n• {link_2}\n• {link_3}\n• {link_4}", parse_mode='HTML')

@bot.message_handler(content_types=['text'])
def button_message(message):

    if message.text == "Сообщить о продаже машины 🚘":
        markup = types.InlineKeyboardMarkup()
        
        for i in range(0, len(users_advetesment[message.chat.id])):
            print(i)
            if i != 0:
                markup.add(types.InlineKeyboardButton(f"{users_advetesment[message.chat.id][i+1]}", callback_data="coment_Ru"))

        bot.send_message(message.chat.id, text = "Выберете автотомобиль который был продан", reply_markup=markup)

    if message.text == "Avtomobil sotilgani haqida xabar bering 🚘":

        markup = types.InlineKeyboardMarkup()
        
        for i in range(0, len(users_advetesment[message.chat.id])):
            print(i)
            if i != 0:
                markup.add(types.InlineKeyboardButton(f"{users_advetesment[message.chat.id][i+1]}", callback_data="coment_OZ"))

        bot.send_message(message.chat.id, text = "Выберете автотомобиль который был продан", reply_markup=markup)

    if message.text == "Дать рекламное обьявление 🛍":
        bot.send_message(message.chat.id, text = "Пожалуйста, заполните пошагово анкету об автомобиле для рекламы о продаже 🚘.")
            
        msg_1 = bot.send_message(message.chat.id, text = "Модель и марка машины:")
        bot.register_next_step_handler(msg_1, message_review_1)

    if message.text == "Нужна помощь с другим вопросом ❓":
        event_help = bot.send_message(message.chat.id, text = "Пожалуйста оставьте свое сообщение и в течении 24 часов мы свяжемся с вами 🤓.")
        bot.register_next_step_handler(event_help, event_help_1)

    if message.text == "Boshqa savol bo'yicha yordam kerak ❓":
        event_help = bot.send_message(message.chat.id, text = "Iltimos, xabaringizni qoldiring, biz siz bilan 24 soat ichida bog'lanamiz 🤓.")
        bot.register_next_step_handler(event_help, event_help_2)

    if message.text == "E'lon qo'ying 🛍":
        bot.send_message(message.chat.id, text = "Sotish haqida e'lon qilish uchun mashina haqida bosqichma-bosqich anketani to'ldiring 🚘.")
            
        msg_01 = bot.send_message(message.chat.id, text = "Avtomobil modeli va markasi:")
        bot.register_next_step_handler(msg_01, message_review_01)
        
def event_help_3(message):

    bot.send_message("#", text = f"Отзыв о продаже автомобиля : {message.text} имя пользователя: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------

    try:
        del user_avto_list_UZ_RU[message.chat.id]
        print(user_avto_list_UZ_RU)
    except Exception as err:
        print(user_avto_list_UZ_RU)

    try:
        del user_avto_list[message.chat.id]
        print(user_avto_list)
    except Exception as err:
        print(user_avto_list)

    user_avto_list.update({message.chat.id:{"leng":"RU"}})
    user_avto_list_UZ_RU.update({message.chat.id:{"leng":"RU"}})
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text = "Благодарим вас за отзыв! Мы будем рады видеть вас снова и будем признательны, если вы порекомендуете наш канал другим 🙏🏻.", reply_markup=a)
    start_message(message)


def event_help_4(message):
    bot.send_message("#", text = f"Отзыв: {message.text} имя пользователя: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------
    a = telebot.types.ReplyKeyboardRemove()
    
    try:
        del user_avto_list_UZ_RU[message.chat.id]
        print(user_avto_list_UZ_RU)
    except Exception as err:
        print(user_avto_list_UZ_RU)

    try:
        del user_avto_list[message.chat.id]
        print(user_avto_list)
    except Exception as err:
        print(user_avto_list)

    user_avto_list.update({message.chat.id:{"leng":"OZ"}})
    user_avto_list_UZ_RU.update({message.chat.id:{"leng":"OZ"}})
    bot.send_message(message.chat.id, text = "Fikr-mulohazangiz uchun rahmat! Sizni yana ko'rganimizdan xursand bo'lamiz va kanalimizni boshqalarga tavsiya qilsangiz minnatdor bo'lamiz 🙏🏻.", reply_markup=a)
    start_message(message)

@bot.message_handler(content_types=['photo'])
def photo_message(message):
    global counter, leng_switcher
    if message.chat.id in user_avto_list and counter<=6:
        counter += 1
        user_avto_list[message.chat.id].update({f'Foto_{counter}:':message.photo[-1].file_id})
        user_avto_list_UZ_RU[message.chat.id].update({f'Foto_{counter}:':message.photo[-1].file_id})
        
    if counter == 6:
        bot.send_message("#", text = f'Клиент ознакомился с планом\n\nЮзернейм: @{message.from_user.username}')
        print(user_avto_list)

    if counter == 6 and leng_switcher == 1:
        counter = 0
        leng_switcher = 0

        markup = types.InlineKeyboardMarkup()

        try:
            print(free_addvetesment[message.chat.id]["free-advetesment"])
        except Exception as err:
            markup.add(types.InlineKeyboardButton("БЕСПЛАТНОЕ объявление по Акции 🔉", callback_data="БЕСПЛАТНОЕ объявление  по Акции 🔉"))

        markup.add(types.InlineKeyboardButton("Эконом🔵", callback_data="Эконом"))
        markup.add(types.InlineKeyboardButton("Стандарт🟢", callback_data="Стандарт"))
        markup.add(types.InlineKeyboardButton("Премиум🟣", callback_data="Премиум"))
        markup.add(types.InlineKeyboardButton("Элитный🟡", callback_data="Элитный"))
        markup.add(types.InlineKeyboardButton("Эксклюзив🟠", callback_data="Эксклюзив"))
        markup.add(types.InlineKeyboardButton("Экстрим🔴", callback_data="Экстрим"))

        bot.send_message(message.chat.id, text = """Пожалуйста выберите тарифный план: \n\n49.000 - Тариф "Эконом"\n● Публикация вашего автомобиля 2 раза по вашему выбору в любое удобное время\n\n59.000 - Тариф "Стандарт"\n● Публикация вашего автомобиля 4 раза по вашему выбору в любое удобное время\n\n69.000 - Тариф "Премиум"\n● Публикация вашего автомобиля 6 раз по вашему выбору в любое удобное время + Закрепление на 3 дня\n\n89.000 - Тариф "Элитный"\n● Публикация вашего автомобиля 8 раз по вашему выбору в любое удобное время + Закрепление на 10 дней\n\n129.000 - Тариф "Эксклюзив"\n● Публикация вашего автомобиля 12 раз по вашему выбору в любое удобное время + Закрепление на 30 дней (возможно установить время для автоматической публикации)\n\n199.000 - Тариф "Экстрим"\n● Публикация вашего автомобиля через день в течение месяца + закрепление до момента продажи\n\n❗️ ПРИ ПОКУПКЕ ЛЮБОГО ТАРИФА - ВАШ АВТОМОБИЛЬ НЕ УДАЛЯЕТСЯ ДО МОМЕНТА ПРОДАЖИ.""", reply_markup=markup)

    if counter == 6 and leng_switcher == 2:
        counter = 0
        leng_switcher = 0

        markup = types.InlineKeyboardMarkup()

        try:
            print(free_addvetesment[message.chat.id]["free-advetesment"])
        except Exception as err:
            markup.add(types.InlineKeyboardButton("BESPLATNOE ob'yavlenie po Aktsii 🔉", callback_data="БЕСПЛАТНОЕ объявление  по Акции 🔉"))

        markup.add(types.InlineKeyboardButton("Iqtisodiyot🔵", callback_data="Iqtisodiyot"))
        markup.add(types.InlineKeyboardButton("Standart🟢", callback_data="Standart"))
        markup.add(types.InlineKeyboardButton("Premium🟣", callback_data="Premium"))
        markup.add(types.InlineKeyboardButton("Elite🟡", callback_data="Elite"))
        markup.add(types.InlineKeyboardButton("Eksklyuziv🟠", callback_data="Eksklyuziv"))
        markup.add(types.InlineKeyboardButton("Ekstremal🔴", callback_data="Ekstremal"))

        bot.send_message(message.chat.id, text = """Tarif rejasini tanlang: \n\n49.000 - "Iqtisodiyot" tarifi\n● Oʻzingiz tanlagan avtomashinani istalgan vaqtda 2 marta chop etish\n\n59.000 - “Standart” tarifi\n● Oʻzingizning maʼlumotingizni eʼlon qilish. avtomashina ixtiyoriy qulay vaqtda 4 marta siz tanlagan holda\n\n69.000 - "Premium" tarifi\n● O'zingiz tanlagan avtomashinani istalgan vaqtda 6 marta nashr qilish + 3 kunga topshiriq\n\n89.000 - "Elite” tarifi\n● Oʻzingiz tanlagan avtomobilingizni 8 marta istalgan qulay vaqtda chop etish + 10 kunga tayinlash\n\n129.000 - “Eksklyuziv” tarifi\n● Oʻzingiz xohlagan qulay vaqtda avtomobilingizni 12 marta nashr qilish vaqt + 30 kunga tayinlash (avtomatik nashr qilish vaqtini belgilash mumkin)\n\n199.000 - "Ekstremal" tarifi\n● Avtomobilingizni bir oy davomida har kuni chop etish + sotuvga qadar kafolatlash\n\n❗️ HAR QANDAY TARIF SOTISHDA - AVTOMOBILINGIZ SOTISH NOKTAGACHA O‘CHIRILMAYDI.""", reply_markup=markup)

def message_review_01(message):

    if message.text == "/start":
        start_message()

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Avtomobil modeli va markasi:':mesage_to_save})

    user_avto_list_UZ_RU[message.chat.id].update({'Модель и марка машины:':mesage_to_save})

    msg_02 = bot.send_message(message.chat.id, text = "Narxi:")
    bot.register_next_step_handler(msg_02, message_review_02)

def message_review_02(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Narxi:':mesage_to_save})

    user_avto_list_UZ_RU[message.chat.id].update({'Цена:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Sedan", callback_data="Sedan"))
    markup.add(types.InlineKeyboardButton("Kupe", callback_data="Kupe"))
    markup.add(types.InlineKeyboardButton("Xetchbek", callback_data="Xetchbek"))
    markup.add(types.InlineKeyboardButton("Stansiya vagoni", callback_data="Stansiya vagoni"))
    markup.add(types.InlineKeyboardButton("Krossover", callback_data="Krossover"))
    markup.add(types.InlineKeyboardButton("SUV", callback_data="SUV"))
    markup.add(types.InlineKeyboardButton("Boshqa", callback_data="Boshqa_кузов"))

    bot.send_message(message.chat.id, text = "Tana turi:", reply_markup=markup)

def message_review_none_01(message):

    if message.text == "/start":
        start_message(message)

    msg_none_01 = bot.send_message(message.chat.id, text = "Tana turi:")
    bot.register_next_step_handler(msg_none_01, message_review_none_02)

def message_review_none_02(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Tana turi:':mesage_to_save})
    user_avto_list_UZ_RU[message.chat.id].update({'Тип кузова:':mesage_to_save})

    msg_none_02 = bot.send_message(message.chat.id, text = "Ishlab chiqarilgan yili:")
    bot.register_next_step_handler(msg_none_02, message_review_013)

def message_review_03(message):

    if message.text == "/start":
        start_message(message)
    
    msg_013 = bot.send_message(message.chat.id, text = "Ishlab chiqarilgan yili:")
    bot.register_next_step_handler(msg_013, message_review_013)

def message_review_013(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Ishlab chiqarilgan yili:':mesage_to_save})
    user_avto_list_UZ_RU[message.chat.id].update({'Пробег:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Avtomatik", callback_data="Avtomatik"))
    markup.add(types.InlineKeyboardButton("qo'lda uzatish", callback_data="qo'lda uzatish"))
    markup.add(types.InlineKeyboardButton("Boshqa", callback_data="Boshqa_коробка"))

    bot.send_message(message.chat.id, text = "Vites qutisi turi:", reply_markup=markup)

def message_review_none_03(message):

    if message.text == "/start":
        start_message(message)

    msg_none_03 = bot.send_message(message.chat.id, text = "Tana turi:")
    bot.register_next_step_handler(msg_none_03, message_review_none_04)

def message_review_none_04(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Vites qutisi turi:':mesage_to_save})
    user_avto_list_UZ_RU[message.chat.id].update({'Тип коробки передач:':mesage_to_save})

    msg_none_04 = bot.send_message(message.chat.id, text = "Chiqarilgan yili:")
    bot.register_next_step_handler(msg_none_04, message_review_04)

def message_review_014(message):

    if message.text == "/start":
        start_message(message)

    msg_04 = bot.send_message(message.chat.id, text = "Chiqarilgan yili:")
    bot.register_next_step_handler(msg_04, message_review_04)

def message_review_04(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Chiqarilgan yili:':mesage_to_save})

    user_avto_list_UZ_RU[message.chat.id].update({'Год выпуска:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Qora", callback_data="Qora"))
    markup.add(types.InlineKeyboardButton("Oq", callback_data="Oq"))
    markup.add(types.InlineKeyboardButton("Kulrang", callback_data="Kulrang"))
    markup.add(types.InlineKeyboardButton("Moviy", callback_data="Moviy"))
    markup.add(types.InlineKeyboardButton("Qizil", callback_data="Qizil"))
    markup.add(types.InlineKeyboardButton("Moviy", callback_data="Moviy"))
    markup.add(types.InlineKeyboardButton("Bej", callback_data="Bej"))
    markup.add(types.InlineKeyboardButton("Kumush", callback_data="Kumush"))
    markup.add(types.InlineKeyboardButton("Yashil", callback_data="Yashil"))
    markup.add(types.InlineKeyboardButton("Boshqa", callback_data="Boshqa_цвет"))

    bot.send_message(message.chat.id, text = "Rang:", reply_markup=markup)

def message_review_none_05(message):

    if message.text == "/start":
        start_message(message)

    msg_none_03 = bot.send_message(message.chat.id, text = "Rang:")
    bot.register_next_step_handler(msg_none_03, message_review_none_05)

def message_review_none_06(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Rang:':mesage_to_save})
    user_avto_list_UZ_RU[message.chat.id].update({'Цвет:':mesage_to_save})

    msg_none_04 = bot.send_message(message.chat.id, text = "Dvigatel hajmi:")
    bot.register_next_step_handler(msg_none_04, message_review_06)

def message_review_05(message):

    if message.text == "/start":
        start_message(message)

    msg_06 = bot.send_message(message.chat.id, text = "Dvigatel hajmi:")
    bot.register_next_step_handler(msg_06, message_review_06)

def message_review_06(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Dvigatel hajmi:':mesage_to_save})

    user_avto_list_UZ_RU[message.chat.id].update({'Объем двигателя:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Benzin", callback_data="Benzin"))
    markup.add(types.InlineKeyboardButton("Gaz", callback_data="Gaz"))
    markup.add(types.InlineKeyboardButton("Elektro", callback_data="Elektro"))
    markup.add(types.InlineKeyboardButton("Gibrid", callback_data="Gibrid"))
    markup.add(types.InlineKeyboardButton("Gaz/Benzin", callback_data="Gaz/Benzin"))

    bot.send_message(message.chat.id, text = "Yoqilg'i turi:", reply_markup=markup)

def message_review_07(message):

    if message.text == "/start":
        start_message(message)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("A’lo", callback_data="A’lo"))
    markup.add(types.InlineKeyboardButton("Yaxshi", callback_data="Yaxshi"))
    markup.add(types.InlineKeyboardButton("O'rtacha", callback_data="O'rtacha"))
    markup.add(types.InlineKeyboardButton("Ta'mirlash kerak", callback_data="Ta'mirlash kerak"))

    bot.send_message(message.chat.id, text = "Mashina holati:", reply_markup=markup)

def message_review_08(message):

    if message.text == "/start":
        start_message(message)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("1", callback_data="1_"))
    markup.add(types.InlineKeyboardButton("2", callback_data="2_"))
    markup.add(types.InlineKeyboardButton("3", callback_data="3_"))
    markup.add(types.InlineKeyboardButton("Boshqa", callback_data="Boshqa_влад"))


    bot.send_message(message.chat.id, text = "Egalari soni:", reply_markup=markup)

def message_review_none_07(message):

    if message.text == "/start":
        start_message(message)

    msg_none_07 = bot.send_message(message.chat.id, text = "Egalari soni:")
    bot.register_next_step_handler(msg_none_07, message_review_none_08)

def message_review_none_08(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Egalari soni:':mesage_to_save})
    user_avto_list_UZ_RU[message.chat.id].update({'Количество владельцев:':mesage_to_save})

    msg_none_08 = bot.send_message(message.chat.id, text = "Aloqa telefon raqami:")
    bot.register_next_step_handler(msg_none_08, message_review_010)

def message_review_09(message):

    if message.text == "/start":
        start_message(message)

    msg_010 = bot.send_message(message.chat.id, text = "Aloqa telefon raqami:")
    bot.register_next_step_handler(msg_010, message_review_010)

def message_review_010(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Aloqa telefon raqami:':mesage_to_save})

    user_avto_list_UZ_RU[message.chat.id].update({'Телефон для связи:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Toshkent", callback_data="Toshkent"))
    markup.add(types.InlineKeyboardButton("Samarqand", callback_data="Samarqand"))
    markup.add(types.InlineKeyboardButton("Andijon", callback_data="Andijon"))
    markup.add(types.InlineKeyboardButton("Buxoro", callback_data="Buxoro"))
    markup.add(types.InlineKeyboardButton("Farg'ona", callback_data="Farg'ona"))
    markup.add(types.InlineKeyboardButton("Boshqa", callback_data="Boshqa_город"))

    bot.send_message(message.chat.id, text = "Shahar:", reply_markup=markup)


def message_review_none_09(message):

    if message.text == "/start":
        start_message(message)

    msg_none_09 = bot.send_message(message.chat.id, text = "Shahar:")
    bot.register_next_step_handler(msg_none_09, message_review_none_010)

def message_review_none_010(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Shahar:':mesage_to_save})
    user_avto_list_UZ_RU[message.chat.id].update({'Город:':mesage_to_save})

    msg_none_010 = bot.send_message(message.chat.id, text = "Toʻlov shakli:")
    bot.register_next_step_handler(msg_none_010, message_review_0111)



def message_review_011(message):

    if message.text == "/start":
        start_message(message)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Naqd pul", callback_data="Naqd pul"))
    markup.add(types.InlineKeyboardButton("Lizing", callback_data="Lizing"))
    markup.add(types.InlineKeyboardButton("Perechisleniye", callback_data="Perechisleniye"))
    markup.add(types.InlineKeyboardButton("Kredit", callback_data="Kredit"))
    markup.add(types.InlineKeyboardButton("Rassrochka (variant)", callback_data="Rassrochka"))

    bot.send_message(message.chat.id, text = "Toʻlov shakli:", reply_markup=markup)

def message_review_0111(message):

    if message.text == "/start":
        start_message(message)

    msg_0111_ = bot.send_message(message.chat.id, text = "Qo'shimcha variantlar:")
    bot.register_next_step_handler(msg_0111_, message_review_0111_)

def message_review_0111_(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({"Qo'shimcha variantlar:":mesage_to_save})

    user_avto_list_UZ_RU[message.chat.id].update({'Доп. Опции:':mesage_to_save})

    bot.send_message(message.chat.id, text = f"""🔥{user_avto_list[message.chat.id]["Avtomobil modeli va markasi:"]}-{user_avto_list[message.chat.id]["Narxi:"]}🔥\n\n▪️Avtomobil modeli va markasi: {user_avto_list[message.chat.id]["Avtomobil modeli va markasi:"]}\n▪️Narxi: {user_avto_list[message.chat.id]["Narxi:"]}\n▪️Tana turi: {user_avto_list[message.chat.id]["Tana turi:"]}\n▪️Ishlab chiqarilgan yili: {user_avto_list[message.chat.id]["Ishlab chiqarilgan yili:"]}\n▪️Vites qutisi turi: {user_avto_list[message.chat.id]["Vites qutisi turi:"]}\n▪️Chiqarilgan yili: {user_avto_list[message.chat.id]["Chiqarilgan yili:"]}\n▪️Rang: {user_avto_list[message.chat.id]["Rang:"]}\n▪️Dvigatel hajmi: {user_avto_list[message.chat.id]["Dvigatel hajmi:"]}\n▪️Yoqilg'i turi: {user_avto_list[message.chat.id]["Yoqilg'i turi:"]}\n▪️Mashina holati: {user_avto_list[message.chat.id]["Mashina holati:"]}\n▪️Egalari soni: {user_avto_list[message.chat.id]["Egalari soni:"]}\n▪️Shahar: {user_avto_list[message.chat.id]["Shahar:"]}\n▪️Toʻlov shakli: {user_avto_list[message.chat.id]["Toʻlov shakli:"]}\n▪️Aloqa telefon raqami: {user_avto_list[message.chat.id]["Aloqa telefon raqami:"]}\n\n\n▪️Qo'shimcha variantlar: {user_avto_list[message.chat.id]["Qo'shimcha variantlar:"]}""")

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Hammasi to'g'ri✅", callback_data="Hammasi to'g'ri✅"))
    markup.add(types.InlineKeyboardButton("Xato❌", callback_data="Reklama berish🛍"))

    bot.send_message(message.chat.id, text = "Iltimos, mashinangiz tafsilotlarini tekshiring🚘.", reply_markup=markup)

def message_review_1(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Модель и марка машины:':mesage_to_save})
    
    msg_2 = bot.send_message(message.chat.id, text = "Цена:")
    bot.register_next_step_handler(msg_2, message_review_2)

def message_review_2(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Цена:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Седан", callback_data="Седан"))
    markup.add(types.InlineKeyboardButton("Купе", callback_data="Купе"))
    markup.add(types.InlineKeyboardButton("Хэтчбек", callback_data="Хэтчбек"))
    markup.add(types.InlineKeyboardButton("Универсал", callback_data="Универсал"))
    markup.add(types.InlineKeyboardButton("Кроссовер", callback_data="Кроссовер"))
    markup.add(types.InlineKeyboardButton("Внедорожник", callback_data="Внедорожник"))
    markup.add(types.InlineKeyboardButton("Другое", callback_data="Другое_кузов"))

    bot.send_message(message.chat.id, text = "Тип кузова:", reply_markup=markup)

def message_review_none_1(message):

    if message.text == "/start":
        start_message(message)

    msg_none_1 = bot.send_message(message.chat.id, text = "Тип кузова:")
    bot.register_next_step_handler(msg_none_1, message_review_none_2)

def message_review_none_2(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Тип кузова:':mesage_to_save})

    msg_none_2 = bot.send_message(message.chat.id, text = "Пробег:")
    bot.register_next_step_handler(msg_none_2, message_review_13)

def message_review_3(message):

    if message.text == "/start":
        start_message(message)
    
    msg_13 = bot.send_message(message.chat.id, text = "Пробег:")
    bot.register_next_step_handler(msg_13, message_review_13)

def message_review_13(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Пробег:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Автоматическая", callback_data="Автоматическая"))
    markup.add(types.InlineKeyboardButton("Механическая", callback_data="Механическая"))
    markup.add(types.InlineKeyboardButton("Другое", callback_data="Другое_коробка"))

    bot.send_message(message.chat.id, text = "Тип коробки передач:", reply_markup=markup)

def message_review_none_3(message):

    if message.text == "/start":
        start_message(message)

    msg_none_3 = bot.send_message(message.chat.id, text = "Тип коробки передач:")
    bot.register_next_step_handler(msg_none_3, message_review_none_4)

def message_review_none_4(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Тип коробки передач:':mesage_to_save})

    msg_none_4 = bot.send_message(message.chat.id, text = "Год выпуска:")
    bot.register_next_step_handler(msg_none_4, message_review_4)

def message_review_14(message):

    if message.text == "/start":
        start_message(message)

    msg_4 = bot.send_message(message.chat.id, text = "Год выпуска:")
    bot.register_next_step_handler(msg_4, message_review_4)

def message_review_4(message):
    
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Год выпуска:':mesage_to_save})

    if message.text == "/start":
        start_message(message)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Черный", callback_data="Черный"))
    markup.add(types.InlineKeyboardButton("Белый", callback_data="Белый"))
    markup.add(types.InlineKeyboardButton("Серый", callback_data="Серый"))
    markup.add(types.InlineKeyboardButton("Голубой", callback_data="Голубой"))
    markup.add(types.InlineKeyboardButton("Красный", callback_data="Красный"))
    markup.add(types.InlineKeyboardButton("Синий", callback_data="Синий"))
    markup.add(types.InlineKeyboardButton("Бежевый", callback_data="Бежевый"))
    markup.add(types.InlineKeyboardButton("Серебристый", callback_data="Серебристый"))
    markup.add(types.InlineKeyboardButton("Зеленый", callback_data="Зеленый"))
    markup.add(types.InlineKeyboardButton("Другой", callback_data="Другой_цвет"))

    bot.send_message(message.chat.id, text = "Цвет:", reply_markup=markup)


def message_review_none_5(message):

    if message.text == "/start":
        start_message(message)

    msg_none_5 = bot.send_message(message.chat.id, text = "Цвет:")
    bot.register_next_step_handler(msg_none_5, message_review_none_6)

def message_review_none_6(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Цвет:':mesage_to_save})

    msg_none_6 = bot.send_message(message.chat.id, text = "Объем двигателя:")
    bot.register_next_step_handler(msg_none_6, message_review_6)

def message_review_5(message):

    if message.text == "/start":
        start_message(message)


    msg_6 = bot.send_message(message.chat.id, text = "Объем двигателя:")
    bot.register_next_step_handler(msg_6, message_review_6)

def message_review_6(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Объем двигателя:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Бензин", callback_data="Бензин"))
    markup.add(types.InlineKeyboardButton("Газ", callback_data="Газ"))
    markup.add(types.InlineKeyboardButton("Электро", callback_data="Электро"))
    markup.add(types.InlineKeyboardButton("Гибрид", callback_data="Гибрид"))
    markup.add(types.InlineKeyboardButton("Газ/Бензин", callback_data="Газ/Бензин"))

    bot.send_message(message.chat.id, text = "Вид топлива:", reply_markup=markup)

def message_review_7(message):

    if message.text == "/start":
        start_message(message)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Отличное", callback_data="Отличное"))
    markup.add(types.InlineKeyboardButton("Хорошее", callback_data="Хорошее"))
    markup.add(types.InlineKeyboardButton("Среднее", callback_data="Среднее"))
    markup.add(types.InlineKeyboardButton("Требует ремонта", callback_data="Требует ремонта"))

    bot.send_message(message.chat.id, text = "Состояние машины:", reply_markup=markup)

def message_review_8(message):

    if message.text == "/start":
        start_message(message)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("1", callback_data="1_владелец"))
    markup.add(types.InlineKeyboardButton("2", callback_data="2_владелец"))
    markup.add(types.InlineKeyboardButton("3", callback_data="3_владелец"))
    markup.add(types.InlineKeyboardButton("Другое", callback_data="Другое_владелец"))

    bot.send_message(message.chat.id, text = "Количество владельцев:", reply_markup=markup)

def message_review_none_7(message):

    if message.text == "/start":
        start_message(message)

    msg_none_7 = bot.send_message(message.chat.id, text = "Количество владельцев:")
    bot.register_next_step_handler(msg_none_7, message_review_none_8)

def message_review_none_8(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Количество владельцев:':mesage_to_save})

    msg_none_8 = bot.send_message(message.chat.id, text = "Телефон для связи:")
    bot.register_next_step_handler(msg_none_8, message_review_10)

def message_review_9(message):

    if message.text == "/start":
        start_message(message)

    msg_10 = bot.send_message(message.chat.id, text = "Телефон для связи:")
    bot.register_next_step_handler(msg_10, message_review_10)

def message_review_10(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Телефон для связи:':mesage_to_save})

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Ташкент", callback_data="Ташкент"))
    markup.add(types.InlineKeyboardButton("Самарканд", callback_data="Самарканд"))
    markup.add(types.InlineKeyboardButton("Андижан", callback_data="Андижан"))
    markup.add(types.InlineKeyboardButton("Фергана", callback_data="Фергана"))
    markup.add(types.InlineKeyboardButton("Бухара", callback_data="Бухара"))
    markup.add(types.InlineKeyboardButton("Другой", callback_data="Другой_город"))

    bot.send_message(message.chat.id, text = "Город:", reply_markup=markup)

def message_review_none_9(message):

    if message.text == "/start":
        start_message(message)

    msg_none_9 = bot.send_message(message.chat.id, text = "Город:")
    bot.register_next_step_handler(msg_none_9, message_review_none_10)

def message_review_none_10(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Город:':mesage_to_save})

    message_review_11(message)

def message_review_11(message):

    if message.text == "/start":
        start_message(message)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Наличными", callback_data="Наличными"))
    markup.add(types.InlineKeyboardButton("Лизинг", callback_data="Лизинг"))
    markup.add(types.InlineKeyboardButton("Перечисление", callback_data="Перечисление"))
    markup.add(types.InlineKeyboardButton("Кредит", callback_data="Кредит"))
    markup.add(types.InlineKeyboardButton("Рассрочка", callback_data="Рассрочка"))

    bot.send_message(message.chat.id, text = "Выберете вид оплаты:", reply_markup=markup)

def message_review_111(message):

    if message.text == "/start":
        start_message(message)

    msg_111_ = bot.send_message(message.chat.id, text = "Доп. Опции:")
    bot.register_next_step_handler(msg_111_, message_review_111_)

def message_review_111_(message):

    if message.text == "/start":
        start_message(message)

    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Доп. Опции:':mesage_to_save})

    bot.send_message(message.chat.id, text = f"""🔥{user_avto_list[message.chat.id]["Модель и марка машины:"]}-{user_avto_list[message.chat.id]["Цена:"]}🔥\n\n▪️Модель и марка машины: {user_avto_list[message.chat.id]["Модель и марка машины:"]}\n▪️Цена: {user_avto_list[message.chat.id]["Цена:"]}\n▪️Тип кузова: {user_avto_list[message.chat.id]["Тип кузова:"]}\n▪️Год выпуска: {user_avto_list[message.chat.id]["Год выпуска:"]}\n▪️Пробег: {user_avto_list[message.chat.id]["Пробег:"]}\n▪️Тип коробки передач: {user_avto_list[message.chat.id]["Тип коробки передач:"]}\n▪️Цвет: {user_avto_list[message.chat.id]["Цвет:"]}\n▪️Объем двигателя: {user_avto_list[message.chat.id]["Объем двигателя:"]}\n▪️Вид топлива: {user_avto_list[message.chat.id]["Вид топлива:"]}\n▪️Состояние машины: {user_avto_list[message.chat.id]["Состояние машины:"]}\n▪️Количество владельцев: {user_avto_list[message.chat.id]["Количество владельцев:"]}\n▪️Город: {user_avto_list[message.chat.id]["Город:"]}\n▪️Вид оплаты: {user_avto_list[message.chat.id]["Вид оплаты:"]}\n▪️Телефон для связи: {user_avto_list[message.chat.id]["Телефон для связи:"]}\n\n\n▪️Доп. Опции: {user_avto_list[message.chat.id]["Доп. Опции:"]}""")

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Все верно✅", callback_data="Все верно✅"))
    markup.add(types.InlineKeyboardButton("Ошибка❌", callback_data="Дать рекламное обьявление🛍"))

    bot.send_message(message.chat.id, text = "Пожалуйста проверьте данные о машине🚘.", reply_markup=markup)

while True:
    try :
        bot.infinity_polling()
    except Exception as err:
        print(err)
