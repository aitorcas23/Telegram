from listeners.commandListener import CommandListener
from telegram import Update


class ButtonRemover(CommandListener):

    def __init__(self):
        super().__init__("remove_buttons")
    
    async def do(self, update: Update, _):
        await self.bot.remove_all_keyboard_buttons(update.effective_chat.id, "Removing buttons")
