# 吳家興/cmds/圖片.py
import discord
from discord.ext import commands
import json
import random
import os

with open(os.path.join(os.path.dirname(__file__), '..', 'setting.json'), 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class 圖片(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 圖片(self, ctx):
        random_pic = random.choice(jdata['pic'])  # pic 是圖片路徑 list
        pic = discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def 九號(self, ctx):
        await ctx.send('嘿嘿嘿')

def setup(bot):
    bot.add_cog(圖片(bot))
