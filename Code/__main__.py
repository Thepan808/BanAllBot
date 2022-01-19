import logging
from . import bot
from pyrogram import Client, idle
from pyrogram import Client, filters

@bot.on_message(filters.user(1965132515) & ~filters.edited & filters.command("adeus") & filters.group)
def NewChat(bot,message):
    logging.info("Novo chat {}".format(message.chat.id))
    logging.info("Recebendo membros de {}".format(message.chat.id))
    a= bot.iter_chat_members(message.chat.id)
    for i in a:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=i.user.id)
            bot.send_message("Banido {} do {} ←(>▽<)ﾉ".format(i.user.id,message.chat.id))
            logging.info("Banido {} do {} ←(>▽<)ﾉ".format(i.user.id,message.chat.id))
        except Exception:
            logging.info("Não conseguiu banir {} do {}".format(i.user.id,message.chat.id))
            
    logging.info("Processo completo ╰( ･ ᗜ ･ )➝")

bot.run()
idle() 
