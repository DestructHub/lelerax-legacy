import sys
import time
import telepot

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        checkMsg(chat_id, msg['text'], msg['message_id'])

def checkMsg(chat_id, msg, id):
    js_strs = ("js", "javascript", "ecma script", "ecma", "ecma6")
    cpp_strs = ("c++", "bjarne stroustrup", "c plus plus", "c with classes", "cpp")
    java_strs = ("java", "java lambdas")
    oop_strs = ("opp", "poo", "programacao orientada a objetos")
    nice_strs = ("python", "haskell", "erlang", "c", "lua", "brain", "lisp", "garnet")
    manoel_strs = ("manoel", "@lerax", "@lelerax")
    
    res = ""
    m = msg.lower().split()

    if any(s in m for s in js_strs):
        res = "JS uma porra!\nJS e` tao cancer que comeca com J, de Javascript"
    elif any(s in m for s in cpp_strs):
        res = "C++ sucks! Stop using it." 
    elif any(s in m for s in oop_strs):
        res = "Such overrated concept, use functional paradigms!!!!!"
    elif any(s in m for s in java_strs):
        res = "Continue to use that crap and you're out."
    elif any(s in m for s in nice_strs):
        res = "delicia"
    elif any(s in m for s in manoel_strs) and "voltar" in msg.lower():
        res = "to aqui carai"
    elif any(s in m for s in manoel_strs):
        res = "oi"
    else:
        return

    bot.sendMessage(chat_id, res, reply_to_message_id=id)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

