import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters

load_dotenv()

TOKEN = os.getenv("TOKEN")

def add_reaction(update, context):
    message = update.effective_message
    message.reply_text("🤡")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    reaction_handler = MessageHandler(Filters.chat_type.groups, add_reaction)
    dispatcher.add_handler(reaction_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
