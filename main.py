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

class InfoMenu(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None
    self.add_item(discord.ui.Button(label="Source Code", url = "https://github.com/EtherealGroup/KeyAuth", emoji="<githubwhite:1252766253777420349>"))

@client.tree.command(name="redeem", description="Redeems product key")
@app_commands.describe(key = "Your product key")
async def redeem(interaction: discord.Interaction, key: str):
   isValid = await searchKeys(key)
   if (isValid):
    await interaction.response.send_message("Your product key is **VALID** ✅\nHere's a cookie: 🍪", ephemeral = True)
   else:
    await interaction.response.send_message("Your product key is **INVALID** ❌", ephemeral = True)

@client.tree.command(name = "info", description = "Information about the bot, and the source code")
async def info(interaction: discord.Interaction):
  view = InfoMenu()
  infoEmbed = discord.Embed(title="Information", color=0x777777)
  infoEmbed.add_field(name="About KeyAuth", value = "KeyAuth is a framework for seamlessly authenticating various types of keys.", inline = False)
  infoEmbed.add_field(name="Ethereal Group", value = "We are Ethereal Group, the developers of this discord bot. We're focused on making open-source and high quality discord bots", inline = False)
  infoEmbed.set_thumbnail(url = "https://avatars.githubusercontent.com/u/173092938?s=200&v=4")
  infoEmbed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar)
  await interaction.response.send_message(embed=infoEmbed, view=view)
  
async def searchKeys(key):
    key = key.strip() # Removes any whitespace characters.
    with open("keys.txt", "r") as f: # keys.txt is the text file in which your keys are stored.
        for x in f:
            if x.strip() == key:
                return True
    return False


client.run(TOKEN)
