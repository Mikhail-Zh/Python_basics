from random import randint
import time
from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher

start_game = 0
A = 1
player_move = 2
bot_win = 3
bot_move = 4

num_start = 0  # Переменная для хранения общего количества конфет
num_candy = 0  # Переменная для хранения максимального количества конфет которое можно взять за ход
complexity = 0  # Переменная для хранения уровня сложности бота


def start(update, context):
    """Начало игры. Вывод правила игры. Запрос общего количества конфет"""
    context.bot.send_message(update.effective_chat.id, 'Правила игры:')
    context.bot.send_message(update.effective_chat.id, 'Кто заберет последнюю конфету тот и победил.')
    context.bot.send_message(update.effective_chat.id, 'Укажите количество конфет на столе:')
    return start_game


def num_candies(update, context):
    """Определение количества конфет которое можно взять за ход. Запрос сложности игры."""
    global num_start
    global num_candy
    num_start = int(update.message.text)
    num_candy = 28 if num_start >= 1001 else 14
    context.bot.send_message(update.effective_chat.id, f'За ход можно взять не более {num_candy} конфет')
    context.bot.send_message(update.effective_chat.id, 'Укажите сложность: 0 - легко, 1 - сложно')
    return A


def out_message_bot(update, context, quantity_candy, num):
    """Вывод фраз бота во время игры"""
    context.bot.send_message(update.effective_chat.id, f'Я взял {quantity_candy}')
    context.bot.send_message(update.effective_chat.id, f'Осталось {num}')


def definition_complexity_game(update, context):
    """Определение игрока который начнет игру"""
    global complexity
    complexity = int(update.message.text)
    context.bot.send_message(update.effective_chat.id, 'Великий рандом определит чей первый ход')
    time.sleep(1)  # Задержка времени, для того чтобы успевать прочитать фразу выше
    for i in range(3, 0, -1):  # Обратный отсчет
        context.bot.send_message(update.effective_chat.id, i)
        time.sleep(0.5)
    first_player = randint(0, 1)
    if first_player:
        context.bot.send_message(update.effective_chat.id, 'Первым ходите Вы')
        return player_move
    else:
        context.bot.send_message(update.effective_chat.id, 'Первым хожу я')
        bot_player(update, context)
        return player_move


def bot_player(update, context):
    """Функция логики игрока bot"""
    # bot с интеллектом
    global num_candy, num_start, complexity
    if complexity == 1:
        if num_start <= num_candy:
            quantity_candy = num_start
            num_start = 0
            out_message_bot(update, context, quantity_candy, num_start)
            bot_finish(update, context)
            return bot_win
        elif num_start % num_candy == 1 and (num_start // num_candy) % 2 != 0:
            num_start -= num_candy
            quantity_candy = num_candy
            out_message_bot(update, context, quantity_candy, num_start)
            return player_move
        elif num_start % num_candy == 0:
            quantity_candy = num_candy - 1
            num_start -= quantity_candy
            out_message_bot(update, context, quantity_candy, num_start)
            return player_move
        elif num_start % num_candy == 1:
            quantity_candy = num_start % num_candy
            num_start -= quantity_candy
            out_message_bot(update, context, quantity_candy, num_start)
            return player_move
        elif num_start % num_candy != 0:
            quantity_candy = num_start % num_candy - 1
            num_start -= quantity_candy
            out_message_bot(update, context, quantity_candy, num_start)
            return player_move
    # bot без интеллекта
    else:
        if num_start > num_candy:
            quantity_candy = randint(1, num_candy - 1)
            num_start -= quantity_candy
            out_message_bot(update, context, quantity_candy, num_start)
            return player_move
        else:
            quantity_candy = num_start
            num_start -= quantity_candy
            out_message_bot(update, context, quantity_candy, num_start)
            bot_finish(update, context)
            return ConversationHandler.END


def player(update, context):
    """Функция хода игрока"""
    global num_start
    selected_number = update.message.text
    if selected_number.isdigit():
        selected_number = int(selected_number)
    else:
        context.bot.send_message(update.effective_chat.id, f'Введены не верные данные')
        return player_move
    if selected_number > num_candy or selected_number <= 0 or selected_number > num_start:
        context.bot.send_message(update.effective_chat.id, f'Введены не верные данные')
        return player_move
    num_start -= selected_number
    context.bot.send_message(update.effective_chat.id, f'Осталось {num_start}')
    if num_start > 0:
        bot_player(update, context)
    else:
        player_win(update, context)
        return ConversationHandler.END


def bot_finish(update, context):
    """Победил Бот"""
    context.bot.send_message(update.effective_chat.id, f'Я победил!!!')


def player_win(update, context):
    """Победил Игрок"""
    context.bot.send_message(update.effective_chat.id, f'Поздравляю!!! Победа за Вами.')


def bot_cancel(update, context):
    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')


start_handler = CommandHandler('start', start)
num_candies_handler = MessageHandler(Filters.text, num_candies)
definition_complexity_handler = MessageHandler(Filters.text, definition_complexity_game)
player_handler = MessageHandler(Filters.text, player)
bot_player_handler = MessageHandler(Filters.text, bot_player)
bot_finish_handler = MessageHandler(Filters.text, bot_cancel)
mes_candies_handler = MessageHandler(Filters.text, cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={start_game: [num_candies_handler],
                                           A: [definition_complexity_handler],
                                           player_move: [player_handler],
                                           bot_move: [bot_player_handler],
                                           bot_win: [bot_finish_handler]},
                                   fallbacks=[mes_candies_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()

