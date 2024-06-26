import os
import discord
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="ka!", intents=intents, case_insensitive=True)


@client.event
async def on_ready():
  print("Bot is online!")
  try:
    synced = await client.tree.sync()
    print(f"synced {len(synced)} commands")
  except Exception as e:
    print(e)




client.run(TOKEN)
