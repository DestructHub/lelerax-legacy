import sys
import time
from random import randint
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
    hell_strs = ("satan", "diabo", "demonio", "inferno", "fogo", "hell")
    bom_strs = ("bom", "que bom", "kibon", "massa", "funciona", "funcionando", "funcionou", "rodar", "rodou", "compilar", "compilou")
    hue_strs = ("hue", "hu3", "br", "brasil", "brazil", "haha", "kkkk")

    stk_card = "CAADAQADfwAD5G3CCTY2lvkcjTKUAg"
    stk_monstro = "CAADAQAD3QAD5G3CCfzBqgbKrcVvAg"
    stk_delicia1 = "CAADAgADhwAD12I0BVT0buDrX9dLAg"
    stk_delicia2 = "CAADAgADcAAD12I0Bd-BteG_OrJCAg"
    stk_aham = "CAADAgADhAAD12I0BVoDZEJxg6_KAg"
    stk_fodase = "CAADAQADPQADarEOBvuO0Zx96BjxAg"
    stk_queromorre = "CAADAQADRQADarEOBrMse4T-xV6SAg"
    stk_satan = "CAADAQADtQADarEOBiaPApuCmIsjAg"
    stk_hue = "CAADAQADxwAD5G3CCXbWeLF4Nd78Ag"
    stk_kibon = "CAADAQADzwAD5G3CCdroYc38v2yHAg"
    stk_flip = "CAADAQADyQAD5G3CCaRAcC_I79baAg"
    
    m = msg.lower().split()
    sticker = ""
    res = ""

    if any(s in m for s in js_strs):
        res = "JS uma porra!\nJS e` tao cancer que comeca com J, de Javascript"
        sticker = stk_fodase if randint(0,1) else stk_queromorre 
    elif any(s in m for s in cpp_strs):
        res = "C++ sucks! Stop using it." 
    elif any(s in m for s in oop_strs):
        res = "Such overrated concept, use functional paradigms!!!!!"
    elif any(s in m for s in java_strs):
        res = "Continue to use that crap and you're out."
    elif any(s in m for s in nice_strs):
        res = "delicia"
        sticker = stk_delicia1 if randint(0,1) else stk_delicia2
    elif "monstro" in msg.lower():
        sticker = stk_monstro
    elif any(s in m for s in hell_strs):
        sticker = stk_satan
    elif any(s in m for s in bom_strs):
        bot.sendSticker(chat_id, stk_card)
        sticker = stk_kibon if randint(0,1) else stk_flip
    elif any(s in msg.lower() for s in hue_strs):
        res = "AHUHAAUUhuahua"
        sticker = stk_hue
    elif any(s in msg.lower() for s in manoel_strs) and "voltar" in msg.lower():
        res = "to aqui carai"
    elif any(s in msg.lower() for s in manoel_strs):
        res = "oi"

    if res:
        bot.sendMessage(chat_id, res, reply_to_message_id=id)
    
    if sticker:
        bot.sendSticker(chat_id, sticker)

TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

