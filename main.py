import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# جلب التوكن من متغيرات البيئة
BOT_TOKEN = os.getenv("TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ لم يتم العثور على توكن البوت في متغيرات البيئة!")

# إعدادات اللوجات
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# دالة التنبؤ (مكان النموذج لاحقاً)
async def predict(image_path):
    return "🐔 أتوقع أن هذه صورة دجاجة"

# التعامل مع الصور المستلمة
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    image_path = f"{photo.file_unique_id}.jpg"
    await file.download_to_drive(image_path)

    prediction = await predict(image_path)
    await update.message.reply_text(prediction)

# الدالة الرئيسية لتشغيل البوت
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("🤖 البوت يعمل الآن...")
    await app.run_polling()

# تشغيل البوت
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
