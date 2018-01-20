import sys
import time
import os
from random import randint
import telepot

UAPDA = -1001096359543  # UAPDA chat id, where lelerax born
TOKEN = sys.argv[1]  # get token from command-line
bot = telepot.Bot(TOKEN)
REACT_FACTOR = 10  # probability between of react: from 0 to 100 (max reaction)
DEBUG = os.environ.get('DEBUG')


def react():
    return randint(1, 100//REACT_FACTOR) == 1


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if DEBUG:
            print(f"Log = cont: {content_type!r} - chat_type: {chat_type!r} - chat_id: {chat_id!r}")
            print(f"Msg = {msg['text']!r}")
        bot_engine(chat_id, msg['text'], msg['message_id'])


def bot_engine(chat_id, msg, message_id):
    if msg.lower().startswith("/uapda"):
        bot.sendMessage(UAPDA, msg.strip("/uapda"))
    else:
        bot_answers(chat_id, msg, message_id)


def bot_answers(chat_id, msg, message_id):
    js_strs = ("js", "javascript", "ecma script", "ecma", "ecma6")
    cpp_strs = ("c++", "bjarne stroustrup", "c plus plus", "c with classes",
                "cpp")
    java_strs = ("java", "java lambdas")
    oop_strs = ("opp", "poo", "programacao orientada a objetos")
    nice_strs = ("python", "haskell", "erlang", "c", "lua", "brain", "lisp",
                 "garnet")
    manoel_strs = ("manoel", "@lerax", "@lelerax", "lerax")
    hell_strs = ("satan", "diabo", "demonio", "inferno", "fogo", "hell")
    bom_strs = ("bom", "que bom", "kibon", "massa", "funciona", "funcionando",
                "funcionou", "rodar", "rodou", "compilar", "compilou")
    hue_strs = ("hue", "hu3", "haha", "kkkk")

    stk_card = "CAADAQADfwAD5G3CCTY2lvkcjTKUAg"
    stk_monstro = "CAADAQAD3QAD5G3CCfzBqgbKrcVvAg"
    stk_delicia1 = "CAADAgADhwAD12I0BVT0buDrX9dLAg"
    stk_delicia2 = "CAADAgADcAAD12I0Bd-BteG_OrJCAg"
    stk_fodase = "CAADAQADPQADarEOBvuO0Zx96BjxAg"
    stk_queromorre = "CAADAQADRQADarEOBrMse4T-xV6SAg"
    stk_satan = "CAADAQADtQADarEOBiaPApuCmIsjAg"
    stk_hue = "CAADAQADxwAD5G3CCXbWeLF4Nd78Ag"
    stk_kibon = "CAADAQADzwAD5G3CCdroYc38v2yHAg"
    stk_flip = "CAADAQADyQAD5G3CCaRAcC_I79baAg"

    msg_norm = msg.lower()
    m = msg_norm.split()
    sticker = ""
    res = ""
    stk_bool = react()

    if any(s in m for s in js_strs):
        res = "JS uma porra!\nJS e` tao cancer que comeca com J, de Javascript"
        sticker = stk_fodase if randint(0, 10) else stk_queromorre
    elif any(s in m for s in cpp_strs):
        res = "C++ eh cancer!."
    elif any(s in m for s in oop_strs):
        res = "Ja ouviu falar de FP?"
    elif any(s in m for s in java_strs):
        res = "Continue to use that crap and you're out."
    elif any(s in m for s in nice_strs):
        res = "delicia"
        sticker = stk_delicia1 if react() else stk_delicia2
    elif "monstro" in msg_norm:
        sticker = stk_monstro
    elif any(s in m for s in hell_strs):
        sticker = stk_satan
    elif any(s in m for s in bom_strs):
        if stk_bool:
            bot.sendSticker(chat_id, stk_card)
        sticker = stk_kibon if react() else stk_flip
    elif any(s in msg_norm for s in hue_strs):
        res = "AHUHAAUUhuahua"
        sticker = stk_hue
    elif "suissa" in msg_norm:
        res = "o suissa eh tao cancer q chamam  ele de JS AUEHAUH"
        sticker = stk_hue
    elif any(s in msg_norm for s in manoel_strs) and "voltar" in msg_norm:
        res = "to aqui carai"
    elif any(s in msg_norm for s in manoel_strs):
        res = "oi"

    if res:
        bot.sendMessage(chat_id, res, reply_to_message_id=message_id)

    if sticker and stk_bool:
        bot.sendSticker(chat_id, sticker)


def repl(chat_id):
    try:
        while True:
            msg = input("> ")
            bot.sendMessage(chat_id, msg)
            if msg == "/quit":
                break
    except Exception as EOFError:
        exit(0)
    except Exception as e:
        print("Cancer happened: {!r}".format(e))
        exit(1)


def bot_loop():
    bot.message_loop(handle)
    print('Listening ...')

    # Keep the program running.
    while 1:
        time.sleep(10)


def main():
    if sys.argv[2] == 'repl':
        repl(UAPDA)
    elif sys.argv[2] == 'bot':
        bot_loop()


if __name__ == '__main__':
    main()
