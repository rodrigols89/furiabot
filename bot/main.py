from __future__ import annotations

import os

from dotenv import load_dotenv
from handlers.menu import send_menu_handler
from handlers.news import get_news_handler
from handlers.nextgames import get_next_games_handler
from telegram.ext import ApplicationBuilder, MessageHandler, filters

# Load the environment variables from .env.
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


# Start the bot.
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN não encontrado no arquivo .env")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Add handlers.
    app.add_handler(get_news_handler())
    app.add_handler(get_next_games_handler())

    # Adicionando o handler de mensagens gerais
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_menu_handler))

    print("🤖 Bot rodando... Envie comandos no Telegram.")
    app.run_polling()


if __name__ == "__main__":
    main()
