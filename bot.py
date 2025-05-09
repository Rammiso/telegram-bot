from telegram.ext import MessageHandler, filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram import Update

BOT_TOKEN = "7946811507:AAFncZnR8nDHMkt9HwsrQ61HntgKhQ5Qg34"
MY_TELEGRAM_ID = 5072548007


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("📝 Send Feedback")],
        [KeyboardButton("❓ Ask a Question")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! Choose an option below:", reply_markup=reply_markup)


async def input_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    user = update.message.from_user

    # Start feedback flow
    if user_input == "📝 Send Feedback":
        await update.message.reply_text("Please type your feedback below:")
        context.user_data['expecting_feedback'] = True
        context.user_data['expecting_question'] = False

    # Start question flow
    elif user_input == "❓ Ask a Question":
        await update.message.reply_text("Please type your question below:")
        context.user_data['expecting_question'] = True
        context.user_data['expecting_feedback'] = False

    # Handle actual feedback
    elif context.user_data.get('expecting_feedback'):
        await context.bot.send_message(
            chat_id=5072548007,
            text=f"📝 New Feedback from {user.full_name} (@{user.username}):\n\n{user_input}"
        )
        await update.message.reply_text("Thanks for your feedback! 🙏")
        context.user_data['expecting_feedback'] = False

    # Handle actual question
    elif context.user_data.get('expecting_question'):
        await context.bot.send_message(
            chat_id=5072548007,
            text=f"❓ New Question from {user.full_name} (@{user.username}):\n\n{user_input}"
        )
        await update.message.reply_text("Thanks for your question! 🙏")
        context.user_data['expecting_question'] = False


app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, input_handler))

print("Bot is running...")
app.run_polling()

