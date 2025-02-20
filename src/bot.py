import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from services.exchange_rate import get_baht_to_ruble, get_usdt_to_baht

token = os.getenv("TELEGRAM_BOT_TOKEN")
if not token:
    raise ValueError("Переменная окружения TELEGRAM_BOT_TOKEN не установлена.")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Напишите "курс", чтобы получить актуальный курс.')

async def get_exchange_rates(update: Update, context: CallbackContext) -> None:
    ruble_rate = get_baht_to_ruble()
    usdt_rate = get_usdt_to_baht()
    await update.message.reply_text(f'Курс бата к рублю: {ruble_rate}\nКурс USDT к бату: {usdt_rate}')

async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    if text == "курс":
        await get_exchange_rates(update, context)

def main() -> None:
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()