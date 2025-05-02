import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers.start import get_start_handler
from handlers.noticias import get_noticias_handler

# Carrega o .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Inicia o bot
def main():
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN não encontrado no arquivo .env")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Adiciona os handlers para /start e /noticias
    app.add_handler(get_start_handler())
    app.add_handler(get_noticias_handler())

    print("🤖 Bot rodando... Envie /start ou /noticias no Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()
