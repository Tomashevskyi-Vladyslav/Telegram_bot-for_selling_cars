import telebot
from telebot import types

token = '#'
bot_pay_token = "#"
bot_pay_token_2 = "#"
bot = telebot.TeleBot(token)

user_avto_list = {}
counter = 0
leng_switcher = 0
terif = ""

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_avto_list
    bot.send_message(message.chat.id, text = 'Avtomarket Uzbekistan xush kelibsiz!\n\nBu yerda siz hohlagan avtomobilingizni eng yaxshi narxlarda sotishingiz va xarid qilishingiz, shuningdek, bozordagi joriy narxlar bilan tanishishingiz mumkin.\n\n-----------------------------------------\n\nДобро пожаловать на Avtomarket Uzbekistan!\n\nТут вы можете продать и купить любую вами желаемую машину по самым выгодным ценам, а так же ознакомиться с актуальными ценами на рынке.')

    bot.send_message("#", text = f'Клиент запустил бот\n\nЮзернейм: @{message.from_user.username}')

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🇺🇿O'zbekcha", callback_data="🇺🇿O'zbekcha"))
    markup.add(types.InlineKeyboardButton("🇷🇺Русский", callback_data="🇷🇺Русский"))
    
    bot.send_message(message.chat.id, text = 'Kerakli tilni tanlang.\n\nВыберите желаемый язык.', reply_markup=markup)

#    markup = types.InlineKeyboardMarkup()
#    markup.add(types.InlineKeyboardButton("Дать рекламное обьявление🛍", callback_data="Дать рекламное обьявление🛍"))
#    markup.add(types.InlineKeyboardButton("Нужна помощь с другим вопросом❓", callback_data="Нужна помощь с другим вопросом ❓"))
#    user_avto_list.update({message.chat.id:{"leng":"RU"}})
#
#    print(user_avto_list)
#    bot.send_message(message.chat.id, text = 'Добро пожаловать на Avtomarket Uzbekistan!\n\nТут вы можете продать и купить любую вами желаемую машину по самым выгодным ценам, а так же ознакомиться с актуальными ценами на рынке.', reply_markup=markup)
#    bot.send_message("#", text = f'Клиент запустил бот\n\nЮзернейм: @{message.from_user.username}')

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    global leng_switcher, user_avto_list, terif

    if callback.data == "🇷🇺Русский":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Дать рекламное обьявление🛍", callback_data="Дать рекламное обьявление🛍"))
        markup.add(types.InlineKeyboardButton("Нужна помощь с другим вопросом❓", callback_data="Нужна помощь с другим вопросом❓"))
        user_avto_list.update({callback.message.chat.id:{"leng":"RU"}})
        print(user_avto_list)

    if callback.data == "Нужна помощь с другим вопросом ❓":
        event_help = bot.send_message(callback.message.chat.id, text = "Пожалуйста оставьте свое сообщение и в тчении 24 часов мы свяжемся с вами.\n\nЕсли в течении 24 часов вы не получите ответ, пожалуйста свяжитесь с администратором @avtomaruzb.")
        bot.register_next_step_handler(event_help, event_help_1)

    if callback.data == "Эконом":
        terif = "Эконом"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data="CLICK Uzbekistan Эконом"))
        markup.add(types.InlineKeyboardButton("PayMe", callback_data="Pey Me Эконом"))

        bot.send_message(callback.message.chat.id, text = "Выберете способ оплаты.", reply_markup=markup)

    if callback.data == "CLICK Uzbekistan Эконом":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Стандарт" с помощью сервеса CLICK Uzbekistan""", """Покупка тарифа "Стандарт" """, "invoice", bot_pay_token, "UZS", [types.LabeledPrice("""Покупка тарифа "Стандарт" """, 49000*100)])

    if callback.data == "Pey Me Эконом":
        bot.send_invoice(callback.message.chat.id, """Покупка тарифа "Стандарт" с помощью сервеса Pey Me""", """Покупка тарифа "Стандарт" """, "invoice", bot_pay_token_2, "UZS", [types.LabeledPrice("""Покупка тарифа "Стандарт" """, 49000*100)])

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

        bot.send_message(callback.message.chat.id, text = "Aytingchi, sizning savolingiz nima bilan bog'liq?", reply_markup=markup)

    if callback.data == "Boshqa savol bo'yicha yordam kerak❓":
        event_help = bot.send_message(callback.message.chat.id, text = "Iltimos, xabaringizni qoldiring va biz 24 soat ichida siz bilan bog'lanamiz.\n\nAgar 24 soat ichida javob kelmasa, @avtomaruzb administratoriga murojaat qiling.")
        bot.register_next_step_handler(event_help, event_help_2)

    if callback.data == "Все верно✅":
        bot.send_message(callback.message.chat.id, text = "Для того чтобы продолжить отправьте 6 фотографий автомобиля.")
        leng_switcher = 1

    if callback.data == "Hammasi to'g'ri✅":
        bot.send_message(callback.message.chat.id, text = "Davom etish uchun mashinaning 6 ta fotosuratini yuboring.")
        leng_switcher = 2

    if callback.data == "Дать рекламное обьявление🛍":
        bot.send_message(callback.message.chat.id, text = "Пожалуйста, заполните пошагово анкету об автомобиле для рекламы о продаже 🚘.")
            
        msg_1 = bot.send_message(callback.message.chat.id, text = "Модель и марка машины:")
        bot.register_next_step_handler(msg_1, message_review_1)

    if callback.data == "Reklama berish🛍":
        bot.send_message(callback.message.chat.id, text = "Sotish haqida e'lon qilish uchun mashina haqida bosqichma-bosqich anketani to'ldiring 🚘.")
            
        msg_01 = bot.send_message(callback.message.chat.id, text = "Avtomobil modeli va markasi:")
        bot.register_next_step_handler(msg_01, message_review_01)

