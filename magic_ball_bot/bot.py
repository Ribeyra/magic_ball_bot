# from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import choice
from sticker_lists import positive, indecisive, neutral, negative
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')

list_of_quest = [
    'как', 'что', 'сколько', 'где', 'какой', 'кто', 'когда', 'почему', 'чем',
    'чего', 'куда', 'который', 'кому', 'зачем', 'откуда', 'чей', 'чья',
    'каков', 'отчего'
]

answer_list = []

answer_list.append(positive)
answer_list.append(indecisive)
answer_list.append(neutral)
answer_list.append(negative)


def start(update, context):
    # user = update.effective_user
    update.message.reply_text('Задай свой вопрос')


def echo(update, context):
    list_text = update.message.text.split()
    if (
        len(list_text) > 2 and
        list_text[0].lower() == 'как' and
        list_text[1].lower().startswith('думаешь')
    ):
        list_text = list_text[2:]
    if list_text[0].lower() in list_of_quest:
        update.message.reply_text('Вопросы только на да или нет')
    elif update.message.text[-1] != '?':
        update.message.reply_text('Я могу только отвечать на вопросы')
    else:
        update.message.reply_sticker(sticker=magic_8_ball())


def magic_8_ball():
    lst = choice(answer_list)
    return choice(lst)


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, echo)
    )

    updater.start_polling()
    updater.idle()
