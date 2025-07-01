import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ضع التوكنات هنا مباشرة
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxx"
TELEGRAM_BOT_TOKEN = "8066444333:AAG70_nQXaBgb-Fmhw_gBDUbL8tJ8OywdsQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا! أرسل لي أي سؤال، وأنا برد عليك باستخدام GPT 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response['choices'][0]['message']['content']
    except Exception as e:
        bot_reply = f"حصل خطأ: {e}"
    await update.message.reply_text(bot_reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
