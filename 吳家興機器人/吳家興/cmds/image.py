# 吳家興/cmds/image.py
import discord
from discord.ext import commands
import random
import json
import os

class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("✅ Image cog loaded")

        # 載入設定檔（內建載入 setting.json）
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base_dir, 'setting.json'), 'r', encoding='utf8') as f:
            self.jdata = json.load(f)

    # image_command 中
    @commands.command(name="圖片", help="隨機傳一張圖片")
    async def image_command(self, ctx):
        relative_path = random.choice(self.jdata["pic"])
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pic_path = os.path.join(base_dir, relative_path)
        pic = discord.File(pic_path)
        await ctx.send(file=pic)


async def setup(bot):
    print("✅ Running setup() for Image")
    await bot.add_cog(Image(bot))
