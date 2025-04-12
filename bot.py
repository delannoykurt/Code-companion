import discord
import random

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

ressources = [
    "https://overapi.com/javascript",
    "https://developer.mozilla.org/fr/",
    "https://visualgo.net/fr",
    "https://rogerdudler.github.io/git-guide/index.fr.html"
]

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command(description="Obtiens une ressource aléatoire")
async def ressource(ctx):
    lien = random.choice(ressources)
    await ctx.respond(f"📘 Voici une ressource : {lien}")


bot.run(TOKEN)

