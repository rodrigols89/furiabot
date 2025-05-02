from __future__ import annotations

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes


# Função principal do handler /proximosjogos
async def nextgames(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    texto = (
        "🎯 *Próximos Jogos da FURIA:*\n\n"
        "Escolha um dos jogos abaixo para ver os próximos confrontos do time da Furia no respectivo jogo na Liquipedia (procure na página por 'Upcoming Tournaments'):"
    )

    # Criação dos botões
    botoes = [
        [
            InlineKeyboardButton(
                "🔫 Counter Strike", url="https://liquipedia.net/counterstrike/FURIA"
            ),
        ],
        [
            InlineKeyboardButton(
                "🧙 League of Legends",
                url="https://liquipedia.net/leagueoflegends/FURIA",
            ),
        ],
        [
            InlineKeyboardButton(
                "🎯 Valorant", url="https://liquipedia.net/valorant/FURIA"
            ),
        ],
        [
            InlineKeyboardButton("⚔️ Dota 2", url="https://liquipedia.net/dota2/FURIA"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(botoes)
    await update.message.reply_text(
        texto, reply_markup=reply_markup, parse_mode="Markdown"
    )


# Função para registrar o handler no bot
def get_next_games_handler() -> CommandHandler:
    return CommandHandler("proximosjogos", nextgames)
