from telegram.ext import CommandHandler
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

# Função para o comando /noticias
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = "📰 Últimas atualizações sobre a FURIA:"

    # Criar os botões
    keyboard = [
        [InlineKeyboardButton("🐦 X (Twitter)", url="https://x.com/FURIA")],
        [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/furiagg/")],
        [InlineKeyboardButton("💼 Vagas na FURIA", url="https://99jobs.com/furia/jobs")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(mensagem, reply_markup=reply_markup)

# Função que retorna o handler para o comando /noticias
def get_noticias_handler() -> CommandHandler:
    return CommandHandler('noticias', noticias)
