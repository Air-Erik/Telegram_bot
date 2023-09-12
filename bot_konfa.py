from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update: Update, context) -> None:
    update.message.reply_text("Привет! Я бот, который сканирует сообщения в чате и отправляет эмодзи 🎰, если встречает слово 'Джекпот'.")

def scan_messages(update: Update, context) -> None:
    text = update.message.text
    if ("джекпот" or "Джекпт") in text.lower():
        update.message.chat.send_dice(emoji="🎰")
    if "кости" in text.lower():
        update.message.chat.send_dice(emoji="🎲")

def main() -> None:
    # Замените <YOUR_BOT_TOKEN> на токен вашего бота
    updater = Updater(token="5655609100:AAH-YHHoJZrCGlXUwKDeWAoR7_Z5Az61AD4", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), scan_messages))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
