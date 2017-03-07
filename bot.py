import sys
import time
import telepot

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type, chat_type, chat_id)

    if content_type == 'text':
        checkMsg(chat_id, msg['text'])

def checkMsg(chat_id, msg):
    js_strs = ("js", "javascript")
    if any(s in msg.lower() for s in js_strs):
        bot.sendMessage(chat_id, "JS sucks!")
        bot.sendSticker(chat_id, "CAADAQAD3QAD5G3CCfzBqgbKrcVvAg") 

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

