# JIA-XING-bot
#  吳家興 Discord Bot

A modular Discord bot built using `discord.py`, featuring cog-based command organization, welcoming messages, and random image posting.

## Features

**Modular Cog System** (`main.py + cmds/*.py`)<br>
`家興:圖片` – Send a random image from a preset list<br>
`家興:ping` – Check bot latency<br>
Auto welcome/farewell messages on member join/leave<br>
Configurable via `setting.json`<br>
Ready for production and extensible<br>

## Requirements

Python 3.10+
`discord.py` 2.3+
A Discord bot token

Install dependencies:

```bash
pip install -U discord.py
python3 -m 吳家興.main
