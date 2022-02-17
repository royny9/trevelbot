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
                                              "  https://inlnk.ru/NDBjL2",)
        elif message.text == 'Арбат':
            bot.send_message(message.chat.id, "http://surl.li/ayblc",)
        elif message.text == 'Большой театр':
            bot.send_message(message.chat.id, "http://surl.li/aybls",)
        elif message.text == 'ВДНХ':
            bot.send_message(message.chat.id, "http://surl.li/ayblw",)
        elif message.text == 'Кремль':
            bot.send_message(message.chat.id, "http://surl.li/aybma",)
        elif message.text == 'Красная площадь':
            bot.send_message(message.chat.id, "http://surl.li/aybme",)
        elif message.text == 'Госуда́рственный Эрмита́ж':
            bot.send_message(message.chat.id, "http://surl.li/kdap",)
        elif message.text == 'Большой Петергофский дворец':
            bot.send_message(message.chat.id, "http://surl.li/aybnl",)
        elif message.text == 'Екатерининский дворец и парк':
            bot.send_message(message.chat.id, "http://surl.li/aybnn",)
        elif message.text == 'Александровский парк':
            bot.send_message(message.chat.id, "http://surl.li/aybnp",)
        elif message.text == 'Музей Фаберже':
            bot.send_message(message.chat.id, "http://surl.li/aybnr",)
        elif message.text == 'Петропавловская крепость':
            bot.send_message(message.chat.id, "http://surl.li/aybnu",)
        elif message.text == 'Казанский Кремль':
            bot.send_message(message.chat.id, "http://surl.li/ayboo",)
        elif message.text == 'Мечеть Кул-Шариф':
            bot.send_message(message.chat.id, "http://surl.li/aybor", )
        elif message.text == 'Кремлевская набережная':
            bot.send_message(message.chat.id, "http://surl.li/aybow", )
        elif message.text == 'Дворец земледельцев':
            bot.send_message(message.chat.id, "http://surl.li/ayboz", )
        elif message.text == 'Старо-татарская слобода':
            bot.send_message(message.chat.id, "http://surl.li/aybpb", )
        elif message.text == 'Дом Ушковой':
            bot.send_message(message.chat.id, "http://surl.li/aybpc", )
        elif message.text == 'Скайпарк':
            bot.send_message(message.chat.id, "http://surl.li/aybpk", )
        elif message.text == 'Солохаул':
            bot.send_message(message.chat.id, "http://surl.li/aybpp", )
        elif message.text == 'Олимпийский парк':
            bot.send_message(message.chat.id, "http://surl.li/aybpv", )
        elif message.text == 'Сочинский океанариум':
            bot.send_message(message.chat.id, "http://surl.li/aybpw", )
        elif message.text == '«Ущелье дьявола»':
            bot.send_message(message.chat.id, "http://surl.li/aydck", )
        elif message.text == 'Сочи Парк':
            bot.send_message(message.chat.id, "http://surl.li/aybqa", )
        elif message.text == 'Усадьба Рукавишниковых':
            bot.send_message(message.chat.id, "http://surl.li/aybsd", )
        elif message.text == 'Стрелка Оки и Волги':
            bot.send_message(message.chat.id, "http://surl.li/aybse", )
        elif message.text == 'Чкаловская мемориальная лестница':
            bot.send_message(message.chat.id, "http://surl.li/aybsg", )
        elif message.text == 'Нижегородский кремль':
            bot.send_message(message.chat.id, "http://surl.li/aybsj", )
        elif message.text == 'Собор Александра Невского':
            bot.send_message(message.chat.id, "http://surl.li/aybsk", )
        elif message.text == 'Государственный банк':
            bot.send_message(message.chat.id, "http://surl.li/aybsl", )
        elif message.text == 'Остров Канта и Кафедральный собор':
            bot.send_message(message.chat.id, "http://surl.li/aybsv", )
        elif message.text == 'Куршская коса':
            bot.send_message(message.chat.id, "http://surl.li/aybsx", )
        elif message.text == 'Кёнигсбергский замок':
            bot.send_message(message.chat.id, "http://surl.li/aybtb", )
        elif message.text == 'Рыбная деревня':
            bot.send_message(message.chat.id, "http://surl.li/aybtl", )
        elif message.text == 'Королевские ворота':
            bot.send_message(message.chat.id, "http://surl.li/aybtu", )
        elif message.text == 'Музей мирового океана':
            bot.send_message(message.chat.id, "http://surl.li/aybtn", )
        elif message.text == 'Вантовые мосты':
            bot.send_message(message.chat.id, "http://surl.li/aybuc", )
        elif message.text == 'Остров Русский':
            bot.send_message(message.chat.id, "http://surl.li/aybug", )
        elif message.text == 'Бухта Золотой Рог':
            bot.send_message(message.chat.id, "http://surl.li/aybuh", )
        elif message.text == 'Сопка Орлиное Гнездо':
            bot.send_message(message.chat.id, "https://clck.ru/ZHsJ4", )
        elif message.text == 'Николаевские Триумфальные ворота':
            bot.send_message(message.chat.id, "https://clck.ru/ZHsLa", )
        elif message.text == 'Владивостокский фуникулёр':
            bot.send_message(message.chat.id, "http://surl.li/aybuv", )
        elif message.text == 'Парк на Стрелке':
            bot.send_message(message.chat.id, "http://surl.li/aybvk", )
        elif message.text == 'Церковь Ильи Пророка':
            bot.send_message(message.chat.id, "http://surl.li/aybvl", )
        elif message.text == 'Успенский собор':
            bot.send_message(message.chat.id, "http://surl.li/aybvp", )
        elif message.text == 'Толгский монастырь':
            bot.send_message(message.chat.id, "http://surl.li/aybvs", )
        elif message.text == 'Казанский женский монастырь':
            bot.send_message(message.chat.id, "http://surl.li/aybvv", )
        elif message.text == 'Волжская башня':
            bot.send_message(message.chat.id, "http://surl.li/aybvy", )
        elif message.text == 'Ботанический сад Атланты':
            bot.send_message(message.chat.id, "http://surl.li/aydea", )
        elif message.text == 'Аквариум Джорджии':
            bot.send_message(message.chat.id, "http://surl.li/aydeg", )
        elif message.text == 'LEGOLAND':
            bot.send_message(message.chat.id, "http://surl.li/aydem", )
        elif message.text == 'World of Coca-Cola':
            bot.send_message(message.chat.id, "http://surl.li/ayder", )
        elif message.text == 'Мост Золотые Ворота':
            bot.send_message(message.chat.id, "http://surl.li/aydfe", )
        elif message.text == 'Алькатрас':
            bot.send_message(message.chat.id, "http://surl.li/aydfg", )
        elif message.text == 'Канатный трамвай':
            bot.send_message(message.chat.id, "http://surl.li/aydfh", )
        elif message.text == 'Ломбард-стрит':
            bot.send_message(message.chat.id, "http://surl.li/aydfl", )
        elif message.text == 'Пирс 39':
            bot.send_message(message.chat.id, "http://surl.li/aydfp", )
        elif message.text == 'Тропа Свободы':
            bot.send_message(message.chat.id, "http://surl.li/aydfs", )
        elif message.text == 'North End':
            bot.send_message(message.chat.id, "http://surl.li/aydgn", )
        elif message.text == 'Общественный сад':
            bot.send_message(message.chat.id, "http://surl.li/aydgi", )
        elif message.text == 'Бостонская публичная библиотека':
            bot.send_message(message.chat.id, "http://surl.li/aydhf", )
        elif message.text == 'Спейс-Нидл':
            bot.send_message(message.chat.id, "http://surl.li/aydhk", )
        elif message.text == 'Музей авиации':
            bot.send_message(message.chat.id, "http://surl.li/aydhl", )
        elif message.text == 'Музей искусств':
            bot.send_message(message.chat.id, "http://surl.li/aydhr", )
        elif message.text == 'Сад Кубота':
            bot.send_message(message.chat.id, "http://surl.li/aydic", )
        elif message.text == 'Плотина Гувера':
            bot.send_message(message.chat.id, "http://surl.li/aydih", )
        elif message.text == 'Paris Las Vegas':
            bot.send_message(message.chat.id, "http://surl.li/aydjk", )
        elif message.text == 'Казино «Белладжио»':
            bot.send_message(message.chat.id, "http://surl.li/aydjm", )
        elif message.text == 'Caesars Palace':
            bot.send_message(message.chat.id, "http://surl.li/aydjr", )
        elif message.text == 'T-Mobile Arena':
            bot.send_message(message.chat.id, "http://surl.li/aydjw", )
        elif message.text == 'Las Vegas Motor Speedway':
            bot.send_message(message.chat.id, "http://surl.li/aydkd", )
        elif message.text == 'Башня свободы':
            bot.send_message(message.chat.id, "http://surl.li/wvic", )
        elif message.text == 'Бродвей':
            bot.send_message(message.chat.id, "http://surl.li/aydkm", )
        elif message.text == 'Пятая авеню':
            bot.send_message(message.chat.id, "http://surl.li/aydkn", )
        elif message.text == 'Таймс-Сквер':
            bot.send_message(message.chat.id, "http://surl.li/aydko", )
        elif message.text == 'Уолл-стрит':
            bot.send_message(message.chat.id, "http://surl.li/aydkq", )
        elif message.text == 'Биопарк Валенсии':
            bot.send_message(message.chat.id, "https://inlnk.ru/JjjBM8", )
        elif message.text == 'Океанографический парк':
            bot.send_message(message.chat.id, "https://goo.su/TtM", )
        elif message.text == 'Валенсийский собор':
            bot.send_message(message.chat.id, "https://goo.su/A44", )
        elif message.text == 'Шелковая биржа':
            bot.send_message(message.chat.id, "https://goo.su/ry3", )
        elif message.text == 'Башня Хиральда':
            bot.send_message(message.chat.id, "https://goo.su/YuV", )
        elif message.text == 'Кафедральный собор в Севилье':
            bot.send_message(message.chat.id, "https://goo.su/Igo", )
        elif message.text == 'Дворец Альказар в Севилье':
            bot.send_message(message.chat.id, "https://goo.su/9qeu", )
        elif message.text == 'Дворец Сан-Тельмо':
            bot.send_message(message.chat.id, "https://goo.su/9kdI", )
        elif message.text == 'Бульвар Рамбла':
            bot.send_message(message.chat.id, "https://goo.su/WLl", )
        elif message.text == 'Рынок Бокерия':
            bot.send_message(message.chat.id, "https://goo.su/l9f", )
        elif message.text == 'Музей Пикассо':
            bot.send_message(message.chat.id, "https://goo.su/9YeB", )
        elif message.text == 'Аквариум Барселоны':
            bot.send_message(message.chat.id, "https://goo.su/JTd", )
        elif message.text == 'Арена Лас-Вентас':
            bot.send_message(message.chat.id, "https://goo.su/dMt", )
        elif message.text == 'Королевский дворец в Мадриде':
            bot.send_message(message.chat.id, "https://goo.su/9FtC", )
        elif message.text == 'музей Прадо':
            bot.send_message(message.chat.id, "https://goo.su/ylm", )
        elif message.text == 'Собор Альмудена':
            bot.send_message(message.chat.id, "https://goo.su/9kw8", )
        elif message.text == 'Эйфелева башня':
            bot.send_message(message.chat.id, "https://goo.su/9LZW", )
        elif message.text == 'Собор Парижской Богоматери':
            bot.send_message(message.chat.id, "https://goo.su/a1NB", )
        elif message.text == 'Лувр':
            bot.send_message(message.chat.id, "https://goo.su/9tlI", )
        elif message.text == 'Триумфальная Арка':
            bot.send_message(message.chat.id, "https://goo.su/9maj", )
        elif message.text == 'Музей Матисса':
            bot.send_message(message.chat.id, "https://goo.su/9uv", )
        elif message.text == 'Ботанический сад Ниццы':
            bot.send_message(message.chat.id, "https://goo.su/QOj", )
        elif message.text == 'Замковая гора':
            bot.send_message(message.chat.id, "https://goo.su/9Kiz", )
        elif message.text == 'Нотр-Дам в Ницце':
            bot.send_message(message.chat.id, "https://goo.su/v8Q", )
        elif message.text == 'Форт святого Иоанна':
            bot.send_message(message.chat.id, "https://goo.su/OG9", )
        elif message.text == 'Аббатство Святого Виктора':
            bot.send_message(message.chat.id, "https://goo.su/NWF", )
        elif message.text == 'Кафедральный собор Марселя':
            bot.send_message(message.chat.id, "https://goo.su/9OGg", )
        elif message.text == 'Замок Иф':
            bot.send_message(message.chat.id, "https://goo.su/9UdJ", )
        elif message.text == 'Дворец Роганов':
            bot.send_message(message.chat.id, "https://goo.su/KM5", )
        elif message.text == 'Страсбургский собор':
            bot.send_message(message.chat.id, "https://goo.su/9rGi", )
        elif message.text == 'Маленькая Франция':
            bot.send_message(message.chat.id, "https://goo.su/kaN", )
        elif message.text == 'Музей изобразительного искусства':
            bot.send_message(message.chat.id, "https://goo.su/zsY", )
        elif message.text == 'Берлинская стена':
            bot.send_message(message.chat.id, "https://goo.su/hcf", )
        elif message.text == 'Берлинская телебашня':
            bot.send_message(message.chat.id, "https://goo.su/MIn", )
        elif message.text == 'Бранденбургские ворота':
            bot.send_message(message.chat.id, "https://goo.su/9IyC", )
        elif message.text == 'Рейхстаг':
            bot.send_message(message.chat.id, "https://goo.su/uio", )
        elif message.text == 'Кёльнский собор':
            bot.send_message(message.chat.id, "https://goo.su/afVD", )
        elif message.text == 'Дворец Аугустусбург':
            bot.send_message(message.chat.id, "https://goo.su/9tCA", )
        elif message.text == 'Музей Людвига':
            bot.send_message(message.chat.id, "https://goo.su/Ww5", )
        elif message.text == 'Церковь Святого Мартина':
            bot.send_message(message.chat.id, "https://goo.su/laL", )
        elif message.text == 'Петерскирхе':
            bot.send_message(message.chat.id, "https://goo.su/zD7", )
        elif message.text == 'Фрауэнкирхе в Мюнхене':
            bot.send_message(message.chat.id, "https://goo.su/NOt", )
        elif message.text == 'Азамкирхе':
            bot.send_message(message.chat.id, "https://goo.su/9HkI", )
        elif message.text == 'Альянц Арена':
            bot.send_message(message.chat.id, "https://goo.su/ZCu", )
        elif message.text == 'Гамбургская ратуша':
            bot.send_message(message.chat.id, "https://goo.su/9oCc", )
        elif message.text == 'Галерея современного искусства':
            bot.send_message(message.chat.id, "https://goo.su/9N8m", )
        elif message.text == 'Музей истории Гамбурга':
            bot.send_message(message.chat.id, "https://goo.su/kWo", )
        elif message.text == 'Гамбургский оперный театр':
            bot.send_message(message.chat.id, "https://goo.su/9P8q", )
        elif message.text == 'Арка Константина в Риме':
            bot.send_message(message.chat.id, "https://goo.su/9iUe", )
        elif message.text == 'Вилла Боргезе':
            bot.send_message(message.chat.id, "https://goo.su/Ty7", )
        elif message.text == 'Колизей в Риме':
            bot.send_message(message.chat.id, "https://goo.su/XZE", )
        elif message.text == 'Капитолийский холм':
            bot.send_message(message.chat.id, "https://goo.su/x1d", )
        elif message.text == 'Галерея Амвросиана':
            bot.send_message(message.chat.id, "https://goo.su/asTT", )
        elif message.text == 'Дуомо':
            bot.send_message(message.chat.id, "https://goo.su/9Jip", )
        elif message.text == 'Замок Сфорца':
            bot.send_message(message.chat.id, "https://goo.su/g7n", )
        elif message.text == 'Башня Веласка':
            bot.send_message(message.chat.id, "https://goo.su/BvI", )
        elif message.text == 'Базилика Сан-Лоренцо':
            bot.send_message(message.chat.id, "https://goo.su/9qxS", )
        elif message.text == 'Баптистерий Сан-Джованни':
            bot.send_message(message.chat.id, "https://goo.su/exG", )
        elif message.text == 'Колокольня Джотто':
            bot.send_message(message.chat.id, "https://goo.su/DoK", )
        elif message.text == 'Палаццо-Веккьо':
            bot.send_message(message.chat.id, "https://goo.su/9K8L", )
        elif message.text == 'Гранд-канал':
            bot.send_message(message.chat.id, "https://goo.su/Qqz", )
        elif message.text == 'Дворец дожей':
            bot.send_message(message.chat.id, "https://goo.su/Lr7", )
        elif message.text == 'Ка’д’Оро':
            bot.send_message(message.chat.id, "https://goo.su/Btc", )
        elif message.text == 'Мост Риальто':
            bot.send_message(message.chat.id, "https://goo.su/9UQY", )
        elif message.text == 'Дворец Холирудхаус':
            bot.send_message(message.chat.id, "https://goo.su/MJh", )
        elif message.text == 'Королевская Миля':
            bot.send_message(message.chat.id, "https://goo.su/9Hkc", )
        elif message.text == 'Эдинбургский замок':
            bot.send_message(message.chat.id, "https://goo.su/ad7W", )
        elif message.text == 'Монумент Скотта':
            bot.send_message(message.chat.id, "https://goo.su/9N5V", )
        elif message.text == 'Манчестерский собор':
            bot.send_message(message.chat.id, "https://goo.su/n9Z", )
        elif message.text == 'Стадион Манчестера':
            bot.send_message(message.chat.id, "https://goo.su/OJc", )
        elif message.text == 'Манчестерская ратуша':
            bot.send_message(message.chat.id, "https://goo.su/9yZa", )
        elif message.text == 'Каслфилд':
            bot.send_message(message.chat.id, "https://goo.su/T1I", )
        elif message.text == 'Гарвардский университет':
            bot.send_message(message.chat.id, "https://goo.su/9y6G", )
        elif message.text == 'Массачусетский институт':
            bot.send_message(message.chat.id, "https://goo.su/9xIm", )
        elif message.text == 'Вестминстерское аббатство':
            bot.send_message(message.chat.id, "https://goo.su/DSO", )
        elif message.text == 'Музей Фицуильяма':
            bot.send_message(message.chat.id, "https://goo.su/EyP", )
        elif message.text == 'Биг-Бен':
            bot.send_message(message.chat.id, "https://goo.su/FHO", )
        elif message.text == '«Лондонский глаз»':
            bot.send_message(message.chat.id, "https://goo.su/BeH", )
        elif message.text == 'Букингемский дворец':
            bot.send_message(message.chat.id, "https://goo.su/9qDD", )
        elif message.text == 'Лондонский Тауэр':
            bot.send_message(message.chat.id, "https://goo.su/H9N", )
        elif message.text == '':
            bot.send_message(message.chat.id, "", )
        else:
            bot.send_message(message.chat.id, "Такой команды не существует")


bot.polling(none_stop=True)
