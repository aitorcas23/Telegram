from listeners.commandListeners.buttonAdder import ButtonAdder
from listeners.commandListeners.chatCodeGetter import ChatCodeGetter
from listeners.commandListeners.buttonRemover import ButtonRemover
from listeners.messageListeners.removeButtonByName import RemoveButtonByName
from telegramBot import TelegramBot

if __name__ == '__main__':


    aitorcas_bot = TelegramBot('5604209283:AAF8uw9B3XMwc6maxN6PYfbQAUAp3NciceQ')

    aitorcas_bot.add_listeners(ChatCodeGetter(), ButtonAdder(), ButtonRemover(), RemoveButtonByName())
    aitorcas_bot.start()
    
    