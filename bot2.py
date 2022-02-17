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
    e1 = types.KeyboardButton('Горнолыжный⛷')
    e2 = types.KeyboardButton('Экспедиции🐻‍❄')
    e3 = types.KeyboardButton('Дайвинг🧊🤿')
    e7 = types.KeyboardButton('⬅Назад🏂')

    markup3.add(e1, e2, e3, e7)

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

    markup5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sb1 = types.KeyboardButton('Сочи🏝')
    sb2 = types.KeyboardButton('Геленджик🏝')
    sb3 = types.KeyboardButton('Адлер🏝')
    sb4 = types.KeyboardButton('Туапсе🏝')
    sb5 = types.KeyboardButton('Ейск🏝')
    sb6 = types.KeyboardButton('Ялта🏝')
    sb7 = types.KeyboardButton('⏪Назад🏝')
    sb8 = types.KeyboardButton('Далее🏝➡')

    markup5.add(sb1, sb2, sb3, sb4, sb5, sb6, sb7, sb8)

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

    markup8.add(nn1, nn2, nn3, nn4, nn5, nn7)

    markup24 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Дубки🏔')
    kg2 = types.KeyboardButton('Махачкала🏔')
    kg3 = types.KeyboardButton('Хунзах🏔')
    kg5 = types.KeyboardButton('⏮Назад🏔')
    kg8 = types.KeyboardButton('Ахты🏔')
    kg6 = types.KeyboardButton('Карадах🏔')
    #https: // bolshayastrana.com / blog / samye - krasivye - mesta - v - dagestane - 62
    #https://www.russiadiscovery.ru/news/dostoprimechatelnosti_severnogo_kavkaza/
    #https://tur-ray.ru/krasnodarskiy-kray-dostoprimechatelnosti.html

    markup24.add(kg1, kg2, kg3, kg5, kg6, kg8)

    markup25 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Анапа🏔')
    kg2 = types.KeyboardButton('Гелендик🏔')
    kg3 = types.KeyboardButton('Туапсе🏔')
    kg4 = types.KeyboardButton('Сочи🏔')
    kg5 = types.KeyboardButton('Адлер🏔')
    kg8 = types.KeyboardButton('⏮Назад🏔')
    kg6 = types.KeyboardButton('тамань🏔')
#https: // kurort.yuga.ru / articles / 3737.html

    markup25.add(kg1, kg2, kg3, kg4, kg5, kg6, kg8)

    markup100 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Алушта🏔')
    kg2 = types.KeyboardButton('Ялта🏔')
    kg3 = types.KeyboardButton('Севастополь🏔')
    kg4 = types.KeyboardButton('⏮Назад🏔')
    kg8 = types.KeyboardButton('Бахчисарай🏔')
    kg6 = types.KeyboardButton('Феодосия🏔')
