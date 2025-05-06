from __future__ import annotations

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes


# Função principal do handler /proximosjogos
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = (
        "Olá, bem-vindo ao FuriaBot 🔥 Como posso ajudar você a acompanhar o time?\n\n"
        "Aqui estão os comandos disponíveis:\n\n"
        "/noticias - Veja as últimas notícias sobre a FURIA.\n"
        "/proximosjogos - Veja os próximos jogos da FURIA.\n"
    )
    await update.message.reply_text(msg)


# Função para registrar o handler no bot
def start_handler() -> CommandHandler:
    return CommandHandler("start", start)
