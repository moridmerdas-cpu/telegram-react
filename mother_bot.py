from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import CHILD_BOTS, OWNER_ID

def start(update, context):
    user_id = update.effective_user.id
    if user_id != OWNER_ID:
        update.message.reply_text("فقط مدیر می‌تونه از این ربات استفاده کنه ❌")
        return

    buttons = [
        [InlineKeyboardButton(f"ربات فرعی {i+1}", url=f"https://t.me/{username}")]
        for i, username in enumerate(CHILD_BOTS)
    ]

    markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("ربات‌های فرعی:", reply_markup=markup)
