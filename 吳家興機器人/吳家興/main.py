# 吳家興/main.py
import discord
from discord.ext import commands
import json
import os
import traceback

# 設定 Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# 建立 Bot 實例
bot = commands.Bot(command_prefix="家興:", intents=intents)

# 讀取設定檔
with open(os.path.join(os.path.dirname(__file__), 'setting.json'), mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

# 自動載入所有 cmd 模組 + 顯示是否載入成功
# ✅ 這是新版 discord.py 推薦的初始化方式
@bot.event
async def setup_hook():
    cmd_path = os.path.join(os.path.dirname(__file__), 'cmds')
    for filename in os.listdir(cmd_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            try:
                await bot.load_extension(f'吳家興.cmds.{filename[:-3]}')
                print(f"✅ Loaded: {filename}")
            except Exception as e:
                print(f"❌ Failed to load {filename}: {e}")
                traceback.print_exc()

# Bot 上線時
@bot.event
async def on_ready():
    print(">> Bot is online <<")
    print(f"✅ Bot command prefix is: {bot.command_prefix}")
    print("📋 Registered commands:")
    for command in bot.commands:
        print(f"- {command.name}")



@bot.command()
async def 幫助(ctx):
    commands_list = [command.name for command in bot.commands]
    await ctx.send(f"目前可用指令：{', '.join(commands_list)}")





# 啟動 Bot
bot.run(jdata['TOKEN'])
