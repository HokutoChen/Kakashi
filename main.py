import os
from discord.ext import commands

import credentials

bot = commands.AutoShardedBot(commands.when_mentioned_or(","))

@bot.event
async def on_ready():
    print("Im starting cog loading process ya fuck.")
    for cog in os.listdir("./cogs"):
        if cog.endswith(".py"):
            try:
                bot.load_extension(f"cogs.{cog[:-3]}")
                print(f"Loaded cog: {cog}")
            except Exception as e:
                print(f"The fuck you do? I can't load {cog}\nError: {e}")
    print("Finished")
    print("Ready!")



@bot.command()
async def hello(ctx: commands.Context):
    await ctx.send(f"The fuck you want")


bot.run(credentials.token)
