from __future__ import annotations

import os

from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, filters

from furiabot.bot.handlers.menu import send_menu_handler
from furiabot.bot.handlers.news import get_news_handler
from furiabot.bot.handlers.nextgames import get_next_games_handler
from furiabot.bot.handlers.start import start_handler

# Load the environment variables from .env.
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


# Start the bot.
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN não encontrado no arquivo .env")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Adicionando o handler de mensagens gerais
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_menu_handler))

    # Add handlers.
    app.add_handler(start_handler())
    app.add_handler(get_news_handler())
    app.add_handler(get_next_games_handler())

    print("🤖 Bot rodando... Envie comandos no Telegram.")
    # Inicia o bot, ignorando mensagens pendentes.
    # Em bots críticos que não podem perder mensagens,
    # esse parâmetro não deve ser usado.
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
