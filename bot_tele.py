

import requests
import credentials
import datetime
from loterias_ws import df_file

def telegram_bot_sendtext(bot_message):

    bot_token  = credentials.bot_token

    bot_chatID = credentials.bot_chatID

    enviar_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(enviar_text)

    return response.json()

Fecha=str(datetime.datetime.now().day)+'/'+ str(datetime.datetime.now().month)+'/'+str(datetime.datetime.now().year)


test = telegram_bot_sendtext(f" ¡ATENCION! Estos son todos los resultados de loterias del día {str(Fecha)}: \n\n   {str(df_file)}\n" ) 
