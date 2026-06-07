import telebot
import random
import os
print(os.listdir('images'))

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Используй команду /MS или /Alfedov, чтобы получить мем!")

@bot.message_handler(commands=['Alfedov'])
def send_mem(message):
    with open('image/imageM1.png', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['MS'])
def send_mem(message):
    img_name = random.choice(os.listdir('image'))  # Случайным образом выбираем изображение
    with open(f'image/{img_name}', 'rb') as f:
        # Отправляем фото, выбранное случайным образом
        bot.send_photo(message.chat.id, f)



bot.polling()
