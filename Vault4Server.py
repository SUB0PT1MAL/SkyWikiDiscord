import os
import discord
from discord.ext import commands
import fandom

BOT_TOKEN = os.environ['BOT_TOKEN']

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def vault(ctx, *, query):
    fandom.set_wiki('sky-children-of-the-light')
    results = fandom.search(query, results=1)
    if not results:
        await ctx.message.reply(f"No results found for '{query}'.")
    else:
        page = fandom.page(results[0][0])
        summary = page.summary[:200] + "..." if len(page.summary) > 200 else page.summary
        url = page.url
        await ctx.message.reply(f"**{page.title}**\n{summary}\n\n{url}")


bot.run(BOT_TOKEN)