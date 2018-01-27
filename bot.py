# coding: utf-8

import sys
import time
import os
from pprint import pprint
from random import randint
from datetime import datetime
import telepot

UAPDA = -1001096359543  # UAPDA chat id, where lelerax born
TOKEN = sys.argv[1]  # get token from command-line
bot = telepot.Bot(TOKEN)
REACT_FACTOR = 10  # probability between of react: from 0 to 100 (max reaction)
DEBUG = os.environ.get('DEBUG')
ANSWER_THIS_SHIT = False


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


def bot_engine(chat_id, msg, message_id):
    if msg.lower().startswith("/uapda"):
        clean_msg = msg.replace("/uapda", "").strip()
        if clean_msg:
            bot.sendMessage(UAPDA, clean_msg)
            print("LOG: UAPDA -> {!r}".format(clean_msg))
    else:
        bot_answers(chat_id, msg, message_id)


def bot_answers(chat_id, msg, message_id):
    global ANSWER_THIS_SHIT
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

    if 'lelerax' in msg_norm:
        ANSWER_THIS_SHIT = True

    if react(20) and any(s in m for s in js_strs):
        res = ":[ Jesus amado, JavaScript não... por favor."
        sticker = stk_fodase if react(10) else stk_queromorre
    elif react(20) and any(s in m for s in cpp_strs):
        res = "C++... hmmm, pelo menos é melhor que Java e, obviamente, JS."
    elif react(20) and any(s in m for s in oop_strs):
        res = "Quantos objetos... AI MEU DEUS UMA CONDIÇÃO DE CORRIDA."
    elif react(20) and any(s in m for s in java_strs):
        res = "Cara, Java? Aproveita e vai ler um livro de programação de verdade... coisa triste."
    elif react(50) and any(s in m for s in nice_strs):
        res = "Excelente! Eu gostei."
        sticker = stk_delicia1 if react() else stk_delicia2
    elif "monstro" in msg_norm:
        sticker = stk_monstro
    elif any(s in m for s in hell_strs):
        sticker = stk_satan
    elif any(s in m for s in bom_strs):
        if stk_bool:
            bot.sendSticker(chat_id, stk_card)
        sticker = stk_kibon if react() else stk_flip
    elif react(5) and any(s in msg_norm for s in hue_strs):
        res = "kkkkkkkk"
        sticker = stk_hue
    elif react(30) and "suissa" in msg_norm:
        res = "Não profira nome de demônio na casa sagrada do resto da APDA que presta."
        sticker = stk_hue
    elif react(50) and any(s in msg_norm for s in manoel_strs) and "voltar" in msg_norm:
        res = "To aqui, carai!"
    elif react(50) and any(s in msg_norm for s in manoel_strs):
        res = "Oi"

    if res:
        bot.sendMessage(chat_id, res, reply_to_message_id=message_id)

    if sticker and stk_bool:
        bot.sendSticker(chat_id, sticker)

    ANSWER_THIS_SHIT = False


def repl(chat_id):
    try:
        while True:
            msg = input("> ")
            if msg == "/quit":
                break
            elif msg.startswith("/img"):
                bot.sendPhoto(chat_id, open(msg[4:].strip(), "rb"))
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
        repl(UAPDA)
    elif sys.argv[2] == 'bot':
        bot_loop()


if __name__ == '__main__':
    main()
