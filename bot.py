import os, logging, random

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Load .env variables...
import dotenv; dotenv.load_dotenv()

BOT_USERNAME = 'AURA_SK_BOT'
GHOSTS_DB = os.getenv("GHOSTS_DB")

def start(update: Update):
    keyboard = [[InlineKeyboardButton("Join Guild", callback_data='join')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to AURA SK! Press Join Guild to continue.', reply_markup=reply_markup)

def button(update: Update):
