import discord
from discord.ext import commands
import asyncio
import datetime
from datetime import datetime



class Init(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("✅ Init Cog loaded!")
    client = self.client
    i = 0
    while True: 
      await self.client.change_presence(activity=discord.Game(name="?help"))
      await asyncio.sleep(5)
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f" {str(len(client.guilds))} servers | {sum([guild.member_count for guild in client.guilds])} users")) 
      await asyncio.sleep(5)
      i = i + 1
      if i == 180:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        channel = await self.client.fetch_channel(974573495667273748)
        await channel.send(f"**ALPHA UP** at {current_time}")
        i = 0