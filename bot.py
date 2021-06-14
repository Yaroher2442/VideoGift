import telebot
import time
from api_wrk import get_jpg

bot = telebot.TeleBot('1809118979:AAEYUk70tjcSsBytOz6U8ofODm9LlCxHdZA')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     "Привет! Я perfect_gift_bot, и я помогу тебе сделать идеальное видеопоздравление!")
    time.sleep(1)
    bot.send_message(message.chat.id, "Просто вставь сюда текст поздравления!")


@bot.message_handler(content_types=['text'])
def send_message(message):
    bot.send_message(message.chat.id, "Видео уже готовится!")
    get_jpg(message.text)


@bot.message_handler(
    content_types=["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                   "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                   "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                   "migrate_from_chat_id", "pinned_message"])
def send_message(message):
    bot.send_message(message.chat.id, "Это не подходит, введите текст")


bot.polling()