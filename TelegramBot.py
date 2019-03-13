import telepot
import sys
import time
from telepot.loop import MessageLoop
import configparser as cfg

def grab_config(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    configs = [parser.get('creds', 'token'), parser.get('creds', 'response'), parser.get('creds', 'command')]
    return (configs)

def handle(msg):
    
    token, response, command = grab_config("config.cfg")
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text' and msg["text"] == command:
        bot.sendMessage(chat_id, response)

token = grab_config("config.cfg")[0]
bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread()

while (1):
    time.sleep(10)