def event_help_1(message):
    bot.send_message("#", text = f"{message.text} Имя пользователя: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------
    bot.send_message(message.chat.id, text = "Сообщение было отправлено с вами скоро свяжеться администратор.")

def event_help_2(message):
    bot.send_message("#", text = f"{message.text} Foydalanuvchi nomi: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------
    bot.send_message(message.chat.id, text = "Xabar yuborildi, administrator tez orada siz bilan bog'lanadi.")

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True, error_message="Toʻlov amalga oshmadi – qayta urinib koʻring yoki bot administratoriga murojaat qiling.\n\n--------------------------\n\nОплата не прошла - попробуйте пожалуйста е ще раз, или свяжитесь с администратором бота.")

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):

    bot.send_message("#", f"""Клиет купил тариф: {terif} Имя пользователя @{message.from_user.username}""")

    if user_avto_list[message.chat.id]['leng'] == "RU":

        bot.send_media_group("#", [telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_1:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_2:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_3:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_4:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_5:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_6:"], f"""🔥{user_avto_list[message.chat.id]["Модель и марка машины:"]}-{user_avto_list[message.chat.id]["Цена:"]}🔥\n\n▪️Модель и марка машины: {user_avto_list[message.chat.id]["Модель и марка машины:"]}\n▪️Цена: {user_avto_list[message.chat.id]["Цена:"]}\n▪️Тип кузова: {user_avto_list[message.chat.id]["Тип кузова:"]}\n▪️Год выпуска: {user_avto_list[message.chat.id]["Год выпуска:"]}\n▪️Пробег: {user_avto_list[message.chat.id]["Пробег:"]}\n▪️Тип коробки передач: {user_avto_list[message.chat.id]["Тип коробки передач:"]}\n▪️Цвет: {user_avto_list[message.chat.id]["Цвет:"]}\n▪️Объем двигателя: {user_avto_list[message.chat.id]["Объем двигателя:"]}\n▪️Вид топлива: {user_avto_list[message.chat.id]["Вид топлива:"]}\n▪️Состояние машины: {user_avto_list[message.chat.id]["Состояние машины:"]}\n▪️Количество владельцев: {user_avto_list[message.chat.id]["Количество владельцев:"]}\n▪️Телефон для связи: {user_avto_list[message.chat.id]["Телефон для связи:"]}\n▪️Город: {user_avto_list[message.chat.id]["Город:"]}\n▪️Вид оплаты: {user_avto_list[message.chat.id]["Вид оплаты:"]}""")])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Сообщить о продаже машины 🚘")
        btn2 = types.KeyboardButton("Дать рекламное обьявление 🛍")
        btn3 = types.KeyboardButton("Нужна помощь с другим вопросом ❓")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, """Спасибо за доверие! Ваше объявление о продаже автомобиля будет опубликовано в кратчайшие сроки.\n\nПожалуйста, сообщите нам после продажи автомобиля 🙏🏻\n\nЕсли ваш пост не будет опубликован в течении 24 часов, прошу связаться с Админом.""", reply_markup=markup)

    if user_avto_list[message.chat.id]["leng"] == "OZ":
        
        bot.send_media_group("#", [telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_1:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_2:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_3:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_4:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_5:"]), telebot.types.InputMediaPhoto(user_avto_list[message.chat.id]["Foto_6:"], f"""🔥{user_avto_list[message.chat.id]["Avtomobil modeli va markasi:"]}-{user_avto_list[message.chat.id]["Narxi:"]}🔥\n\n▪️Avtomobil modeli va markasi: {user_avto_list[message.chat.id]["Avtomobil modeli va markasi:"]}\n▪️Narxi: {user_avto_list[message.chat.id]["Narxi:"]}\n▪️Tana turi: {user_avto_list[message.chat.id]["Tana turi:"]}\n▪️Ishlab chiqarilgan yili: {user_avto_list[message.chat.id]["Ishlab chiqarilgan yili:"]}\n▪️Vites qutisi turi: {user_avto_list[message.chat.id]["Vites qutisi turi:"]}\n▪️Chiqarilgan yili: {user_avto_list[message.chat.id]["Chiqarilgan yili:"]}\n▪️Rang: {user_avto_list[message.chat.id]["Rang:"]}\n▪️Dvigatel hajmi: {user_avto_list[message.chat.id]["Dvigatel hajmi:"]}\n▪️Yoqilg'i turi: {user_avto_list[message.chat.id]["Yoqilg'i turi:"]}\n▪️Avtomobil holati: {user_avto_list[message.chat.id]["Avtomobil holati:"]}\n▪️Egalari soni: {user_avto_list[message.chat.id]["Egalari soni:"]}\n▪️Aloqa telefon raqami: {user_avto_list[message.chat.id]["Aloqa telefon raqami:"]}\n▪️Shahar: {user_avto_list[message.chat.id]["Shahar:"]}\n▪️To'lov turi: {user_avto_list[message.chat.id]["To'lov turi:"]}""")])
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton("Avtomobil sotilgani haqida xabar bering 🚘")
        btn2 = types.KeyboardButton("E'lon qo'ying 🛍")
        btn3 = types.KeyboardButton("Boshqa savol bo'yicha yordam kerak ❓")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, """Ishonchingiz uchun rahmat! Avtomobil sotuvi haqidagi e'loningiz tezroq e'lon qilinadi.\n\nMashina sotilgandan keyin bizga xabar bering 🙏🏻\n\nAgar postingiz 24 soat ichida e'lon qilinmasa, Administratorga murojaat qiling.""", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def button_message(message):
    if message.text == "Сообщить о продаже машины 🚘":
        event_help = bot.send_message(message.chat.id, text = "Пожалуйста оставьте отзыв о нашем канале 🙏🏻:")
        bot.register_next_step_handler(event_help, event_help_3)

    if message.text == "Avtomobil sotilgani haqida xabar bering 🚘":
        event_help = bot.send_message(message.chat.id, text = "Kanalimiz haqida sharh qoldiring 🙏🏻:")
        bot.register_next_step_handler(event_help, event_help_4)

    if message.text == "Дать рекламное обьявление 🛍":
        bot.send_message(message.chat.id, text = "Пожалуйста, заполните пошагово анкету об автомобиле для рекламы о продаже 🚘.")
            
        msg_1 = bot.send_message(message.chat.id, text = "Модель и марка машины:")
        bot.register_next_step_handler(msg_1, message_review_1)

    if message.text == "Нужна помощь с другим вопросом ❓":
        event_help = bot.send_message(message.chat.id, text = "Пожалуйста оставьте свое сообщение и в тчении 24 часов мы свяжемся с вами.\n\nЕсли в течении 24 часов вы не получите ответ, пожалуйста свяжитесь с администратором @avtomaruzb.")
        bot.register_next_step_handler(event_help, event_help_1)

    if message.text == "Boshqa savol bo'yicha yordam kerak ❓":
        event_help = bot.send_message(message.chat.id, text = "Iltimos, xabaringizni qoldiring va biz 24 soat ichida siz bilan bog'lanamiz.\n\nAgar 24 soat ichida javob kelmasa, @avtomaruzb administratoriga murojaat qiling.")
        bot.register_next_step_handler(event_help, event_help_2)

    if message.text == "E'lon qo'ying 🛍":
        bot.send_message(message.chat.id, text = "Sotish haqida e'lon qilish uchun mashina haqida bosqichma-bosqich anketani to'ldiring 🚘.")
            
        msg_01 = bot.send_message(message.chat.id, text = "Avtomobil modeli va markasi:")
        bot.register_next_step_handler(msg_01, message_review_01)
        
def event_help_3(message):
    bot.send_message("#", text = f"Отзыв: {message.text} имя пользователя: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text = "Благодарим вас за отзыв! Мы будем рады видеть вас снова и будем признательны, если вы порекомендуете наш канал другим 🙏🏻.", reply_markup=a)
    start_message(message)


def event_help_4(message):
    bot.send_message("#", text = f"Отзыв: {message.text} имя пользователя: @{message.from_user.username}")#------------------------------------------------------------------------------------------------------------------------------------
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, text = "Fikr-mulohazangiz uchun rahmat! Sizni yana ko'rganimizdan xursand bo'lamiz va kanalimizni boshqalarga tavsiya qilsangiz minnatdor bo'lamiz 🙏🏻.", reply_markup=a)
    start_message(message)

@bot.message_handler(content_types=['photo'])
def photo_message(message):
    global counter, leng_switcher
    if message.chat.id in user_avto_list and counter<=6:
        counter += 1
        user_avto_list[message.chat.id].update({f'Foto_{counter}:':message.photo[-1].file_id})
        
    if counter == 6:
        bot.send_message("#", text = f'Клиент ознакомился с планом\n\nЮзернейм: @{message.from_user.username}')
        print(user_avto_list)

    if counter == 6 and leng_switcher == 1:
        counter = 0
        leng_switcher = 0

        markup = types.InlineKeyboardMarkup()
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
        markup.add(types.InlineKeyboardButton("Iqtisodiyot🔵", callback_data="Iqtisodiyot"))
        markup.add(types.InlineKeyboardButton("Standart🟢", callback_data="Standart"))
        markup.add(types.InlineKeyboardButton("Premium🟣", callback_data="Premium"))
        markup.add(types.InlineKeyboardButton("Elite🟡", callback_data="Elite"))
        markup.add(types.InlineKeyboardButton("Eksklyuziv🟠", callback_data="Eksklyuziv"))
        markup.add(types.InlineKeyboardButton("Ekstremal🔴", callback_data="Ekstremal"))

        bot.send_message(message.chat.id, text = """Tarif rejasini tanlang: \n\n49.000 - "Iqtisodiyot" tarifi\n● Oʻzingiz tanlagan avtomashinani istalgan vaqtda 2 marta chop etish\n\n59.000 - “Standart” tarifi\n● Oʻzingizning maʼlumotingizni eʼlon qilish. avtomashina ixtiyoriy qulay vaqtda 4 marta siz tanlagan holda\n\n69.000 - "Premium" tarifi\n● O'zingiz tanlagan avtomashinani istalgan vaqtda 6 marta nashr qilish + 3 kunga topshiriq\n\n89.000 - "Elite” tarifi\n● Oʻzingiz tanlagan avtomobilingizni 8 marta istalgan qulay vaqtda chop etish + 10 kunga tayinlash\n\n129.000 - “Eksklyuziv” tarifi\n● Oʻzingiz xohlagan qulay vaqtda avtomobilingizni 12 marta nashr qilish vaqt + 30 kunga tayinlash (avtomatik nashr qilish vaqtini belgilash mumkin)\n\n199.000 - "Ekstremal" tarifi\n● Avtomobilingizni bir oy davomida har kuni chop etish + sotuvga qadar kafolatlash\n\n❗️ HAR QANDAY TARIF SOTISHDA - AVTOMOBILINGIZ SOTISH NOKTAGACHA O‘CHIRILMAYDI.""", reply_markup=markup)

def message_review_01(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Avtomobil modeli va markasi:':mesage_to_save})
    
    msg_02 = bot.send_message(message.chat.id, text = "Narxi:")
    bot.register_next_step_handler(msg_02, message_review_02)

def message_review_02(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Narxi:':mesage_to_save})

    msg_03 = bot.send_message(message.chat.id, text = "Tana turi:")
    bot.register_next_step_handler(msg_03, message_review_03)

def message_review_03(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Tana turi:':mesage_to_save})

    msg_013 = bot.send_message(message.chat.id, text = "Ishlab chiqarilgan yili:")
    bot.register_next_step_handler(msg_013, message_review_013)

def message_review_013(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Ishlab chiqarilgan yili:':mesage_to_save})

    msg_014 = bot.send_message(message.chat.id, text = "Vites qutisi turi:")
    bot.register_next_step_handler(msg_014, message_review_014)

def message_review_014(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Vites qutisi turi:':mesage_to_save})

    msg_04 = bot.send_message(message.chat.id, text = "Chiqarilgan yili:")
    bot.register_next_step_handler(msg_04, message_review_04)

def message_review_04(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Chiqarilgan yili:':mesage_to_save})

    msg_05 = bot.send_message(message.chat.id, text = "Rang:")
    bot.register_next_step_handler(msg_05, message_review_05)

def message_review_05(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Rang:':mesage_to_save})

    msg_06 = bot.send_message(message.chat.id, text = "Dvigatel hajmi:")
    bot.register_next_step_handler(msg_06, message_review_06)

def message_review_06(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Dvigatel hajmi:':mesage_to_save})

    msg_07 = bot.send_message(message.chat.id, text = "Yoqilg'i turi:")
    bot.register_next_step_handler(msg_07, message_review_07)

def message_review_07(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({"Yoqilg'i turi:":mesage_to_save})

    msg_08 = bot.send_message(message.chat.id, text = "Avtomobil holati:")
    bot.register_next_step_handler(msg_08, message_review_08)

def message_review_08(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Avtomobil holati:':mesage_to_save})

    msg_09 = bot.send_message(message.chat.id, text = "Egalari soni:")
    bot.register_next_step_handler(msg_09, message_review_09)

def message_review_09(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Egalari soni:':mesage_to_save})

    msg_010 = bot.send_message(message.chat.id, text = "Aloqa telefon raqami:")
    bot.register_next_step_handler(msg_010, message_review_010)

def message_review_010(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Aloqa telefon raqami:':mesage_to_save})

    msg_011 = bot.send_message(message.chat.id, text = "Shahar:")
    bot.register_next_step_handler(msg_011, message_review_011)

def message_review_011(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Shahar:':mesage_to_save})

    msg_0111 = bot.send_message(message.chat.id, text = "To'lov turi:")
    bot.register_next_step_handler(msg_0111, message_review_0111)

def message_review_0111(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({"To'lov turi:":mesage_to_save})

    msg_0111_ = bot.send_message(message.chat.id, text = "Qo'shimcha variantlar:")
    bot.register_next_step_handler(msg_0111_, message_review_0111_)

def message_review_0111_(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({"Qo'shimcha variantlar:":mesage_to_save})

    bot.send_message(message.chat.id, text = f"""🔥{user_avto_list[message.chat.id]["Avtomobil modeli va markasi:"]}-{user_avto_list[message.chat.id]["Narxi:"]}🔥\n\n▪️Avtomobil modeli va markasi: {user_avto_list[message.chat.id]["Avtomobil modeli va markasi:"]}\n▪️Narxi: {user_avto_list[message.chat.id]["Narxi:"]}\n▪️Tana turi: {user_avto_list[message.chat.id]["Tana turi:"]}\n▪️Ishlab chiqarilgan yili: {user_avto_list[message.chat.id]["Ishlab chiqarilgan yili:"]}\n▪️Vites qutisi turi: {user_avto_list[message.chat.id]["Vites qutisi turi:"]}\n▪️Chiqarilgan yili: {user_avto_list[message.chat.id]["Chiqarilgan yili:"]}\n▪️Rang: {user_avto_list[message.chat.id]["Rang:"]}\n▪️Dvigatel hajmi: {user_avto_list[message.chat.id]["Dvigatel hajmi:"]}\n▪️Yoqilg'i turi: {user_avto_list[message.chat.id]["Yoqilg'i turi:"]}\n▪️Avtomobil holati: {user_avto_list[message.chat.id]["Avtomobil holati:"]}\n▪️Egalari soni: {user_avto_list[message.chat.id]["Egalari soni:"]}\n▪️Shahar: {user_avto_list[message.chat.id]["Shahar:"]}\n▪️To'lov turi: {user_avto_list[message.chat.id]["To'lov turi:"]}\n▪️Aloqa telefon raqami: {user_avto_list[message.chat.id]["Aloqa telefon raqami:"]}\n\n\n▪️Qo'shimcha variantlar: {user_avto_list[message.chat.id]["Qo'shimcha variantlar:"]}""")
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Hammasi to'g'ri✅", callback_data="Hammasi to'g'ri✅"))
    markup.add(types.InlineKeyboardButton("Xato❌", callback_data="Reklama berish🛍"))

    bot.send_message(message.chat.id, text = "Iltimos, mashinangiz tafsilotlarini tekshiring.", reply_markup=markup)

def message_review_1(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Модель и марка машины:':mesage_to_save})
    
    msg_2 = bot.send_message(message.chat.id, text = "Цена:")
    bot.register_next_step_handler(msg_2, message_review_2)

def message_review_2(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Цена:':mesage_to_save})

    msg_3 = bot.send_message(message.chat.id, text = "Тип кузова:")
    bot.register_next_step_handler(msg_3, message_review_3)

def message_review_3(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Тип кузова:':mesage_to_save})

    msg_13 = bot.send_message(message.chat.id, text = "Пробег:")
    bot.register_next_step_handler(msg_13, message_review_13)

def message_review_13(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Пробег:':mesage_to_save})

    msg_14 = bot.send_message(message.chat.id, text = "Тип коробки передач:")
    bot.register_next_step_handler(msg_14, message_review_14)

def message_review_14(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Тип коробки передач:':mesage_to_save})

    msg_4 = bot.send_message(message.chat.id, text = "Год выпуска:")
    bot.register_next_step_handler(msg_4, message_review_4)

def message_review_4(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Год выпуска:':mesage_to_save})

    msg_5 = bot.send_message(message.chat.id, text = "Цвет:")
    bot.register_next_step_handler(msg_5, message_review_5)

def message_review_5(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Цвет:':mesage_to_save})

    msg_6 = bot.send_message(message.chat.id, text = "Объем двигателя:")
    bot.register_next_step_handler(msg_6, message_review_6)

def message_review_6(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Объем двигателя:':mesage_to_save})

    msg_7 = bot.send_message(message.chat.id, text = "Вид топлива:")
    bot.register_next_step_handler(msg_7, message_review_7)

def message_review_7(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Вид топлива:':mesage_to_save})

    msg_8 = bot.send_message(message.chat.id, text = "Состояние машины:")
    bot.register_next_step_handler(msg_8, message_review_8)

def message_review_8(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Состояние машины:':mesage_to_save})

    msg_9 = bot.send_message(message.chat.id, text = "Количество владельцев:")
    bot.register_next_step_handler(msg_9, message_review_9)

def message_review_9(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Количество владельцев:':mesage_to_save})

    msg_10 = bot.send_message(message.chat.id, text = "Телефон для связи:")
    bot.register_next_step_handler(msg_10, message_review_10)

def message_review_10(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Телефон для связи:':mesage_to_save})

    msg_11 = bot.send_message(message.chat.id, text = "Город:")
    bot.register_next_step_handler(msg_11, message_review_11)

def message_review_11(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Город:':mesage_to_save})

    msg_111 = bot.send_message(message.chat.id, text = "Выберете вид оплаты, доступны такие виды как (Наличка/Кредит/Лизинг/Рассрочка):")
    bot.register_next_step_handler(msg_111, message_review_111)

def message_review_111(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Вид оплаты:':mesage_to_save})

    msg_111_ = bot.send_message(message.chat.id, text = "Доп. Опции:")
    bot.register_next_step_handler(msg_111_, message_review_111_)

def message_review_111_(message):
    mesage_to_save = message.text
    user_avto_list[message.chat.id].update({'Доп. Опции:':mesage_to_save})

    
    bot.send_message(message.chat.id, text = f"""🔥{user_avto_list[message.chat.id]["Модель и марка машины:"]}-{user_avto_list[message.chat.id]["Цена:"]}🔥\n\n▪️Модель и марка машины: {user_avto_list[message.chat.id]["Модель и марка машины:"]}\n▪️Цена: {user_avto_list[message.chat.id]["Цена:"]}\n▪️Тип кузова: {user_avto_list[message.chat.id]["Тип кузова:"]}\n▪️Год выпуска: {user_avto_list[message.chat.id]["Год выпуска:"]}\n▪️Пробег: {user_avto_list[message.chat.id]["Пробег:"]}\n▪️Тип коробки передач: {user_avto_list[message.chat.id]["Тип коробки передач:"]}\n▪️Цвет: {user_avto_list[message.chat.id]["Цвет:"]}\n▪️Объем двигателя: {user_avto_list[message.chat.id]["Объем двигателя:"]}\n▪️Вид топлива: {user_avto_list[message.chat.id]["Вид топлива:"]}\n▪️Состояние машины: {user_avto_list[message.chat.id]["Состояние машины:"]}\n▪️Количество владельцев: {user_avto_list[message.chat.id]["Количество владельцев:"]}\n▪️Город: {user_avto_list[message.chat.id]["Город:"]}\n▪️Вид оплаты: {user_avto_list[message.chat.id]["Вид оплаты:"]}\n▪️Телефон для связи: {user_avto_list[message.chat.id]["Телефон для связи:"]}\n\n\n▪️Доп. Опции: {user_avto_list[message.chat.id]["Доп. Опции:"]}""")

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Все верно✅", callback_data="Все верно✅"))
    markup.add(types.InlineKeyboardButton("Ошибка❌", callback_data="Дать рекламное обьявление🛍"))

    bot.send_message(message.chat.id, text = "Пожалуйста проверьте данные о машине.", reply_markup=markup)

while True:
    try :
        bot.infinity_polling()
    except Exception as err:
        print(err)