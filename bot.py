import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to HS Training Bot!")

def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN not found!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    PORT = int(os.environ.get("PORT", 8080))
    RAILWAY_URL = os.environ.get("RAILWAY_PUBLIC_DOMAIN", "localhost")
    webhook_url = f"https://{RAILWAY_URL}/{BOT_TOKEN}"
    
    logger.info(f"Starting webhook on port {PORT}")
    
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=webhook_url
    )

if __name__ == "__main__":
    main()
