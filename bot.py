from telegram.ext import MessageHandler, filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler
from telegram import _update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
BOT_TOKEN = "7946811507:AAFncZnR8nDHMkt9HwsrQ61HntgKhQ5Qg34"



async def start(update: _update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("📝 Send Feedback")],
        [KeyboardButton("❓ Ask a Question")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! Choose an option below:", reply_markup=reply_markup)


async def help_command(update:_update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can use /start to talk to me!😍")


# echo handler function

# async def echo(update: _update, context:ContextTypes.DEFAULT_TYPE):
#     user_text = update.message.text
#     await update.message.reply_text(f"You said: {user_text}")


# async def input_handler(update:_update, context:ContextTypes.DEFAULT_TYPE):
#     user_input = update.message.text
#
#     if user_input == "📝 Get Info":
#         await update.message.reply_text("I am telegram bot created by Musab. 🚀")
#     elif user_input == "📞 Contact":
#         await update.message.reply_text("You can contact my creator at @ramiso0")
#     # elif user_input == "📽️ Menu":
#     else:
#         await update.message.reply_text(f"You said: {user_input}")


async def menu(update:_update, context: ContextTypes.DEFAULT_TYPE):
    inline_button = [
        [InlineKeyboardButton("📶 Join Channel", url="https://t.me/ramisoTech")],
        [InlineKeyboardButton("📝 Bot info", callback_data="bot_info")]
    ]
    reply_markup = InlineKeyboardMarkup(inline_button)
    await update.message.reply_text("Choose an action: ", reply_markup = reply_markup)


async def handle_callback(update:_update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "bot_info":
        await query.message.reply_text("I'm a smart bot created by Musab 🤖✨")


YOUR_TELEGRAM_ID = 5072548007  # Replace this with your actual ID

async def input_handler_feedback(update: _update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    user = update.message.from_user

    if user_input == "📝 Send Feedback":
        await update.message.reply_text("Please type your feedback below:")
        context.user_data['expecting_feedback'] = True

    elif context.user_data.get('expecting_feedback'):
        feedback = update.message.text

        # Send feedback to your personal Telegram
        await context.bot.send_message(
            chat_id=5072548007,
            text=f"📝 New Feedback from {user.full_name} (@{user.username}):\n\n{feedback}"
        )

        await update.message.reply_text("Thanks for your feedback! 🙏")
        context.user_data['expecting_feedback'] = False

    # Add similar handling for question if needed

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CallbackQueryHandler(handle_callback))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, input_handler_feedback))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, input_handler))

print("Starting bot...")
# app.run_polling()

app.run_polling()

