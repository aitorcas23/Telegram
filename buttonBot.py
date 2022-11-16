from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

class ButtonBot:

    active_buttons:list

    def __init__(self):
        self.active_buttons = []

    async def add_keyboard_button(self, to, message_text:str = "Adding button", button_text:str = "Button", ask_number:bool = False, one_time_use = False):
        if not self.active_buttons:
            self.active_buttons.insert(0,[KeyboardButton("/remove_buttons")])
        self.active_buttons.append([KeyboardButton(button_text, ask_number)])
        if one_time_use:
            self.get_remove_button_by_name().add_listen_to(button_text)
        await self.__refresh_buttons(to, message_text)

    async def __refresh_buttons(self, to, message_text:str = "Refreshing buttons"):
        botones = []
        for rep in self.active_buttons:
            botones.insert(0,rep)
        reply = ReplyKeyboardMarkup(botones, resize_keyboard=True, one_time_keyboard=False)
        if not self.active_buttons or (len(self.active_buttons) == 1 and self.active_buttons[0][0].text == "/remove_buttons"):
            await self.remove_all_keyboard_buttons(to,message_text)
        else:
            await self.bot.bot.send_message(chat_id=to, text=message_text, reply_markup=reply)
    
    async def remove_all_keyboard_buttons(self, to, message_text:str = "Removing all buttons"):
        self.active_buttons = []
        await self.bot.bot.send_message(chat_id=to, text=message_text, reply_markup=ReplyKeyboardRemove(True))
        self.get_remove_button_by_name().listen_to.clear()

    async def remove_keyboard_button(self, to, button_name:str, message_text:str = None):
        for button in self.active_buttons:
            if button[0].text == button_name:
                self.active_buttons.remove(button)
                if message_text != None:
                    await self.__refresh_buttons(to, message_text)
                else:
                    await self.__refresh_buttons(to)