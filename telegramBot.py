from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from listeners import listener, commandListener, messageListener
from buttonBot import ButtonBot

class TelegramBot(ButtonBot):

    def __init__(self, token):
        super().__init__()
        self.token = token
        self.users = []
        self.active_listeners = []
        self.bot = ApplicationBuilder().token(token).build()

    async def send(self, to, message):
        await self.bot.send_message(chat_id = to, text=message)
    
    def add_listener(self, listener:listener.Listener):
        listener.set_bot(self)
        self.active_listeners.append(listener)
        if isinstance(listener, commandListener.CommandListener):
            self.bot.add_handler(CommandHandler(listener.filter, listener.do))
        elif isinstance(listener, messageListener.MessageListener):
            self.bot.add_handler(MessageHandler(listener.filter, listener.do))
        print(len(self.active_listeners))
    
    def add_listeners(self, *listeners:listener.Listener):
        for l in listeners:
            l.set_bot(self)
            self.active_listeners.append(l)
            if isinstance(l, commandListener.CommandListener):
                self.bot.add_handler(CommandHandler(l.filter, l.do))
            elif isinstance(l, messageListener.MessageListener):
                self.bot.add_handler(MessageHandler(l.filter, l.do))

    def remove_listeners(self, *listeners:listener.Listener):
        for l in listeners:
            self.bot.remove_handler(l)

    def start(self):
        self.bot.run_polling()

    def get_remove_button_by_name(self):
        from listeners.messageListeners.removeButtonByName import RemoveButtonByName
        for listener in self.active_listeners:
            if isinstance(listener, RemoveButtonByName):
                return listener
        return None
