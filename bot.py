import discord
import requests
from discord.ext import commands

# Настройки для бота
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# ========== 1. Экологические советы из интернета ==========
def get_eco_tips():
    url = "https://api.adviceslip.com/advice"  # Используем API для получения случайного совета
    res = requests.get(url)
    data = res.json()
    if 'slip' in data:
        tip = data['slip']['advice']
        return tip
    else:
        return "Не удалось получить совет. Попробуйте позже."

@bot.command(help="Отправляет случайный совет по защите окружающей среды.")
async def ecotip(ctx):
    tip = get_eco_tips()
    await ctx.send(tip)