#https://sutochno.ru/info/krasivye-mesta-kryma

    markup100.add(kg1, kg2, kg3, kg4, kg6, kg8)

    markup26 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Тюнгур🏔')
    kg2 = types.KeyboardButton('Чибит🏔')
    kg3 = types.KeyboardButton('Джазаторское🏔') #https://www.marshruty.ru/Places/Place.aspx?PlaceID=75176aa5-3b0a-4b49-b1fe-bf6fdcba6ea2
    kg4 = types.KeyboardButton('⏮Назад🏔')
    #https://www.kp.ru/russia/gory-rossii/altajskie/

    markup26.add(kg1, kg2, kg3, kg4)

    markup27 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('⏮Назад🏔')
    kg2 = types.KeyboardButton('Вилючинск🏔')
    kg6 = types.KeyboardButton('Петропавловск-Камчатский🏔')
    #https://kamchatkaland.ru/note/gory-kamchatki

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
    #https://tripplanet.ru/dostoprimechatelnosti-severnogo-kavkaza/#Krepost_Naryn-Kala

    markup30.add(kg1, kg2, kg3, kg4, kg5, kg6)

    markup28 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kg1 = types.KeyboardButton('Бахчисарай🏛')
    kg2 = types.KeyboardButton('Судак🏛')
    kg3 = types.KeyboardButton('Феодосия🏛')
    kg4 = types.KeyboardButton('Керч🏛')
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
    kg1 = types.KeyboardButton('Белокуриха🏃') #https://edem-altay.ru/
    kg2 = types.KeyboardButton('Кисловодск🏃') #https://www.vertebra.clinic/
    kg3 = types.KeyboardButton('Московская область🏃')#https://pakhra.amaks-kurort.ru/
    kg4 = types.KeyboardButton('Ессентуки🏃')#https://www.istochnik-essentuki.ru/
    kg5 = types.KeyboardButton('Ялта🏃')#https://mriya-resort.online/?gclid=CjwKCAiA6Y2QBhAtEiwAGHybPYPildr9o6q4NOY84H2dR0BHt-kBvk7IZ82mwFss9wgTnBF2kZ8K7RoCvwcQAvD_BwE
    kg6 = types.KeyboardButton('Саки🏃')# https://yurmino.ru/
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
    kz3 = types.KeyboardButton('Пересыпь🤿')
    kz4 = types.KeyboardButton('Приморско-Ахтарск🤿')
    kz10 = types.KeyboardButton('Лазаревское🤿')
    kz8 = types.KeyboardButton('⏮Назад🤿')
    kz7 = types.KeyboardButton('Кучугуры🤿')
    kz9 = types.KeyboardButton('Анапа🤿')
    kz5 = types.KeyboardButton('Геленджик🤿')

    markup33.add(kz1, kz2, kz3, kz4, kz5, kz7, kz8, kz9, kz10)

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
    kz3 = types.KeyboardButton('Пересыпь🏄‍♂')
    kz4 = types.KeyboardButton('Приморско-Ахтарск🏄‍♂')
    kz10 = types.KeyboardButton('Лазаревское🏄‍♂')
    kz8 = types.KeyboardButton('⏮Назад🏄‍♂')
    kz7 = types.KeyboardButton('Кучугуры🏄‍♂')
    kz9 = types.KeyboardButton('Анапа🏄‍♂')
    kz5 = types.KeyboardButton('Геленджик🏄‍♂')

    markup36.add(kz1, kz2, kz3, kz4, kz5, kz7, kz8, kz9, kz10)

    markup18 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sc1 = types.KeyboardButton('Сочи⛷')
    sc2 = types.KeyboardButton('Красноярск⛷')
    sc3 = types.KeyboardButton('Москова⛷')
    sc5 = types.KeyboardButton('Санкт-Петербург⛷')
    sc6 = types.KeyboardButton('Кировск⛷')
    sc7 = types.KeyboardButton('Домбай⛷')
    sc8 = types.KeyboardButton('⏪Назад⛷')
    sc9 = types.KeyboardButton('Иркутск⛷')

    markup18.add(sc1, sc2, sc3, sc5, sc6, sc7, sc8, sc9)

    if message.chat.type == 'private':
        if message.text == 'Туда где тепло🌴':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup1)
        elif message.text == 'Туда где холодно❄️':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup2)
        elif message.text == 'Экстрим🏂':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup3)
        elif message.text == '⬅Назад🏂':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup2)
        elif message.text == '⬅Назад🌴':
            bot.send_message(message.chat.id, "Ваши предпочтения к путешествию", reply_markup=markup10)
        elif message.text == '⬅Назад❄️':
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
        elif message.text == 'Экстрим🏂':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup3)
        elif message.text == 'Горнолыжный⛷':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup18)
        elif message.text == '⏪Назад⛷':
            bot.send_message(message.chat.id, "что именно вы хотите?", reply_markup=markup3)
        elif message.text == 'Крымский ПО🟩':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup7)
            bot.send_photo(message.chat.id, p3)
        elif message.text == '⏮Назад🏝':
            bot.send_message(message.chat.id, "Какая область вас больше интересует?", reply_markup=markup66)
            bot.send_photo(message.chat.id, p1)
        elif message.text == 'Крым🟥':
            bot.send_message(message.chat.id, "Вот список городов", reply_markup=markup28)
        elif message.text == 'Германия':
            bot.send_message(message.chat.id, "", reply_markup=markup9)
        elif message.text == 'Италия':
            bot.send_message(message.chat.id, "", reply_markup=markup4)
        elif message.text == 'Великобритания':
            bot.send_message(message.chat.id, "", reply_markup=markup4)
        elif message.text == 'Пляж🏝':
            bot.send_photo(message.chat.id, p1)
        elif message.text == 'Геленджик🏝':
            bot.send_message(message.chat.id, "В Геленджике представлены песчаные и галечные пляжи \n"
                                              "Вот ссылка на сайт для бронирования отелей\n"
                                              "  https://inlnk.ru/NDBjL2")
        else:
            bot.send_message(message.chat.id, "Такой команды не существует")


bot.polling(none_stop=True)
