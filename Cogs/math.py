import discord
from discord.ext import commands
from google_translate_py import Translator
import random

class Math(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print("✅ Math Cog loaded!")

    
# [CALCULATOR]
  @commands.command(aliases=["cal", "calc"])
  async def calculate(self, ctx, expression : str):
    if (len(expression) < 10):
      await ctx.send(f">>> 🧮 **Input:** `{expression}` \n🔢**Result:** `{eval(expression)}`")
    else:
      await ctx.send(">>> ❌ **Sorry, your enetered calculation is too long.** We apologise for any inconvenience.")
    

# [RNG]
  @commands.command(aliases=["rng","rand"])
  async def random(self, ctx,num1=-9999999, num2=9999999):
    num1 = int(num1)
    num2 = int(num2)
    res = random.randint(num1, num2)
    await ctx.send(f">>> 🔢 **{res}** is a random number from  **{num1}** to **{num2}**.")

  