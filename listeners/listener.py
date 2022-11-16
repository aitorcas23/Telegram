import abc
from telegram import Update
from telegram.ext import CallbackContext


class Listener:

    def __init__(self, filter):
        from telegramBot import TelegramBot
        self.filter = filter
        self.bot:TelegramBot

    def set_bot(self, bot):
        self.bot = bot

    @abc.abstractmethod
    async def do(update: Update, context: CallbackContext):
        pass