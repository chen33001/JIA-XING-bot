# 吳家興/cmds/welcome.py
from discord.ext import commands
import discord
import json
import os

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("✅ Welcome cog loaded")

        # 載入設定
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(base_dir, 'setting.json'), 'r', encoding='utf8') as f:
            self.jdata = json.load(f)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.jdata["Gaming house"])
        await channel.send(f"{member.mention} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(self.jdata["Gaming house"])
        await channel.send(f"{member.mention} leave!")

async def setup(bot):
    print("✅ Running setup() for Welcome")
    await bot.add_cog(Welcome(bot))
