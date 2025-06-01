# 吳家興/cmds/ping.py
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("✅ Ping cog loaded")

    @commands.command(name="ping", help="Show bot latency")
    async def ping_command(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)} ms")

# ✅ 必須是 async def！
async def setup(bot):
    print("✅ Running setup() for Ping")
    await bot.add_cog(Ping(bot))
