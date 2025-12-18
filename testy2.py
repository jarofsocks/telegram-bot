import telebot
import datetime
import pytz

key = '8269052843:AAFXTSzfa1VYupfNzQDOltE0OF6j9LaKUYU'
id = '-5001720968'
boty = telebot.TeleBot(key)

@boty.message_handler(commands = ['test'])
def take_user_message(message):
    boty.send_message(message.chat.id, f'online: {str(datetime.datetime.now())}')

@boty.message_handler(commands = ['help'])
def take_user_message(message):
    with open('help.txt', 'rb') as help_txt:
        boty.send_message(message.chat.id, help_txt.read())

@boty.message_handler()
def gol(message):
    try:
        user_input = message.text.split(' ',1)
        print(user_input)
        arg = user_input[0]
        text = user_input[1]
        if arg == 'text':
            boty.send_message(id, text)
        elif arg == 'file':
            with open(text, 'rb') as doc:
                boty.send_document(id, doc)
    except:
        boty.send_message(message.chat.id, 'error occured')

boty.polling()