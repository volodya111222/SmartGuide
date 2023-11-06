import telebot
from telebot import types

doni = [1603857681]
bot = telebot.TeleBot('6429952178:AAHK0r__48ligeLwPogxTUxZxLMJ-Tw0xdc')

@bot.message_handler(commands=['start'])
def start(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('волейбол')
        btn2 = types.KeyboardButton('футбол')
        btn3 = types.KeyboardButton('баскетбол')
        btn4 = types.KeyboardButton('хоккей')
        btn5 = types.KeyboardButton('ДРУГОЕ')
        btn6 = types.KeyboardButton('хобихорсинг')
        btn7 = types.KeyboardButton('шахматы')
        btn8 = types.KeyboardButton('кёрлинг')
        markup.add(btn1, btn2, btn3, btn4, btn5)



        bot.send_message(message.from_user.id,'здравствуйте! этот бот поможет вам найти новых знакомых увлекающихся тем же видом спорта что и вы.', reply_markup=markup)
        bot.register_next_step_handler(message, txt)





@bot.message_handler(content_types=['text'])
def txt(message):
    markup = types.InlineKeyboardMarkup()
    markup2 = types.InlineKeyboardMarkup()
    markup3 = types.InlineKeyboardMarkup()
    markup4 = types.InlineKeyboardMarkup()
    markup5 = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text='вступить в сообщество', url='https://t.me/+I1iTrV2hsRQ1NjI6')
    button2 = types.InlineKeyboardButton(text='КУПИТЬ', callback_data='send_photo')
    button77 = types.InlineKeyboardButton(text='я оплатил(а)', callback_data='YES')
    button3 = types.InlineKeyboardButton(text='хобихорсинг', url='https://t.me/+I1iTrV2hsRQ1NjI6')
    button4 = types.InlineKeyboardButton(text='шахматы', url='https://t.me/+I1iTrV2hsRQ1NjI6')
    button5 = types.InlineKeyboardButton(text='кёрлинк', url='https://t.me/+I1iTrV2hsRQ1NjI6')

    if message.text == 'волейбол':
        markup.add(button1)
        teext = 'вот сообщество в котором вы можете найти друзей, которые так же как и вы любят проводить время за игрой в волейбол \n здесь вы можете найти все актуальные новости о волейболе - "здесь будет ссылка"'
        bot.send_message(message.chat.id, teext,  reply_markup=markup)

    elif message.text == 'ДРУГОЕ':
        markup.add(button2)
        bot.send_message(message.chat.id, '"вот сообщество в котором вы можете найти друзей. ссылка на сайт с новостями об этом спорте - "здесь будетссылка"', reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.data == 'send_photo':
            file = open('чек.jpg', 'rb')
            bot.send_photo(call.message.chat.id, file)
            markup.add(button77)
            bot.send_message(message.chat.id, 'если вы оплатили то жмите сюда',  reply_markup=markup)

        if call.data == 'YES' and message.chat.id not in doni:
            bot.send_message(message.chat.id, 'извтните, но вы не можете воспользоваться коммандой так как не купили премиум')

        elif call.data == 'YES':
            markup.add(button3, button4, button5)
            bot.send_message(message.chat.id, 'вот премиум виды спорта', reply_markup=markup)


bot.polling(none_stop=True, interval=0)