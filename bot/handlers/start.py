from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

# Função para responder ao comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Olá, bem-vindo ao FuriaBot 🔥 Como posso ajudar você a acompanhar o time?")

# Função que retorna o handler para o comando /start
def get_start_handler() -> CommandHandler:
    return CommandHandler('start', start)
