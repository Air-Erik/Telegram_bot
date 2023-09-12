import logging
import os
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение значения токена из переменной окружения
token = os.getenv('TOKEN')

# Функция-обработчик сообщений
def reply_yes(update: Update, context):
    if update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text='да')

def main():
    # Создание объекта Bot
    bot = Bot(token=token)

    # Создание экземпляра Updater и передача объекта Bot
    updater = Updater(bot=bot, use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрация обработчика сообщений
    dispatcher.add_handler(MessageHandler(Filters.text, reply_yes))

    # Запуск бота
    updater.start_polling()

    # Остановка бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
