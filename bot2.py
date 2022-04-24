import telebot
import config

from telebot import types


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.KeyboardButton("Туда где тепло🌴")
    i2 = types.KeyboardButton("Туда где холодно❄️")

    markup.add(i1, i2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nВаши предпочтения к путешествию".format(message.from_user,
                                                                                                 bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def travel(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Пляж🏝')
    item2 = types.KeyboardButton('Горы🏔')
    item3 = types.KeyboardButton('Экскурсии🏛')
    item4 = types.KeyboardButton('⬅Назад🌴')
    item5 = types.KeyboardButton('Экстрим🏄🏻‍♀')
    item9 = types.KeyboardButton('Зож🏃')

    markup1.add(item1, item2, item3, item4, item5, item9)

    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    z1 = types.KeyboardButton('Зож🏃‍♀')
    z4 = types.KeyboardButton('Экстрим🏂')
    z5 = types.KeyboardButton('рыбалка🎣')
    z8 = types.KeyboardButton('⬅Назад❄️')

    markup2.add(z1, z4, z5, z8)

    p1 = open("пляж кр кр.png", 'rb')
    p2 = open("краснодарский край.png", 'rb')
    p3 = open("крымский поо.jpg", 'rb')
    p4 = open("горы all.jpeg", 'rb')
    p5 = open("камчатка11.png", 'rb')
    p6 = open("дагнестан горы.png", 'rb')
    p7 = open("алтай горы.png", 'rb')
    p8 = open("зож.jpeg", 'rb')
    p9 = open("экскурсии all.png", 'rb')
    p10 = open("Калининград.png", 'rb')
    p11 = open("дегесьан экс.png", 'rb')
    p12 = open("скалолазание all.png", 'rb')
    p13 = open("кавказ скалолазание.jpg", 'rb')
    p14 = open("дайвинг all.png", 'rb')
    p15 = open("серфинг all.png", 'rb')

    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    e1 = types.KeyboardButton('⬅Назад❄')
    e8 = types.KeyboardButton('Горнолыжный⛷')

    markup3.add(e1, e8)

    markup10 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.KeyboardButton("Туда где тепло🌴")
    i2 = types.KeyboardButton("Туда где холодно❄️")

    markup10.add(i1, i2)

    markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    x1 = types.KeyboardButton('Скалолазание🧗🏼‍♂')
    x2 = types.KeyboardButton('Сёрфинг🏄‍♂')
    x4 = types.KeyboardButton('Дайвинг🤿')
    x7 = types.KeyboardButton('⬅Назад🏄🏻‍♀')

    markup4.add(x1, x2, x4, x7)

    markup66 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kz1 = types.KeyboardButton('⏪Назад🏝')
    kz2 = types.KeyboardButton('Крымский ПО🟩')
    kz3 = types.KeyboardButton('Краснодарский край🟥')

    markup66.add(kz1, kz2, kz3)

    markup6 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kz1 = types.KeyboardButton('Сочи🏝')
    kz2 = types.KeyboardButton('Адлер🏝')
    kz3 = types.KeyboardButton('Пересыпь🏝')
    kz4 = types.KeyboardButton('Приморско-Ахтарск🏝')
    kz10 = types.KeyboardButton('Лазаревское🏝')
    kz8 = types.KeyboardButton('⏮Назад🏝')
    kz7 = types.KeyboardButton('Кучугуры🏝')
    kz9 = types.KeyboardButton('Анапа🏝')
    kz5 = types.KeyboardButton('Геленджик🏝')

    markup6.add(kz1, kz2, kz3, kz4, kz5, kz7, kz8, kz9, kz10)

    markup7 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sc1 = types.KeyboardButton('Феодосия🏝')
    sc2 = types.KeyboardButton('Ялта🏝')
    sc3 = types.KeyboardButton('Судак🏝')
    sc4 = types.KeyboardButton('Евпатория🏝')
    sc5 = types.KeyboardButton('Севастополь🏝')
    sc7 = types.KeyboardButton('⏮Назад🏝')
    sc9 = types.KeyboardButton('Алупка🏝')
    sc10 = types.KeyboardButton('Коктебель🏝')
    sc6 = types.KeyboardButton('Керчь🏝')

    markup7.add(sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc9, sc10)

    markup8 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    nn1 = types.KeyboardButton('Дагестан🔵')
    nn2 = types.KeyboardButton('Краснодакий край🔴')
    nn3 = types.KeyboardButton('Крымский ПО🟢')
    nn4 = types.KeyboardButton('⏪Назад🏔')
    nn5 = types.KeyboardButton('Камчатка🟠')
    nn7 = types.KeyboardButton('Алтай🟣')

    markup8.add(nn1, nn2, nn3, nn4, nn7, nn5)

    markup24 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Дубки🏔')
    kg2 = types.KeyboardButton('Махачкала🏔')
    kg3 = types.KeyboardButton('Хунзах🏔')
    kg5 = types.KeyboardButton('⏮Назад🏔')
    kg8 = types.KeyboardButton('Ахты🏔')
    kg6 = types.KeyboardButton('Карадах🏔')

    markup24.add(kg1, kg2, kg3, kg5, kg6, kg8)

    markup25 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Анапа🏔')
    kg2 = types.KeyboardButton('Гелендик🏔')
    kg3 = types.KeyboardButton('Туапсе🏔')
    kg4 = types.KeyboardButton('Сочи🏔')
    kg5 = types.KeyboardButton('Адлер🏔')
    kg8 = types.KeyboardButton('⏮Назад🏔')
    kg6 = types.KeyboardButton('тамань🏔')

    markup25.add(kg1, kg2, kg3, kg4, kg5, kg6, kg8)

    markup100 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Алушта🏔')
    kg2 = types.KeyboardButton('Ялта🏔')
    kg3 = types.KeyboardButton('Севастополь🏔')
    kg4 = types.KeyboardButton('⏮Назад🏔')
    kg8 = types.KeyboardButton('Бахчисарай🏔')
    kg6 = types.KeyboardButton('Феодосия🏔')

    markup100.add(kg1, kg2, kg3, kg4, kg6, kg8)

    markup26 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Тюнгур🏔')
    kg2 = types.KeyboardButton('Чибит🏔')
    kg3 = types.KeyboardButton('Джазаторское🏔')
    kg4 = types.KeyboardButton('⏮Назад🏔')

    markup26.add(kg1, kg2, kg3, kg4)

    markup27 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('⏮Назад🏔')
    kg2 = types.KeyboardButton('Вилючинск🏔')
    kg6 = types.KeyboardButton('Петропавловск-Камчатский🏔')

    markup27.add(kg1, kg2, kg6,)

    markup9 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Дагестан🟧')
    kg2 = types.KeyboardButton('Крым🟥')
    kg3 = types.KeyboardButton('Краснодарский край🟩')
    kg4 = types.KeyboardButton('⏪Назад🏛')
    kg7 = types.KeyboardButton('Калининградская область🟦')

    markup9.add(kg1, kg2, kg3, kg4, kg7)

    markup30 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Дербент🏛')
    kg2 = types.KeyboardButton('Ахты🏛')
    kg3 = types.KeyboardButton('Махачкала🏛')
    kg4 = types.KeyboardButton('⏮Назад🏛')
    kg5 = types.KeyboardButton('Кизляр🏛')
    kg6 = types.KeyboardButton('Буйнакск🏛')

    markup30.add(kg1, kg2, kg3, kg4, kg5, kg6)

    markup28 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Бахчисарай🏛')
    kg2 = types.KeyboardButton('Судак🏛')
    kg3 = types.KeyboardButton('Феодосия🏛')
    kg4 = types.KeyboardButton('Керчь🏛')
    kg5 = types.KeyboardButton('Севастополь🏛')
    kg8 = types.KeyboardButton('⏮Назад🏛')
    kg6 = types.KeyboardButton('Ялта🏛')

    markup28.add(kg1, kg2, kg3, kg4, kg5, kg6, kg8)

    markup11 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vs1 = types.KeyboardButton('Тамань🏛')
    vs2 = types.KeyboardButton('Сочи🏛')
    vs3 = types.KeyboardButton('Адлер🏛')
    vs4 = types.KeyboardButton('Лазоревское🏛')
    vs5 = types.KeyboardButton('Геленджик🏛')
    vs6 = types.KeyboardButton('Туапсе🏛')
    vs7 = types.KeyboardButton('⏮Назад🏛')

    markup11.add(vs1, vs2, vs3, vs4, vs5, vs6, vs7)

    markup29 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Калининград🏛')
    kg2 = types.KeyboardButton('Советск🏛')
    kg3 = types.KeyboardButton('Зеленоградск🏛')
    kg4 = types.KeyboardButton('Светлогорск🏛')
    kg5 = types.KeyboardButton('Балтийск🏛')
    kg8 = types.KeyboardButton('⏮Назад🏛')
    kg6 = types.KeyboardButton('Гусев🏛')

    markup29.add(kg1, kg2, kg3, kg4, kg5, kg6, kg8)

    markup12 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Белокуриха🏃')
    kg2 = types.KeyboardButton('Кисловодск🏃')
    kg3 = types.KeyboardButton('Московская область🏃')
    kg4 = types.KeyboardButton('Ессентуки🏃')
    kg5 = types.KeyboardButton('Ялта🏃')
    kg6 = types.KeyboardButton('Саки🏃')
    kg7 = types.KeyboardButton('⏪Назад🏃')

    markup12.add(kg1, kg2, kg3, kg4, kg5, kg6, kg7)

    markup15 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vs1 = types.KeyboardButton('⏪Назад🧗🏼‍♂')
    vs3 = types.KeyboardButton('Кавказ🟧')
    vs7 = types.KeyboardButton('Крым🟩')

    markup15.add(vs1, vs3, vs7)

    markup31 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Ялта🧗🏼‍♂')
    kg2 = types.KeyboardButton('Алушта🧗🏼‍♂')
    kg3 = types.KeyboardButton('Симферополь🧗🏼‍♂')
    kg4 = types.KeyboardButton('⏮Назад🧗🏼‍♂')
    kg5 = types.KeyboardButton('Судак🧗🏼‍♂')
    kg6 = types.KeyboardButton('Бахчисарай🧗🏼‍♂')

    markup31.add(kg1, kg2, kg3, kg4, kg5, kg6)

    markup32 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Архыз🧗🏼‍♂')
    kg2 = types.KeyboardButton('Сочи🧗🏼‍♂')
    kg3 = types.KeyboardButton('Кисловодск🧗🏼‍♂')
    kg4 = types.KeyboardButton('Владикавказ🧗🏼‍♂')
    kg5 = types.KeyboardButton('Дубки🧗🏼‍♂')
    kg8 = types.KeyboardButton('⏮Назад🧗🏼‍♂')
    kg6 = types.KeyboardButton('Эльбрус🧗🏼‍♂')

    markup32.add(kg1, kg2, kg3, kg4, kg5, kg6, kg8)

    markup14 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sc1 = types.KeyboardButton('⏪Назад🤿')
    sc2 = types.KeyboardButton('Крым🟦')
    sc7 = types.KeyboardButton('Краснодарский край🟧')

    markup14.add(sc1, sc2, sc7)

    markup33 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kz1 = types.KeyboardButton('Сочи🤿')
    kz2 = types.KeyboardButton('Адлер🤿')
    kz4 = types.KeyboardButton('Геленджик🤿')
    kz10 = types.KeyboardButton('⏮Назад🤿')
    kz8 = types.KeyboardButton('Анапа🤿')
    kz7 = types.KeyboardButton('Кучугуры🤿')
    kz9 = types.KeyboardButton('Лазаревское🤿')
    kz11 = types.KeyboardButton('Туапсе🤿')

    markup33.add(kz1, kz2, kz4, kz7, kz8, kz9, kz10, kz11)

    markup35 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sc1 = types.KeyboardButton('Феодосия🤿')
    sc2 = types.KeyboardButton('Ялта🤿')
    sc3 = types.KeyboardButton('Судак🤿')
    sc4 = types.KeyboardButton('Евпатория🤿')
    sc5 = types.KeyboardButton('Севастополь🤿')
    sc7 = types.KeyboardButton('⏮Назад🤿')
    sc9 = types.KeyboardButton('Алупка🤿')
    sc10 = types.KeyboardButton('Коктебель🤿')
    sc6 = types.KeyboardButton('Керчь🤿')

    markup35.add(sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc9, sc10)

    markup99 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sc1 = types.KeyboardButton('⏪Назад🏄‍♂')
    sc2 = types.KeyboardButton('Крым🟪')
    sc4 = types.KeyboardButton('Краснодарский край🟫')

    markup99.add(sc1, sc2, sc4)

    markup34 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sc1 = types.KeyboardButton('Феодосия🏄‍♂')
    sc2 = types.KeyboardButton('Ялта🏄‍♂')
    sc3 = types.KeyboardButton('Судак🏄‍♂')
    sc4 = types.KeyboardButton('Евпатория🏄‍♂')
    sc5 = types.KeyboardButton('Севастополь🏄‍♂')
    sc7 = types.KeyboardButton('⏮Назад🏄‍♂')
    sc9 = types.KeyboardButton('Алупка🏄‍♂')
    sc10 = types.KeyboardButton('Коктебель🏄‍♂')
    sc6 = types.KeyboardButton('Керчь🏄‍♂')

    markup34.add(sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc9, sc10)

    markup36 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kz1 = types.KeyboardButton('Сочи🏄‍♂')
    kz2 = types.KeyboardButton('Адлер🏄‍♂')
    kz4 = types.KeyboardButton('Туапсе🏄‍♂')
    kz10 = types.KeyboardButton('Лазаревское🏄‍♂')
    kz8 = types.KeyboardButton('⏮Назад🏄‍♂')
    kz7 = types.KeyboardButton('Кучугуры🏄‍♂')
    kz9 = types.KeyboardButton('Анапа🏄‍♂')
    kz5 = types.KeyboardButton('Геленджик🏄‍♂')

    markup36.add(kz1, kz2, kz3, kz4, kz5, kz7, kz8, kz9, kz10)

    markup40 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Краснодарский край⬜')
    item2 = types.KeyboardButton('Крым🟨')
    item3 = types.KeyboardButton('Другие⛷')
    item4 = types.KeyboardButton('⏪Назад⛷')

    markup40.add(item1, item2, item3, item4)

    markup42 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Алушта⛷')
    item2 = types.KeyboardButton('Ай Петри⛷')
    item5 = types.KeyboardButton('⏮Назад⛷')

    markup42.add(item1, item2, item5)

    markup41 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton('Красная Поляна⛷')
    item3 = types.KeyboardButton('Лаго-Наки⛷')
    item4 = types.KeyboardButton('Псебай⛷')
    item5 = types.KeyboardButton('⏮Назад⛷')

    markup41.add(item2, item3, item4, item5)

    markup43 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Бобровый лог⛷')
    item2 = types.KeyboardButton('Сорочаны⛷')
    item3 = types.KeyboardButton('Игора⛷')
    item4 = types.KeyboardButton('Большой Вудъявр⛷')
    item5 = types.KeyboardButton('Домбай⛷')
    item6 = types.KeyboardButton('Гора Соболиная⛷')
    item7 = types.KeyboardButton('Завьялиха⛷')
    item8 = types.KeyboardButton('⏮Назад⛷')

    markup43.add(item1, item2, item3, item4, item5, item6, item7, item8)

    if message.chat.type == 'private':
        if message.text == 'Туда где тепло🌴':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup1)
        elif message.text == 'Туда где холодно❄️':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup3)
        elif message.text == '⬅Назад🏂':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup3)
        elif message.text == '⬅Назад🌴':
            bot.send_message(message.chat.id, "Ваши предпочтения к путешествию", reply_markup=markup10)
        elif message.text == '⬅Назад❄':
            bot.send_message(message.chat.id, "Ваши предпочтения к путешествию", reply_markup=markup10)
        elif message.text == 'Экстрим🏄🏻‍♀':
            bot.send_message(message.chat.id, "Какой вид экстрима вы предпочитаете?", reply_markup=markup4)
        elif message.text == '⬅Назад🏄🏻‍♀':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup1)
        elif message.text == '⏪Назад🏝':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup1)
        elif message.text == 'Пляж🏝':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup66)
            bot.send_photo(message.chat.id, p1)
        elif message.text == 'Краснодарский край🟥':
            bot.send_message(message.chat.id, "Вот список городов этого региона", reply_markup=markup6)
            bot.send_photo(message.chat.id, p2)
        elif message.text == 'Крымский ПО🟢':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup100)
            bot.send_photo(message.chat.id, p3)
        elif message.text == 'Горы🏔':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup8)
            bot.send_photo(message.chat.id, p4)
        elif message.text == '⏮Назад🏔':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup8)
            bot.send_photo(message.chat.id, p4)
        elif message.text == 'Дагестан🔵':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup24)
            bot.send_photo(message.chat.id, p6)
        elif message.text == 'Краснодакий край🔴':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup25)
            bot.send_photo(message.chat.id, p2)
        elif message.text == '⏪Назад🏔':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup1)
        elif message.text == 'Алтай🟣':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup26)
            bot.send_photo(message.chat.id, p7)
        elif message.text == 'Камчатка🟠':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup27)
            bot.send_photo(message.chat.id, p5)
        elif message.text == 'Далее🏔➡':
            bot.send_message(message.chat.id, "Вот еще список городов", reply_markup=markup8)
        elif message.text == '⬅Назад🏔':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup7)
        elif message.text == 'Экскурсии🏛':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup9)
            bot.send_photo(message.chat.id, p9)
        elif message.text == 'Крым🟥':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup28)
            bot.send_photo(message.chat.id, p3)
        elif message.text == 'Краснодарский край🟩':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup11)
            bot.send_photo(message.chat.id, p2)
        elif message.text == 'Дагестан🟧':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup30)
            bot.send_photo(message.chat.id, p11)
        elif message.text == 'Калининградская область🟦':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup29)
            bot.send_photo(message.chat.id, p10)
        elif message.text == '⏮Назад🏛':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup9)
            bot.send_photo(message.chat.id, p9)
        elif message.text == '⏪Назад🏛':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup1)
        elif message.text == '🏛Далее➡':
            bot.send_message(message.chat.id, "Вот еще список городов", reply_markup=markup11)
        elif message.text == '⬅Назад🏛':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup9)
        elif message.text == 'Зож🏃':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup12)
            bot.send_photo(message.chat.id, p8)
        elif message.text == '⏪Назад🏃':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup1)
        elif message.text == '⬅Назад🏃':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup12)
        elif message.text == 'Скалолазание🧗🏼‍♂':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup15)
            bot.send_photo(message.chat.id, p12)
        elif message.text == 'Крым🟩':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup31)
            bot.send_photo(message.chat.id, p3)
        elif message.text == '⏮Назад🧗🏼‍♂':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup15)
            bot.send_photo(message.chat.id, p12)
        elif message.text == 'Кавказ🟧':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup32)
            bot.send_photo(message.chat.id, p13)
        elif message.text == '⏪Назад🧗🏼‍♂':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup4)
        elif message.text == 'Дайвинг🤿':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup14)
            bot.send_photo(message.chat.id, p14)
        elif message.text == 'Краснодарский край🟧':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup33)
            bot.send_photo(message.chat.id, p2)
        elif message.text == 'Крым🟦':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup35)
            bot.send_photo(message.chat.id, p3)
        elif message.text == '⏮Назад🤿':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup14)
            bot.send_photo(message.chat.id, p14)
        elif message.text == '⏪Назад🤿':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup4)
        elif message.text == 'Сёрфинг🏄‍♂':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup99)
            bot.send_photo(message.chat.id, p15)
        elif message.text == 'Крым🟪':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup34)
            bot.send_photo(message.chat.id, p3)
        elif message.text == 'Краснодарский край🟫':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup36)
            bot.send_photo(message.chat.id, p2)
        elif message.text == '⏮Назад🏄‍♂':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup4)
            bot.send_photo(message.chat.id, p15)
        elif message.text == '⏪Назад🏄‍♂':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup4)
            #################################################################################
        elif message.text == 'Горнолыжный⛷':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup40)
        elif message.text == 'Краснодарский край⬜':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup41)
        elif message.text == 'Крым🟨':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup42)
        elif message.text == 'Другие⛷':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup43)
        elif message.text == '⏪Назад⛷':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup3)
        elif message.text == '⏮Назад⛷':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup40)
            ##################################################################################
        elif message.text == 'Крымский ПО🟩':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup7)
            bot.send_photo(message.chat.id, p3)
        elif message.text == '⏮Назад🏝':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup66)
            bot.send_photo(message.chat.id, p1)
        elif message.text == 'Крым🟥':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup28)
        elif message.text == '⏮Назад⛷':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup40)
        elif message.text == 'Пляж🏝':
            bot.send_photo(message.chat.id, p1)
        elif message.text == 'Геленджик🏝':
            bot.send_message(message.chat.id, "В Геленджике представлены песчаные и галечные пляжи \n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigp",)
        elif message.text == 'Сочи🏝':
            bot.send_message(message.chat.id, "В Сочи представлены галечные и песчаные пляжи\n"
                                              "Лучшие пляжи Сочи по отзывам отдыхающих — это песчаные\n"
                                              "Вот ссылка на сайтдля бронирования отелей\n"
                                              " http://surl.li/bvifu", )
        elif message.text == 'Адлер🏝':
            bot.send_message(message.chat.id, "Пляжи Адлера покрыты галькой с редкими вкраплениями песчаных участков\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              " http://surl.li/bvify", )
        elif message.text == 'Туапсе🏝':
            bot.send_message(message.chat.id, "Преобладают галечные и песчано-галечные пляжи с довольно ровной и "
                                              "пологой береговой линией\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigr")
        elif message.text == 'Ейск🏝':
            bot.send_message(message.chat.id, "В Ейске представлены Песчано-ракушечные и Песчано-галечные пляжи\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigs")
        elif message.text == 'Пересыпь🏝':
            bot.send_message(message.chat.id, "В Пересыпи представлены ракушечные пляжи\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              " http://surl.li/bviga")
        elif message.text == 'Приморско-Ахтарск🏝':
            bot.send_message(message.chat.id, " Преобладают песчаный и песчано-галечный пляж\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigb")
        elif message.text == 'Лазаревское🏝':
            bot.send_message(message.chat.id, "Преобладают галечные и смешанные песчано-галечные пляжи\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigf")
        elif message.text == 'Кучугуры🏝':
            bot.send_message(message.chat.id, "Полоса прекрасных песчано-ракушечных пляжей тянется от "
                                              "курортного посёлка"
                                              "Кучугуры в сторону мыса Пёклы\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigl")
        elif message.text == 'Анапа🏝':
            bot.send_message(message.chat.id, "Естественное покрытие диких пляжей — песчаное, к югу — галечное\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigo")
        elif message.text == 'Феодосия🏝':
            bot.send_message(message.chat.id, "Пляжи Феодосии преимущественно песчаные, но встречаются также "
                                              "варианты с мелкой и крупной галькой\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihe")
        elif message.text == 'Ялта🏝':
            bot.send_message(message.chat.id, "Пляжи Ялты покрыты крупной и мелкой галькой\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihf")
        elif message.text == 'Судак🏝':
            bot.send_message(message.chat.id, "ляжи Судака покрывает смесь крупного кварцевого и "
                                              "сланцевого песка необычного серебристо-серого оттенка\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihh")
        elif message.text == 'Евпатория🏝':
            bot.send_message(message.chat.id, " Пляжи преимущественно песчаные, местами с мелкими ракушками\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihj")
        elif message.text == 'Севастополь🏝':
            bot.send_message(message.chat.id, "В Севастополе представены песчаные, галичные, скалистые и "
                                              "городске бетонные пляжи\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihm")
        elif message.text == 'Алупка🏝':
            bot.send_message(message.chat.id, "Пляжи этого курорта — каменно-галечные\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EU2")
        elif message.text == 'Коктебель🏝':
            bot.send_message(message.chat.id, "Пляжи в Коктебеле преобладают галечные, с песчаным дном\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EWC")
        elif message.text == 'Керчь🏝':
            bot.send_message(message.chat.id, "Керченский полуостров предлагает гостям Крыма отличные"
                                              " песчаные пляжи на берегах Чёрного и Азовского морей\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EYP")
        elif message.text == 'Дубки🏔':
            bot.send_message(message.chat.id, "Сулакский каньон — одна из самых ярких и захватывающих природных "
                                              "достопримечательностей Дагестана. Он протянулся на десятки километров"
                                              " к северу от Гимринского хребта, где берет свое начало река Сулак\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Ffp ")
        elif message.text == 'Махачкала🏔':
            bot.send_message(message.chat.id, "Ахульго – это горная вершина, окуруженная кольцом других гор\n"
                                              "Джалган - это горная вершина системы Сабаново-Джалганского хребта "
                                              "и имеет высоту 708,2 метра\n"
                                              "Ачигсырт – это горная вершина, относящаяся к передовому"
                                              " Сабаново-Джалганскому хребту Большого Кавказа. Ее высота "
                                              "составляет 585 метров над уровнем моря\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0FhW")
        elif message.text == 'Хунзах🏔':
            bot.send_message(message.chat.id, "Акаро — горная вершина находящаяся на территории Хунзахского района"
                                              " к юго-западу от Хунзаха. Высота над уровнем моря 2194 м\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0FlK")
        elif message.text == 'Ахты🏔':
            bot.send_message(message.chat.id, "Ухиндаг — вершина в южной части Дагестана. "
                                              "Относится к Гельмец-Ахтынскому"
                                              "хребту системы Бокового хребта Кавказских гор. Ее высота 1870 метров"
                                              " над уровнем моря\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://www.hotel24.ru/akhty/11807")
        elif message.text == 'Карадах🏔':
            bot.send_message(message.chat.id, "Карадахская теснина — уникальный природный памятник. Любой турист,"
                                              " попадающий сюда, сразу понимает, отчего у теснины такие"
                                              " странные названия — ущелье шириной всего лишь"
                                              " от 2 до 5 метров окружено большими гладкими стенами средней"
                                              " высотой в 150 метров\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://goo-gl.me/gfdzL")
        elif message.text == 'Анапа🏔':
            bot.send_message(message.chat.id, "Самой высокой является Лысая гора в Анапе – своеобразные "
                                              "ворота в Большой Кавказ. Ее высота 319 метров над уровнем моря\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigo")
        elif message.text == 'Гелендик🏔':
            bot.send_message(message.chat.id, "Самая высокая гора тут Тхаб - 905 метров над уровнем моря"
                                              "Есть возвышенности и пониже. Популярнейший среди них - Маркотхский"
                                              " хребет (чуть более 600 м).\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigp")
        elif message.text == 'Туапсе🏔':
            bot.send_message(message.chat.id, "Главная вершина Туапсинского района - гора Шесси - 1839 метров над"
                                              "уровнем моря. Есть и поменьше, к примеру, со странным"
                                              "названием Индюк или Семашко - чуть более тысячи метров\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigr")
        elif message.text == 'Сочи🏔':
            bot.send_message(message.chat.id, "Лысая гора 140м популярная из-за купли-продажи недвижимости,"
                                              "может также похвастаться дендрарием на своем хребте и любопытной"
                                              "историей названия\n"
                                              "еще больше инвормации о горах по ссылке\n"
                                              "https://kukarta.ru/goryi-sochi/"
                                              "Вот ссылка на сайтдля бронирования отелей\n"
                                              "http://surl.li/bvifu")
        elif message.text == 'Адлер🏔':
            bot.send_message(message.chat.id, "Гора Ахун стоит в междуречье Мацесты и Хосты, это заметная и "
                                              "яркая достопримечательность сочинского побережья"
                                              "Высота над уровнем моря — 663 м\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvify")
        elif message.text == 'тамань🏔':
            bot.send_message(message.chat.id, "Карабетова гора представляет собой большой грязевой вулкан, который "
                                              "находится в Темрюкском районе. Гора имеет вид овального"
                                              " кратерного плато,"
                                              " протяженностью в 1400 метров и 860 метров в диаметре и высотой около"
                                              " 60 метров\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://inlnk.ru/w4gM69")
        elif message.text == 'Алушта🏔':
            bot.send_message(message.chat.id, "Медведь-гора Аю-Даг - историко-археологический памятник Крыма."
                                            "Гора расположена на Южном берегу Крыма, на границе Большой Алушты и"
                                              "Большой Ялты к востоку от Гурзуфа. Высота Медведь-горы - 577 метров"
                                              " над уровнем моря\n"
                                              "больше информации о горах поссылке\n"
                                              "http://surl.li/bliij"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://inlnk.ru/G6YA9e")
        elif message.text == 'Ялта🏔':
            bot.send_message(message.chat.id, "Ай-Петри - знаменитый потухший вулкан, расположенный "
                                              "в горах над городом Алупка, в Ялтинском регионе Крыма."
                                              " Различают несколько вершин горы Ай-Петри: Главную – 1234 метра,"
                                              " Западную и Восточную – 1100 метров\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihf")
        elif message.text == 'Севастополь🏔':
            bot.send_message(message.chat.id, "Сапу́н-Гора́, также Сапу́н-гора́ — хребтообразная возвышенность, "
                                              "находящаяся к юго-востоку от Севастополя. Высота — 240 метров\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihm")
        elif message.text == 'Феодосия🏔':
            bot.send_message(message.chat.id, "Горный хребет Эчки-Даг – место удивительное. Здесь сошлись море, горы,"
                                              " степь и лес, создав прекрасную возможность "
                                              "увидеть многообразие природы Крыма, поднявшись на его вершину"
                                              "Ее высота 688 метров над уровнем моря"
                                              "еще больше информации о горах по ссылке"
                                              "http://surl.li/bliir\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihe")
        elif message.text == 'Бахчисарай🏔':
            bot.send_message(message.chat.id, "Пещерный город Тепе-Кермен — это старинная крепость, расположенная на"
                                              " одноименной горе, возвышающейся над рекой Кача\n"
                                              "еще больше информации по ссылке"
                                              "https://www.tourister.ru/world/europe/russia/city/bakhchysaray/mount"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://inlnk.ru/emOwxm")
        elif message.text == 'Чибит🏔':
            bot.send_message(message.chat.id, "В 2,5 километрах от села, вниз по течению Чуи, находится деревянный мост,"
                                              " с севера от которого на правобережье находится небольшая "
                                              "гора Еже-тру(1307 м над ур. моря)"
                                              "На юго-востоке от села на правом борту Чуи находится "
                                              "гора Белькенек (2264 м)\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://inlnk.ru/O1eJAw")
        elif message.text == 'Джазаторское🏔':
            bot.send_message(message.chat.id, "Ледник Большой Актру это 8 km (11 000 шагов) маршрут расположенный"
                                              " рядом Джазаторское. Этот маршрут имеет перепад высот около 733 m"
                                              " и имеет рейтинг cложно")
        elif message.text == 'Тюнгур🏔':
            bot.send_message(message.chat.id, "Гора Белуха находится в Усть-Коксинском районе Горного Алтая."
                                              " Она является высшей точкой Катунского хребта и высшей точкой Сибири\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Z0G")
        elif message.text == 'Вилючинск🏔':
            bot.send_message(message.chat.id, "Вилю́чинская Со́пка или Вилю́чинский — вулкан на Камчатке,"
                                              " расположен к юго-западу от г. Петропавловска-Камчатского"
                                              "Представлен правильным конусом высотой 2173 м над уровнем моря\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Z4m")
        elif message.text == 'Петропавловск-Камчатский🏔':
            bot.send_message(message.chat.id, "Кумроч — горный хребет на востоке Камчатском крае России,"
                                              " северо-восточная часть системы Восточного хребта."
                                              "Протяжённость хребта составляет 220 км."
                                              "Средняя высота — от 800 до 1400 м. Высшая точка — вулкан Шиш (2346 м)"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Z76")
        elif message.text == 'Белокуриха🏃':
            bot.send_message(message.chat.id, "Вот ссылки на одни из лучших санаториев Белокурихи\n"
                                              "1: https://edem-altay.ru/\n"
                                              "2: https://www.belokurikha-san.ru/\n"
                                              "3: https://altai-west.ru/")
        elif message.text == 'Кисловодск🏃':
            bot.send_message(message.chat.id, "Вот ссылки на одни из лучших санаториев Белокурихи\n"
                                              "1: https://www.sanzarya.ru/ \n"
                                              "2: https://krugozor.su/ \n"
                                              "3: https://www.villa-arnest.ru/")
        elif message.text == 'Московская область🏃':
            bot.send_message(message.chat.id, "Вот ссылки на одни из лучших санаториев Московской области\n"
                                              "1: http://surl.li/bllcb \n"
                                              "2: http://surl.li/bllct \n"
                                              "3: http://surl.li/bllcw")
        elif message.text == 'Ессентуки🏃':
            bot.send_message(message.chat.id, "Вот ссылки на одни из лучших санаториев Есентуков\n"
                                              "1: http://surl.li/blldb\n"
                                              "2: https://sangem.ru/\n"
                                              "3: https://sanand.ru/")
        elif message.text == 'Ялта🏃':
            bot.send_message(message.chat.id, "Вот ссылки на одни из лучших санаториев Ялты\n"
                                              "1: http://surl.li/blldv\n"
                                              "2: http://surl.li/blldn\n"
                                              "3: https://zaporozh.ru/")
        elif message.text == 'Саки🏃':
            bot.send_message(message.chat.id, "Вот ссылки на одни из лучших санаториев Саки\n"
                                              "1: http://surl.li/blleg\n"
                                              "2: https://slavutich.su/\n"
                                              "3: https://sakropol.center/")
        elif message.text == 'Калининград🏛':
            bot.send_message(message.chat.id, "Вот некоторые из достопремичательностей этого города"
                                              "1: Бранденбургские ворота в Калининграде\n"
                                              "2: Кафедральный собор\n"
                                              "3: Королевские ворота\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "http://surl.li/blqod"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Z9F")
        elif message.text == 'Советск🏛':
            bot.send_message(message.chat.id, "Вот некоторые из достопремичательностей этого города"
                                              "1: Мост королевы Луизы\n"
                                              "2: Pobedy Street\n"
                                              "3: Музей истории города Советска\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "http://surl.li/blqoc"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZcI")
        elif message.text == 'Зеленоградск🏛':
            bot.send_message(message.chat.id, "Вот некоторые из достопремичательностей этого города"
                                              "1: Бювет «Королева Луиза»\n"
                                              "2: Сквер королевы Луизы\n"
                                              "3: Водонапорная башня\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "http://surl.li/blqob"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Zez")
        elif message.text == 'Светлогорск🏛':
            bot.send_message(message.chat.id, "Вот некоторые из достопремичательностей этого города"
                                              "1: Макет средневекового Кёнигсберга\n"
                                              "2: Солнечные часы Зодиак\n"
                                              "3: Храм преподобного Серафима Саровского\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "http://surl.li/blqnz"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZfV")
        elif message.text == 'Балтийск🏛':
            bot.send_message(message.chat.id, "1: Крепость Пиллау\n"
                                              "2: Музей Балтийского флота\n"
                                              "3: Пехотные казармы\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "http://surl.li/blqnm"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Zh3")
        elif message.text == 'Гусев🏛':
            bot.send_message(message.chat.id, "1: Гусевский историко-краеведческий музей им. А.М. Иванова\n"
                                              "2: Храм-памятник в честь Всех Святых\n"
                                              "3: Памятник Памяти забытой войны, изменившей ход истории\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "http://surl.li/blqns"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZiP")
        elif message.text == 'Бахчисарай🏛':
            bot.send_message(message.chat.id, "1: Бахчисарайский Свято-Успенский мужской монастырь\n"
                                              "2: Историко-культурный и археологический музей-заповедник\n"
                                              "3: Малая ханская мечеть\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFhI"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/bahchisarai/hotels/")
        elif message.text == 'Судак🏛':
            bot.send_message(message.chat.id, "1: Судакская крепость\n"
                                              "2: Солнечная Долина Дегустационный зал\n"
                                              "3: Холм Славы\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFhu"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/sudak/hotels/")
        elif message.text == 'Феодосия🏛':
            bot.send_message(message.chat.id, "1: Дача Стамболи\n"
                                              "2: Дача Виктория - ИПЦ Феостория\n"
                                              "3: Генуэзская крепость Каффа\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFhO"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/feodosiya/hotels/")
        elif message.text == 'Керчь🏛':
            bot.send_message(message.chat.id, "1: Митридатская лестница\n"
                                              "2: Крепость Ени-Кале\n"
                                              "3: Керченская крепость\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LF4W"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/kerch/hotels/")
        elif message.text == 'Севастополь🏛':
            bot.send_message(message.chat.id, "1: Бронебашенная Береговая Батарея 35\n"
                                              "2: Малахов курган\n"
                                              "3: Панорама (Оборона Севастополя 1854–1855 гг.)\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LF4c"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/sevastopol/hotels/")
        elif message.text == 'Ялта🏛':
            bot.send_message(message.chat.id, "1: Дом-музей А.П.Чехова\n"
                                              "2: Ялтинский историко-литературный музей\n"
                                              "3: Музей автомобильного искусства\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LF4r"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/yalta/hotels/")
        elif message.text == 'Тамань🏛':
            bot.send_message(message.chat.id, "1: Таманский музейный комплекс\n"
                                              "2: Дом-музей Лермонтова\n"
                                              "3: Шато-Тамань\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFY7"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/taman/hotels/")
        elif message.text == 'Сочи🏛':
            bot.send_message(message.chat.id, "1: Смотровая башня на горе Ахун\n"
                                              "2: Сочи Парк\n"
                                              "3: Парк Ривьера\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFYt"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvifu")
        elif message.text == 'Адлер🏛':
            bot.send_message(message.chat.id, "1: Дворец зимнего спорта Айсберг\n"
                                              "2: Электрический музей Николы Тесла\n"
                                              "3: Механический музей Леонардо да Винчи\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFYQ"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvify")
        elif message.text == 'Лазоревское🏛':
            bot.send_message(message.chat.id, "1: Крабовое ущелье\n"
                                              "2: Мамедово ущелье\n"
                                              "3: Берендеево царство\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFYd"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigf")
        elif message.text == 'Геленджик🏛':
            bot.send_message(message.chat.id, "1: Парк Римская Империя\n"
                                              "2: Геленджикский створный маяк\n"
                                              "3: Батарея №394 капитана А.Э. Зубкова\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFYS"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigp")
        elif message.text == 'Туапсе🏛':
            bot.send_message(message.chat.id, "1: Мыс Кадош\n"
                                              "2: Диспетчерская база управления морского порта\n"
                                              "3: Историко-краеведческий музей им. Н.Г. Полетаева\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFBn"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigr")
        elif message.text == 'Дербент🏛':
            bot.send_message(message.chat.id, "1: Архитектурный комплекс Цитадель Нарын-Кала\n"
                                              "2: Цитадель и крепостные сооружения древнего Дербента\n"
                                              "3: Музей ковра и декоративно-прикладного искусства\n"
                                              "вот ссылка на еще большее количество достопроемичательностей"
                                              "https://usnd.to/LFB4"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Zqy")
        elif message.text == 'Ахты🏛':
            bot.send_message(message.chat.id, "1:Ахтынские мосты\n"
                                              "2:Ротонда Шарвили\n"
                                              "3:Ахтынская крепость\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Zsd")
        elif message.text == 'Махачкала🏛':
            bot.send_message(message.chat.id, "1: Центральная Джума-мечеть\n"
                                              "2: Дагестанский музей изобразительных искусств\n"
                                              "3: Тарки-Тау\n"
                                              "вот ссылка на еще большее количество достопроемичательностей\n"
                                              "https://usnd.to/LFBJ"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Ztx")
        elif message.text == 'Кизляр🏛':
            bot.send_message(message.chat.id, "1: Монумент Память\n"
                                              "2: Аллея Славы\n"
                                              "3: Пушкинский сквер\n"
                                              "вот ссылка на еще большее количество достопроемичательностей\n"
                                              "https://turum.net/ru/kizlyar/places/"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZvE")
        elif message.text == 'Буйнакск🏛':
            bot.send_message(message.chat.id, "1: Gimry Tunnel\n"
                                              "2: Сарыкум by Cronwell Hotel&SPA\n"
                                              "3: Гимринское ущелье\n"
                                              "вот ссылка на еще большее количество достопроемичательностей\n"
                                              "https://usnd.to/LFBf"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0Zy6")
        elif message.text == 'Ялта🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное место - Скала Алим\n"
                                              "вот бельше информации"
                                              "https://usnd.to/LFQO"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihf")
        elif message.text == 'Алушта🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное место - Куш-Кая\n"
                                              "вот бельше информации"
                                              "https://usnd.to/LFQO"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZD9")
        elif message.text == 'Симферополь🧗🏼‍♂':
            bot.send_message(message.chat.id, " Cамое популярное место - cкалы в районе 'Пионерское' \n"
                                              "вот бельше информации"
                                              "https://usnd.to/LFQO"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZEA")
        elif message.text == 'Судак🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное место - Скала «Болван»\n"
                                              "вот бельше информации"
                                              "https://usnd.to/LFQO"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihh")
        elif message.text == 'Бахчисарай🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное место - Ущелье Салачик\n"
                                              "вот бельше информации"
                                              "https://usnd.to/LFQO"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZH3")
        elif message.text == 'Архыз🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное восхождение на 3 вершины\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZIa")
        elif message.text == 'Сочи🧗🏼‍♂':
            bot.send_message(message.chat.id, " Cамый популярный маршрут :"
                                              " переход из Красной Поляны через Энгельмановы Поляны и "
                                              "озера Кардывач в Абхазию, на озеро Рица\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvifu")
        elif message.text == 'Кисловодск🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное место - Берёзовая балка\n"
                                              "Вот дополнительная информация: "
                                              "https://usnd.to/FsQq"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZKV")
        elif message.text == 'Владикавказ🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное место - скалодром Раёк\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZMq")
        elif message.text == 'Дубки🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное место - Сулакский каньон\n"
                                              "Вот ссылка на сайт для бронирования отелей")
        elif message.text == 'Эльбрус🧗🏼‍♂':
            bot.send_message(message.chat.id, "Cамое популярное место - гора Эльбрус\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0ZYO")
        elif message.text == 'Сочи🤿':
            bot.send_message(message.chat.id, "В Сочи присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://turnado.net/ru/c-sochi/a-diving/\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvifu")
        elif message.text == 'Адлер🤿':
            bot.send_message(message.chat.id, "В Адлере присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://turnado.net/ru/c-sochi/a-diving/\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvify ")
        elif message.text == 'Лазаревское🤿':
            bot.send_message(message.chat.id, "В Лазореввском присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://turnado.net/ru/c-lazarevskoe/a-diving/ "
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              " http://surl.li/bvigf")
        elif message.text == 'Кучугуры🤿':
            bot.send_message(message.chat.id, "В Кучеугурах присутствует давйвинг с катера и с берега\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigl")
        elif message.text == 'Анапа🤿':
            bot.send_message(message.chat.id, "В Анапе присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://myanapa.ru/razvlechenia/dajving-v-anape/"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              " http://surl.li/bvigo")
        elif message.text == 'Геленджик🤿':
            bot.send_message(message.chat.id, "В Геленджике присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://blacksea-trips.ru/dajving-v-gelendzhike.html"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigp")
        elif message.text == 'Туапсе🤿':
            bot.send_message(message.chat.id, "В Туапсе присутствует давйвинг с катера и с берега\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigr")
        elif message.text == 'Феодосия🤿':
            bot.send_message(message.chat.id, "В Феодосии присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://turnado.net/ru/c-feodosiya/a-diving/"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/feodosiya/hotels/")
        elif message.text == 'Ялта🤿':
            bot.send_message(message.chat.id, "В Ялте присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://turnado.net/ru/c-yalta/a-diving/"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihf")
        elif message.text == 'Судак🤿':
            bot.send_message(message.chat.id, "В Судаке присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://turnado.net/ru/c-sudak/a-diving/"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/sudak/hotels/")
        elif message.text == 'Евпатория🤿':
            bot.send_message(message.chat.id, "В Евпатории присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://turnado.net/ru/c-evpatoriya/a-diving/"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihj")
        elif message.text == 'Севастополь🤿':
            bot.send_message(message.chat.id, "В Севастополе присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://mater-bober.ru/"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihm")
        elif message.text == 'Алупка🤿':
            bot.send_message(message.chat.id, "В Алупке присутствует давйвинг с катера и с берега\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EU2")
        elif message.text == 'Коктебель🤿':
            bot.send_message(message.chat.id, "В Коктебеле присутствует давйвинг с катера и с берега\n"
                                              "ваот ссылка: https://turnado.net/ru/c-koktebel/a-diving/"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EWC")
        elif message.text == 'Керчь🤿':
            bot.send_message(message.chat.id, "В Керчи присутствует давйвинг с катера и с берега\n"
                                              "вот ссылка: https://usnd.to/F39d"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EYP")
        elif message.text == 'Феодосия🏄‍♂':
            bot.send_message(message.chat.id, "Берег приспособлен для занятий серфинга в Крыму: "
                                              "скалы и камни здесь отсутствуют, нет сильных прибоев,"
                                              " температурный режим воды поддерживается теплым.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://tvil.ru/city/feodosiya/hotels/")
        elif message.text == 'Евпатория🏄‍♂':
            bot.send_message(message.chat.id, "Вот ссылка на подробную информацию и бронирование"
                                              "https://usnd.to/F3N0\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihj")
        elif message.text == 'Севастополь🏄‍♂':
            bot.send_message(message.chat.id, "Вот ссылка на подробную информацию и бронирование"
                                              "https://usnd.to/F3Ny\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihm")
        elif message.text == 'Алупка🏄‍♂':
            bot.send_message(message.chat.id, "Самый распространенный - это sup серфинг\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EU2")
        elif message.text == 'Коктебель🏄‍♂':
            bot.send_message(message.chat.id, "Вот ссылка на подробную информацию и бронирование"
                                              "https://usnd.to/F3NR\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EWC")
        elif message.text == 'Керчь🏄‍♂':
            bot.send_message(message.chat.id, "Вот ссылка на подробную информацию и бронирование"
                                              "https://usnd.to/F3vc\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd0EYP")
        elif message.text == 'Ялта🏄‍♂':
            bot.send_message(message.chat.id, "Самый распространенный - это sup серфинг\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvihf")
        elif message.text == 'Сочи🏄‍♂':
            bot.send_message(message.chat.id, "В Сочи есть Классический серфинг, SUP-серфинг, виндсерфинг, вейксерфинг\n"
                                              "поопутярны споты в Имеретинской бухте и Станция No Bad Days"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvifu")
        elif message.text == 'Адлер🏄‍♂':
            bot.send_message(message.chat.id, "Самый распространенный - это sup серфинг\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvify")
        elif message.text == 'Туапсе🏄‍♂':
            bot.send_message(message.chat.id, "Самый распространенный - это sup серфинг\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigr")
        elif message.text == 'Лазаревское🏄‍♂':
            bot.send_message(message.chat.id, "Самые популярные - это виндсерфинг и sup серфинг"
                                              "вот ссылка на один из ресурсов \n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigf")
        elif message.text == 'Кучугуры🏄‍♂':
            bot.send_message(message.chat.id, "Специального сёрфинг-центра с прокатом сёрфов, инструкторами,"
                                              " обучающими новичков, в Кучугурах нет. Однако спортсменами из "
                                              "многих уголков России подмечено, что Азовское побережье Тамани обладает "
                                              "исключительно подходящей розой ветров для занятий этим видом спорта\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigl")
        elif message.text == 'Анапа🏄‍♂':
            bot.send_message(message.chat.id, "Один из лучших спотов России\n"
                                              "Условия для катания на серфинге в Анапе не простые."
                                              "Вот побольше информации о серфинге в Анапе"
                                              "https://usnd.to/F3vL"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigo")
        elif message.text == 'Геленджик🏄‍♂':
            bot.send_message(message.chat.id, "Самый распространенный - это sup серфинг\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "http://surl.li/bvigp")
        elif message.text == 'Алушта⛷':
            bot.send_message(message.chat.id, "Ангарский перевал – одно из знаменитых мест Крыма,"
                                              "с ним связаны важные исторические события, а красота природы,"
                                              "окружающей эту достопримечательность, восхищает всех\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1VL0")
        elif message.text == 'Ай Петри⛷':
            bot.send_message(message.chat.id, "Самая снежная точка на карте — гора Ай-Петри."
                                              " Именно здесь зимой собираются лыжники, сноубордисты"
                                              " и желающие покататься на «ватрушках».\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1VPg")
        elif message.text == 'Красная Поляна⛷':
            bot.send_message(message.chat.id, "Красная Поляна — яркая. Этот курорт стремительно расцвел "
                                              "и всего за несколько лет заслужил статус самого респектабельного"
                                              " горнолыжного кластера России.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1VVu")
        elif message.text == 'Лаго-Наки⛷':
            bot.send_message(message.chat.id, "Лаго-Наки – это обширная территория, часть которой находится "
                                              "на территории Кавказского заповедника. Средняя высота плато"
                                              " – 2000 м над уровнем моря. Это всесезонный курорт\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1VWM")
        elif message.text == 'Псебай⛷':
            bot.send_message(message.chat.id, "Трассы поддерживаются в идеальном состоянии с помощью новейшего "
                                              "оборудования, предоставленного итальянской компанией Liski, трассы"
                                              " практически исключают травмирование спортсменов, так как организаторами"
                                              " отдыха предприняты все меры для соблюдения безопасности туристов.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1VZ1")
        elif message.text == 'Бобровый лог⛷':
            bot.send_message(message.chat.id, "Для любителей горных лыж и сноуборда работают 15 трасс и "
                                              "2 учебный склона. По уровням сложности: 6 «черных» трасс "
                                              "(требуется экспертный уровень катания), 5 «красных» трасс "
                                              "(продвинутый уровень), 3 «синих» трассы (средний уровень) и"
                                              " 1 «зеленая» трасса (для новичков). Для обучения начинающих"
                                              " подготовлены 2 учебных склона.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1W16")
        elif message.text == 'Сорочаны⛷':
            bot.send_message(message.chat.id, "Горнолыжный курорт «Сорочаны» предлагает спортсменам 10 "
                                              "трасс разного уровня сложности с перепадом высот от 40 до 90 метров,"
                                              " шириной до 70 метров и протяженностью до 1050 метров\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1W4l")
        elif message.text == 'Игора⛷':
            bot.send_message(message.chat.id, "На курорте Игора самые высокие горы и самые протяженные склоны в"
                                              " Ленинградской области. Максимальный перепад "
                                              "высот - 120 метров, длина – 1210 метров. Система искусственного"
                                              " снегообразования. Ежедневная обработка склонов ратраками.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1W83")
        elif message.text == 'Большой Вудъявр⛷':
            bot.send_message(message.chat.id, "Горнолыжный курорт «Большой Вудъявр» - это разнообразие маршрутов. "
                                              "Общий перепад высот "
                                              "составляет порядка 650 метров. Любой начинающий или профессиональный "
                                              "горнолыжник и сноубордист с радостью оставит на курорте свой след.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1WaP")
        elif message.text == 'Домбай⛷':
            bot.send_message(message.chat.id, "Престижный горный курорт Домбай (Домбайская поляна) расположился "
                                              "на территории Карачаево-Черкесской республики, у подножия Главного"
                                              " хребта Кавказских гор. Находится поляна на высоте 1650 метров над "
                                              "уровнем моря. Центр этой живописной территории соединяют три ущелья:"
                                              " Алибек, Аманауз и Домбай-Ульген, которая считается наивысшей точкой "
                                              "курорта - 4046 м.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1Wg1")
        elif message.text == 'Гора Соболиная⛷':
            bot.send_message(message.chat.id, " Пожалуй, самый популярный зимний объект при упоминании об активном "
                                              "отдыхе на Байкале - это крупнейший в Восточной Сибири горнолыжный курорт"
                                              "«Гора Соболиная», расположенный близ города Байкальска на северном склоне"
                                              " одноименной горы.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1Wif")
        elif message.text == 'Завьялиха⛷':
            bot.send_message(message.chat.id, "Горнолыжный курорт Завьялиха расположен на юго-восточной окраине г."
                                              " Трёхгорный, на противоположном от города правом берегу реки Юрюзань. "
                                              "На курорте есть 10 горнолыжных трасс общей протяжённостью около 16.5. км:"
                                              " одна чёрная трасса, шесть красных, синяя, зелёная и детская трасса.\n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "https://vk.cc/cd1WjW")
        else:
            bot.send_message(message.chat.id, "Вы ввели что то не то(")


bot.polling(none_stop=True)
