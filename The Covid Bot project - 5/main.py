from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import json
updater = Updater(token='5258340594:AAHbbKnwwI5MVcvGFNnFmZOK6h66VfIZAWg', use_context= True)
dispatcher = updater.dispatcher
updater.start_polling()
def summary (update, context):
    response = requests.get('https://api.covid19api.com/summary')
    print ('Hi')
    if response.status_code == 200:
        data = response.json()
        date = data['Date'][:10]
        answer = f"covid 2022 summary (As of {date}): \n"
        for attribute, value in data['Global'].items():
            if attribute not in ['NewConfirmed', 'NewDeaths', 'NewRecovered']:
             answer += 'total' + attribute [5::].lower()+":" +str(value) +"\n"
        context.bot.send_message(chat_id = update.effective_chat.id, text = answer)
    else: 
        context.bot.send_message(chat_id = update.effective_chat.id, text = "error, something went wrong")
covid_summary = CommandHandler('summary', summary)
dispatcher.add_handler(covid_summary)