# coding: utf-8

import sys
import time
import os
from pprint import pprint
from random import randint
from datetime import datetime
import telepot
from random import choice

UAPDA = -1001096359543  # UAPDA chat id, where lelerax born
LISP = -1001280636766
KADICU= -1001444576606
CHATS = {
    'uapda': UAPDA,
    'lisp': LISP,
    'kadicu': KADICU,
}

TOKEN = sys.argv[1]  # get token from command-line
bot = telepot.Bot(TOKEN)
REACT_FACTOR = 5  # probability between of react: from 0 to 100 (max reaction)
DEBUG = os.environ.get('DEBUG')
ANSWER_THIS_SHIT = False

# String -> Tuple[String]
keywords = {
    "js": ("js", "javascript", "ecmascript", "ecma", "ecma6"),
    "cpp": ("c++", "bjarne stroustrup", "cancer++", "cpp"),
    "java": ("java", "javismo", "jre", "jvm"),
    "oop": ("opp", "poo", "smalltalk"),
    "nice": ("python", "haskell", "erlang", "c", "lua", "brain", "lisp",
              "rust", "cl"),
    "manoel": ("manoel", "lelerax", "lerax", "ryukinix"),
    "hell": ("satan", "diabo", "demonio", "inferno", "fogo", "hell", "suissa"),
    "bom": ("bom", "kibon", "massa", "funciona", "funcionando",
            "funcionou", "rodar", "rodou", "compilar", "compilou"),
    "hue": ("hue", "hu3", "haha", "kkkk", "huashuash")

}

# String -> Tuple[String]
reactions = {
    "js": (":[ Jesus amado, JavaScript não... por favor.",
           "Se JS fosse bom eu estava usando."),
    "cpp": ( "C++... hmmm, pelo menos é melhor que Java e, obviamente, JS.",
             "Parece que encontramos um.... MASOQUISTA"),
    "java": ("Cara, Java? Aproveita e vai ler um livro de programação de verdade... coisa triste.",
             "Gogo JAVA CHECKED EXCEPTIONS.",
             "Pera aí, deixa eu comprar mais um pente de RAM rapidão aqui."),
    "oop": ("Quantos objetos... AI MEU DEUS UMA CONDIÇÃO DE CORRIDA.",
            "Meu Deus, quantos estados nesses objetos! D:"),
    "nice": ("Excelente! Eu gostei.", "Aê, aprovado!", "Porra, muito bom, cara!",
             "Ensina aí pra nóis", "Assim eu gosto", "Tem que ser assim mesmo!"),
    "manoel": ("To aqui, carai!", "Oi"),
    "hell": ("Coisa do demônio!.",
             "Rapaz que parada mais cancer."),
    "hue": ("kkkkkkkk", "caramba kkk", "carai mano kkkk", "porra kkkk", "fala serio kkkk",
            "toma kkkkk"),
}


# String -> String
stickers = {
    "card": "CAADAQADfwAD5G3CCTY2lvkcjTKUAg",
    "monstro": "CAADAQAD3QAD5G3CCfzBqgbKrcVvAg",
    "delicia1": "CAADAgADhwAD12I0BVT0buDrX9dLAg",
    "delicia2": "CAADAgADcAAD12I0Bd-BteG_OrJCAg",
    "fodase": "CAADAQADPQADarEOBvuO0Zx96BjxAg",
    "queromorre": "CAADAQADRQADarEOBrMse4T-xV6SAg",
    "satan": "CAADAQADtQADarEOBiaPApuCmIsjAg",
    "hue": "CAADAQADxwAD5G3CCXbWeLF4Nd78Ag",
    "kibon": "CAADAQADzwAD5G3CCdroYc38v2yHAg",
    "flip": "CAADAQADyQAD5G3CCaRAcC_I79baAg"
}


def react(x=REACT_FACTOR):
    return randint(1, 100//x) == 1 or ANSWER_THIS_SHIT


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if DEBUG:
        print("LOG: {}".format(datetime.now()))
        debug = dict(msg=msg, content_type=content_type,
                     chat_type=chat_type, chat_id=chat_id)
        pprint(debug)
    if content_type == 'text':
        bot_engine(chat_id, msg['text'], msg['message_id'])

def anonymouns_message(command, chat_id, msg):
    if msg.lower().startswith(command):
        clean_msg = msg.replace(command, "").strip()
        if clean_msg:
            bot.sendMessage(chat_id, clean_msg)
            print("LOG: {!r} -> {!r}".format(command, clean_msg))
            return True

    return False


def bot_engine(chat_id, msg, message_id):
    anonymouns_message("/uapda", UAPDA, msg) or  \
        anonymouns_message("/lisp", LISP, msg) or \
        bot_answers(chat_id, msg, message_id)


def bot_answers(chat_id, msg, message_id):
    global ANSWER_THIS_SHIT

    msg_norm = msg.lower()
    m = msg_norm.split()
    sticker_flag = react()
    sticker = ""
    res = ""

    if 'lelerax' in msg_norm:
        ANSWER_THIS_SHIT = True

    for category, keys in keywords.items():
        if category in reactions and any(s in m for s in keys):
            res = choice(reactions[category])

    if "monstro" in msg_norm:
        sticker = stickers["monstro"]
    elif any(s in m for s in keywords["hell"]):
        sticker = stickers["satan"]
    elif any(s in m for s in keywords["bom"]):
        if sticker_flag:
            bot.sendSticker(chat_id, stickers["card"])
        sticker = stickers["kibon"] if react() else stickers["flip"]

    if react() and res:
        bot.sendMessage(chat_id, res, reply_to_message_id=message_id)

    if sticker and sticker_flag():
        bot.sendSticker(chat_id, sticker)

    ANSWER_THIS_SHIT = False


def repl(chat):
    try:
        chat_id = CHATS[chat]
        while True:
            msg = input("{}> ".format(chat))
            if msg == "/quit":
                break
            elif msg.startswith("/img"):
                bot.sendPhoto(chat_id, open(msg.split()[1].strip(), "rb"))
            elif msg.startswith("/file"):
                bot.sendDocument(chat_id, open(msg.split()[1].strip(), "rb"))
            elif msg.startswith("/leave"):
                bot.leaveChat(chat_id)
            elif msg.startswith("/chat"):
                chat = msg.split()[1].lower()
                chat_id = CHATS[chat]
            else:
                bot.sendMessage(chat_id, msg)
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
        repl('uapda')
    elif sys.argv[2] == 'bot':
        bot_loop()


if __name__ == '__main__':
    main()
