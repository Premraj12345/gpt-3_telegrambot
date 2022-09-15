from telegram.ext.updater import Updater 
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext 
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters 
import openai

api_key = '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'
openai.api_key = api_key

updater = Updater('5383451954:AAGx7pk-duETmTo-nH7NyEyXaLjqwkA0VoQ', use_context=True) 


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir") 

def unknown(update: Update, context: CallbackContext):
    msg = update.message.text
    response = openai.Completion.create(model="text-davinci-002",prompt= msg,temperature=0.7,max_tokens=256,top_p=1,frequency_penalty=0,presence_penalty=0)
    resp = response['choices'][0]['text']
    update.message.reply_text(resp) 

 
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
  
updater.start_polling()