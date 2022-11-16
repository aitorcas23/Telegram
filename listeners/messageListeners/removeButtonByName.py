from listeners.messageListener import MessageListener
from telegram import Update
from telegram.ext import filters

class RemoveButtonByName(MessageListener):
    from buttonBot import ButtonBot
    def __init__(self):
        super().__init__(filters.TEXT)
        self.listen_to = []

    def add_listen_to(self, listen_to:str):
        self.listen_to.append(listen_to)
        print(len(self.listen_to))
    
    def setBot(self, bot:ButtonBot):
        self.bot = bot

    async def do(self, update: Update, _):
        if update.effective_message.text in self.listen_to:
            self.listen_to.remove(update.effective_message.text)
            await self.bot.remove_keyboard_button(update.effective_chat.id, update.effective_message.text)
            print(len(self.listen_to))
