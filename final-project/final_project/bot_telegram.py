TOKEN = '7431182722:AAGMQ2zsgzPnG1e-bAn2JGwA7UWLsDELz9Q'

# !/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
        format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", level = logging.INFO
        )
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
            reply_markup = ForceReply(selective = True),
            )
    await update.message.reply_text("Bienvenido al bot de notificaciones de tareas desarrolladora por ori, "
                                    "para comenzar escribe /id para obtener tu id de telegram")


async def id_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /id is issued."""
    user = update.effective_user
    await update.message.reply_text(f"Tu id de telegram es: {user.id} 👌")


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("id", id_command))
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates = Update.ALL_TYPES)


if __name__=="__main__":
    main()