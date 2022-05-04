import discord
from discord.ext import commands
import asyncio
import json

class Moderation(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("✅ Moderation Cog loaded!")


  #[KICK]
  @commands.command(aliases=["kc","kik","kic"])
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason="no reason"):
    await member.kick(reason=reason)
    await ctx.send(f"> ✅ **{member}** has been kicked for {reason}.", delete_after=10)
    await ctx.message.delete(delay=10)

  #[BAN]
  @commands.command(aliases=["b","ba","bn"])
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason="no reason"):
    await member.ban(reason=reason)
    await ctx.send(f"> ✅ **{member}** has been banned for {reason}.", delete_after=10)
    await ctx.message.delete(delay=10)


  #[CLEAR]
  @commands.command(aliases=["purge","pr","cl","pg","purg"])
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, number: int=2):
    await ctx.channel.purge(limit = number)
    channel = ctx.channel
    if number == 1: 
      await ctx.send(f"> ✅ **{number}** message have been cleared in **{channel.mention}**.", delete_after=10)
      await ctx.message.delete(delay=10)
    else: 
      await ctx.send(f"> ✅ **{number}** messages have been cleared in **{channel.mention}**.", delete_after=10)
      await ctx.message.delete(delay=10)

  #[TEMPBAN]
  # removed for now, check code.txt in "other" folder


#[LOCK & UNLOCK]
  @commands.command(aliases=["lck", "lk"])
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, channel : discord.TextChannel=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      await ctx.send(f">>> 🔒 Channel **{channel}** is locked for `{ctx.guild.default_role}`.")

  
  @commands.command(aliases=["unlck", "ulk"])
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx, channel : discord.TextChannel=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      await ctx.send(f">>> 🔓 Channel **{channel}** is unlocked.")


# [MUTE & UNMUTE]
  @commands.has_permissions(manage_roles = True)
  @commands.command(aliases = ["mt"])
  async def mute(self, ctx, member: discord.Member, *, reason=None):
      guild = ctx.guild
      yesorno = 0
      for role in guild.roles:
          if role.name == "Muted":
              yesorno = 1
              await member.add_roles(role)
  
              await ctx.send(f">>> 🔇 **{member}** was muted indefinitely.")
  
              return
      if yesorno == 0:
          guild = ctx.guild
          perms = discord.Permissions(send_messages = False, view_channel = True)
          await guild.create_role(name="Muted", permissions = perms)
          await member.add_roles("Muted")
  
          await ctx.send(f">>> 🔇 **{member}** was muted indefinitely, *muted* role created because no muted role was found in the server*.")

  
  
  @commands.has_permissions(manage_roles = True)
  @commands.command(aliases = ["umt"])
  async def unmute(self, ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    for role in guild.roles:
      if role.name == "Muted":
        await member.remove_roles(role)
    
    await ctx.send(f">>> 🔊 **{member}** was unmuted.")

# [AUTOMOD]
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    with open('automod.json', 'r') as f:
      prefixes = json.load(f)
      prefixes[str(guild.id)] = 'off'
    with open('automod.json', 'w') as f:
      json.dump(prefixes, f, indent=4)

  @commands.Cog.listener()
  async def on_guild_remove(self, guild): 
      with open('automod.json', 'r') as f:
        prefixes = json.load(f)
        prefixes.pop(str(guild.id))
      with open('automod.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
  

      
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def automod(self, ctx, toggle="on"):
    with open('automod.json', 'r') as f:
      prefixes = json.load(f)
      prefixes[str(ctx.guild.id)] = toggle
      await ctx.send(f"> ✅ **Automod has been turned `{toggle}`.**")
    with open('automod.json', 'w') as f:
      json.dump(prefixes, f, indent=4)


  
  

  
  @commands.Cog.listener() 
  async def on_message(self, message):
    def automod_test(message):
      with open('automod.json', 'r') as f:
        prefixes = json.load(f)
      return prefixes[str(message.guild.id)]
    
    if automod_test(message) == "on":
      banned_words = ["fuck", "shit", "nigger", "nigga", "niga", "dick", "faggot", "cock", "pussy", "cunt", "bitch"]
      cnt = message.content.lower()
      for word in banned_words:
        if word in cnt:
          member = message.author
          await message.channel.send(f">>> ⛔ **Watch your language, {member.mention}.**", delete_after = 10)
          await message.delete()
        



