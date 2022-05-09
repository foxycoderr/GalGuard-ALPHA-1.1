import discord
from discord.ext import commands
import asyncio

class Init(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("✅ Init Cog loaded!")
    client = self.client
    while True: 
      await self.client.change_presence(activity=discord.Game(name="?help"))
      await asyncio.sleep(5)
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f" {str(len(client.guilds))} servers | {sum([guild.member_count for guild in client.guilds])} users")) 
      await asyncio.sleep(5)