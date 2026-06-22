from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ضع الـ Token هنا (من BotFather)
TOKEN = "8999164629:AAHJWrc0txfUjqmWBRFKAiBKRd4WniFFi14"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بيك! 👋 البوت شغال!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت شغال...")
    app.run_polling()

if __name__ == "__main__":
    main()
