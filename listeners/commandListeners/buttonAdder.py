from listeners.commandListener import CommandListener
from telegram import Update
from telegram.ext import ContextTypes


class ButtonAdder(CommandListener):

    def __init__(self):
        super().__init__("button")
    
    async def do(self, update: Update, context:ContextTypes.DEFAULT_TYPE):
        button_name = ""
        if context.args:
            for name in context.args:
                button_name = button_name + name + " "
            button_name = button_name[:-1]
            await self.bot.add_keyboard_button(update.effective_chat.id, button_text = button_name, one_time_use=True)
        else:
            await self.bot.remove_keyboard_buttons(update.effective_chat.id, "Removing buttons")
