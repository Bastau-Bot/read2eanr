import telebot

bot = telebot.TeleBot('7581777238:AAEjcWht1cpJ-NEf0lW9netGhTcS9NVmZDc')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Салем, {message.from_user.first_name} саған шынымен кітап оқу ұнайды ма әлде ақша үшін келдің бе? Егер саған шынымен кітап оқу ұнаса, оқығанда шын ниетіңмен оқысаң кеттік.'
    bot.send_message(message.chat.id, mess)



bot.polling(none_stop=True)





