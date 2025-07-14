import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7893647778:AAHtXBfyE7bkhd0e3HfSCqZlrNyW_dHrlvE"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def predict(image_path):
    return "أتوقع أن هذه صورة دجاجة 🐔"

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    image_path = f"{photo.file_unique_id}.jpg"
    await file.download_to_drive(image_path)

    prediction = await predict(image_path)
    await update.message.reply_text(prediction)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())