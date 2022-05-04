""" 


Welcome 👋🏼!

This repl contains all of source code of the GalGuard Discord bot. 

Please consider adding our bot to your discord server to support our work.
Invite link: https://discord.com/api/oauth2/authorize?client_id=963457369310916678&permissions=8&scope=bot (copy and paste into browser)

😊 Happy coding!

  — Sincerely, FoxyCoder (co-owner of the bot)


""" 

#[----------IMPORTS----------]
import discord
from discord.ext import commands
import os
import json
from Cogs.init import Init
from Cogs.info import Info
from Cogs.moderation import Moderation
from Cogs.errors import Errors
from Cogs.fun import Fun
from Cogs.math import Math
from Cogs.giveaways import Giveaways
from Cogs.bomb import Bomb
from hosting import keep_alive
from datetime import datetime
from datetime import date
import time
from discord_ui import Components, Button, UI


#[----------PREFIXES----------]
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]


#[----------BOT----------]
client = commands.Bot(command_prefix=get_prefix, help_command=None)
ui = UI(client)

#[----------EVENTS----------]
@client.event
async def on_ready():
    print("✅ Main.py loaded!")


#client.process_commands(message)
# ^^^ add to every event ^^^

#[----------COMMANDS----------]


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        prefixes[str(guild.id)] = '?'
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        prefixes.pop(str(guild.id))
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def set_prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        await ctx.send(f"> ✅ **Prefix has been updated to `{prefix}`.**")
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.command()
async def test(ctx):
    await ctx.send("> ✅ **Bot is operational, running all cogs.**")


@client.command()
async def ping(ctx):
    await ctx.send(
        f">>> ⌛ Bot's current latency is **{client.latency * 1000}** ms.")


client.add_cog(Init(client))
client.add_cog(Info(client))
client.add_cog(Moderation(client))
client.add_cog(Errors(client))
#client.add_cog(Translate(client))
client.add_cog(Fun(client))
client.add_cog(Math(client))
client.add_cog(Bomb(client))
client.add_cog(Giveaways(client))

#[----------LOGGING IN----------]
keep_alive()
tokenvar = os.environ['token']
client.run(tokenvar)
