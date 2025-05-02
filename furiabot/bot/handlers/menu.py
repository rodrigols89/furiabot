from __future__ import annotations

from telegram import Update
from telegram.ext import ContextTypes


# Função que responde com o menu de comandos
async def send_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    resposta = (
        "Olá, bem-vindo ao FuriaBot 🔥 Como posso ajudar você a acompanhar o time?\n\n"
        "Aqui estão os comandos disponíveis:\n\n"
        "/noticias - Veja as últimas notícias sobre a FURIA.\n"
        "/proximosjogos - Veja os próximos jogos da FURIA.\n"
    )
    await update.message.reply_text(resposta)
