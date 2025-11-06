from telegram.ext import Updater, MessageHandler, Filters
from telegram import Update
from config import CHILD_TOKENS

REACTIONS = ["👍", "🔥", "😂", "❤️"]

def react(update: Update, context):
    try:
        for emoji in REACTIONS:
            context.bot.send_reaction(chat_id=update.effective_chat.id, message_id=update.message.message_id, emoji=emoji)
    except Exception as e:
        print("Error:", e)

def main(token):
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, react))
    updater.start_polling()
    print(f"Started {token}")
    updater.idle()

if name == "main":
    for token in CHILD_TOKENS:
        main(token)
