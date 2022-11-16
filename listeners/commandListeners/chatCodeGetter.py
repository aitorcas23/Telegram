from telegram import Update
from listeners.commandListener import CommandListener

class ChatCodeGetter(CommandListener):

    def __init__(self):
        super().__init__("start")

    async def do(self, update: Update, _):
        self.bot.users.append({'name':update.effective_user.full_name,'kode':update.effective_chat.id})
        print(update.effective_user.full_name + str(update.effective_chat.id))