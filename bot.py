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
    cpp_strs = ("c++", "bjarne stroustrup", "c plus plus", "c with classes")
    java_strs = ("java", "java lambdas")
    oop_strs = ("opp", "poo", "programacao orientada a objetos")
    nice_strs = ("python", "haskell", "erlang", "c")
    
    if any(s in msg.lower() for s in js_strs):
        bot.sendMessage(chat_id, "JS sucks! Stop using it.")
    elif any(s in msg.lower() for s in cpp_strs):
        bot.sendMessage(chat_id, "C++ sucks! Stop using it.")     
    elif any(s in msg.lower() for s in oop_strs):
        bot.sendMessage(chat_id, "Such overrated concept, use functional paradigms!!!!!")
    elif any(s in msg.lower() for s in java_strs):
        bot.sendMessage(chat_id, "Continue to use that crap and you're out.")
    elif any(s in msg.lower() for s in nice_strs):
        bot.sendMessage(chat_id, "https://www.youtube.com/watch?v=ExsAwMTQwfI")

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

