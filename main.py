import os
import random
from dotenv import load_dotenv
import telebot

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "I am Royaska Bot made for emotional support of those who I deem to be my friends")


@bot.message_handler(commands=['hello'])
def send_emiliya(message):
    bot.reply_to(message, "Hello amk")


@bot.message_handler(commands=['joke'])
def send_joke(message):
    text = "Как называется то состояние когда ни одной свободной минутки нет?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, cont_joke)

def cont_joke(message):
    text = "Мин.нет"
    bot.reply_to(message, text)
    

@bot.message_handler(commands=['yomama'])
def yomama_joke(message):
    jokes = ["Yo momma's so fat and old when God said, \"Let there be light,\" he asked your mother to move out of the way.", 
             "Yo mama's so fat, when her beeper goes off, people think shes backin up",
             "Yo momma's so fat, that when she fell, no one was laughing but the ground was cracking up.",
             "Yo mama's so classless, she's a Marxist utopia.",
             "Yo mama's so depressing, blues singers come to visit her when they've got writer's block.",
             "Yo mama is so mean, Taylor Swift wrote a song about her.",
             "Yo momma so short, she went to see Santa and he told her to get back to work.",
             "Yo momma so old, she knew Burger King when he was a prince.",
             "Yo mama is so nasty, she went swimming and made the Dead Sea.",
             "Yo mama's so poor, Nigerian princes wire her money.",
             "Yo momma so old, she was a waitress at the Last Supper.",
             "Yo mama's so poor, she can't even afford to pay attention.",
             "Yo mama is so scary, even Voldemort won't say her name.",
             "Yo Mama's so old, when she was in school there was no history class.",
             "Yo mama is so scary, the government moved Halloween to her birthday.",
             "Yo mama's so mean, they don't give her happy meals at McDonald's.",
             "Yo mama's so confusing, even Scooby Doo couldn't solve that mystery."]
    bot.reply_to(message, random.choice(jokes))
    

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "cringe")


bot.infinity_polling()

