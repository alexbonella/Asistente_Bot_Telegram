# Asistente_Bot_Telegram

Bot que envía resultados de loteria 


# Presencia Online 

[![LinkedIn](https://img.shields.io/badge/-Go%20To%20LinkedIn-3b5998)](https://www.linkedin.com/in/alexanderbolano)
[![Stackoverflow](https://img.shields.io/badge/-Stackoverflow-ff7c55)](https://stackoverflow.com/story/alexbonella)
[![Twitter](https://img.shields.io/badge/-@Alex_bonella-1DA1F2)](https://twitter.com/Alex_bonella)

# Descripción 

Este repositorio contiene lo necesario para enviar por medio de un Bot de Telegram todos los resultados de loteria jugados el día anterior en Colombia .

# Paso a Paso  

1. Crear un Bot de Telegram de manera gratuita 

    * Ingresar a [Telegram_Web](https://web.telegram.org)
    * Buscar el **`BotFather`** dentro de Telegram
    * Ir a la pestaña **`newbot`** y seguir las intrucciones para configuración del nombre y usuario.
    * Extraer Bot_Token y copiarlo en *`credentials.py`*
    
2.  Extrer Bot_Chat_ID 

    * Ir a la ulr **`https://api.telegram.org/bot<Your_Token_Here>/getUpdates`** reemplazando *`<Your_Token_Here>`* por el que obtuviste en el paso anterior y copiarlo en *`credentials.py`* . 
  
4. Ejecutar el Script **`bot_tele.py`**

6. Observamos nuestros resultados en Telegram 


![loterias_telegram](https://user-images.githubusercontent.com/45697319/110657994-4ef64180-818f-11eb-8ebe-65b6a7164625.png)



