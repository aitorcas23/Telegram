import logging, datetime
from alerta import Alerta
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import filters, ContextTypes, CommandHandler, MessageHandler, InlineQueryHandler, CallbackContext, CallbackQueryHandler
from telegram.ext import ApplicationBuilder

dataFile = "src/telegram/data.txt"

dataBase = [{
    "name":"Aitor",
    "surname":"Castaño",
    "id":5352156188
}]

opened_buttons:bool = False

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.effective_chat.id)
    #Crear el boton para pedir el numero de telefono
    botones = [[KeyboardButton("Entregar número de telefono", True)],[KeyboardButton("Cancel")]]
    #botonInLine = [[InlineKeyboardButton('Button: Print Clicked', callback_data=1)]]
    #Crear el teclado en el que va a meter el boton
    reply = ReplyKeyboardMarkup(botones, resize_keyboard=True, one_time_keyboard=False)
    #replyInLine= InlineKeyboardMarkup(botonInLine)
    #Enviar el boton
    opened_buttons = True
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Necesitamos su número de telefono", reply_markup=reply)
    
    message = ""
    #Identificar a la parsona
    for person in dataBase:
        id = update.effective_user.id
        if(id == person["id"]):
            message = "Hola " + person["name"]
    if message == "":
        message = "Quien eres?"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title= query.upper(),
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

async def getPhoneNumber(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #recibir numero de telefono
    #if opened_buttons:
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.contact.phone_number, reply_markup = ReplyKeyboardRemove(True))
        #opened_buttons = False
    #await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def alertaCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    alerta = Alerta("belmek001_m1", "alarm066", 3, "Presion excesiva en el sistema", datetime.datetime(2022,11,11,12,23,32,261), 7.9, 7.5)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=alerta.toString())

async def callbackHandler(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="callback")

async def cancelHandler(update: Update, context: CallbackContext):
    #if opened_buttons:
    if update.effective_message.text == 'Cancel':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Cancelled", reply_markup = ReplyKeyboardRemove(True))
    #opened_buttons = False

def writeInFile(s:str, fileName:str):
    data = open(fileName, "a+")
    data.write(s)
    data.close()

class main:
    if __name__ == '__main__':
        opened_buttons = False
        application = ApplicationBuilder().token('5424527179:AAGpRg5HtvExfDuUK-j1suOiGfpW9aXT-Is').build()
        
        start_handler = CommandHandler('start', start)
        #echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
        #caps_handler = CommandHandler('caps', caps)
        alerta_handler = CommandHandler('alerta', alertaCommand)
        #inline_caps_handler = InlineQueryHandler(inline_caps)
        phone_number_handler = MessageHandler(filters.CONTACT, getPhoneNumber)
        cancel_handler = MessageHandler(filters.TEXT, cancelHandler)
        unknown_handler = MessageHandler(filters.COMMAND, unknown)

        application.add_handler(start_handler)
        #application.add_handler(echo_handler)
        #application.add_handler(caps_handler)
        application.add_handler(alerta_handler)
        #application.add_handler(inline_caps_handler)
        application.add_handler(phone_number_handler)
        #application.add_handler(CallbackQueryHandler(callbackHandler))
        application.add_handler(cancel_handler)
        application.add_handler(unknown_handler)
        
        application.run_polling()