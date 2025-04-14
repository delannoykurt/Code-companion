import os
import random
import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

ressources = [
    "https://overapi.com/javascript",
    "https://developer.mozilla.org/fr/",
    "https://visualgo.net/fr",
    "https://rogerdudler.github.io/git-guide/index.fr.html"
]

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command(name="ressource", help="Affiche une ressource aléatoire")
async def ressource(ctx):
    lien = random.choice(ressources)
    await ctx.send(f"📘 Voici une ressource : {lien}")

bot.run(TOKEN)
