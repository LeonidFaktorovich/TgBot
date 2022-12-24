from telebot.async_telebot import AsyncTeleBot
import telebot
import asyncio

bot = AsyncTeleBot('5925498570:AAHnk7IF9o1MI3aCNSykOT35WexEXWYYxQU')


@bot.message_handler(commands=['MSU'])
async def msu(message):
    await bot.send_message(message.chat.id, "evaluation: 5/10")


@bot.message_handler(commands=['HSE'])
async def hse(message):
    await bot.send_message(message.chat.id, "evaluation: 8/10")


@bot.message_handler(commands=['MIPT'])
async def mipt(message):
    await bot.send_message(message.chat.id, "evaluation: 8/10")


@bot.message_handler(commands=['KFU'])
async def kfu(message):
    await bot.send_message(message.chat.id, "evaluation: 6/10")


@bot.message_handler(commands=['SPBGU'])
async def spbgu(message):
    await bot.send_message(message.chat.id, "evaluation: 8/10")


@bot.message_handler(commands=["help"])
async def help(message):
    await bot.send_message(message.chat.id,
                           "if you want to get evaluation of MSU, HSE, MIPT, KFU or SPBGU just send: /MSU, /HSE, /MIPT, /KFU or /SPBGU")


@bot.message_handler(commands=["start"])
async def start(message): 
    await bot.send_message(message.chat.id,
                           "if you want to get evaluation of MSU, HSE, MIPT, KFU or SPBGU just send: /MSU, /HSE, /MIPT, /KFU or /SPBGU")


# Do not forget to register
bot.add_custom_filter(telebot.asyncio_filters.ChatFilter())

asyncio.run(bot.polling())
