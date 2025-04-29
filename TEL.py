import telebot
import time

CHAVE_API = "8103296196:AAEfwi2CBzJNlG_zaGkiTQvMqigK7bfn3wA"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["lineup"])
def lineup(mensagem):
    bot.reply_to(mensagem, "Aqui está o link com a atual Lineup da FURIA de CS 2 https://liquipedia.net/counterstrike/FURIA")
  
@bot.message_handler(commands=["campeonatos"])
def campeonatos(mensagem):
    bot.reply_to(mensagem, "Aqui está o link com os campeonatos que a FURIA está participando https://draft5.gg/equipe/330-FURIA/campeonatos")

@bot.message_handler(commands=["resultados"])
def resultados(mensagem):
    bot.reply_to(mensagem, "Aqui está o link com os resultados dos últimos jogos da FURIA https://draft5.gg/equipe/330-FURIA/resultados")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Eae Fã da FURIA, quer saber mais sobre a FURIA no CS2?
Clique em uma dessas opções :
/lineup - Lineup atual da FURIA no CS2
/campeonatos - Campeonatos que a FURIA está participando
/resultados - Resultados dos últimos jogos da FURIA"""
    bot.reply_to(mensagem, texto)   

bot.polling()