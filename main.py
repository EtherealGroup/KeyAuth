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

@client.tree.command(name="redeem", description="Redeems product key")
@app_commands.describe(key = "Your product key")
async def redeem(interaction: discord.Interaction, key: str):
   isValid = await searchKeys(key)
   if (isValid):
    await interaction.response.send_message("Your product key is **VALID** ✅\nHere's a cookie: 🍪")
   else:
    await interaction.response.send_message("Your product key is **INVALID** ❌")
  
async def searchKeys(key):
    key = key.strip() # Removes any whitespace characters.
    with open("keys.txt", "r") as f: # keys.txt is the text file in which your keys are stored.
        for x in f:
            if x.strip() == key:
                return True
    return False


client.run(TOKEN)
