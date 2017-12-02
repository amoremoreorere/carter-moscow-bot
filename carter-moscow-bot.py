# -*- coding: utf-8 -*-
import telebot
import requests
from telebot import types
import logging
import os

TOKEN = '443038853:AAGkWWhT0toBHvyniNc0VAShL1ZNBhbSRYU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, message.from_user.first_name + ', Добро пожаловать! Здесь ты можешь подобрать одежду своему малышу.\nКому ищешь? \nЕсли мальчику, то жми /boy. \nЕсли девочке, то жми /girl. \n Хочешь узнать историю бренда Carters, жми /history \nЧтобы узнать о доставке, жми /dostavka \nУзнать о размерах Картер, жми /size_chart \nКоманда /help ознакомит тебя со всеми моими возможностями и командами \nЕсли живешь в Строгино, жми /strogino')

@bot.message_handler(commands=['help'])
def start(message):
    sent = bot.send_message(message.chat.id, message.from_user.first_name + ', я помогу тебе здесь разобраться. Вот команды, которые я знаю: \n \start - чтобы начать выбор одежды  \n/zakaz - чтобы сделать заказ \n/dostavka - узнать о доставке \n/history - узнать историю бренда Картерс \n/size_chart - определить размер одежды малыша')

if __name__ == '__main__':
    bot.polling(none_stop=True)
