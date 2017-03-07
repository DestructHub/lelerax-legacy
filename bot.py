import sys
import time
import telepot

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type, chat_type, chat_id)

    if content_type == 'text':
        checkMsg(chat_id, msg['text'])

def checkMsg(chat_id, msg):
    js_strs = ("js", "javascript", "ecma script", "ecma", "ecma6")
    cpp_strs = ("c++", "Bjarne Stroustrup", "c plus plus", "c with classes")
    oop_strs = ("OOP", "POO", "programacao orientada a objetos")

    if any(s in msg.lower() for s in js_strs):
        bot.sendMessage(chat_id, "JS sucks!")
        bot.sendSticker(chat_id, "CAADAQAD3QAD5G3CCfzBqgbKrcVvAg") 
    
    if any(s in msg.lower() for s in cpp_strs):
        bot.sendMessage(chat_id, "C++ sucks! Stop using it.")
           
    if any(s in msg.lower() for s in oop_strs):
        bot.sendMessage(chat_id, "Such overrated concept, use functional paradigms!!!!!")

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

