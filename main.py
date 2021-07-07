import credentials

from discord.ext import commands

bot = commands.AutoShardedBot(commands.when_mentioned_or("gay"))

@bot.event
async def on_ready():
    print("you gay")

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"tyler senpai {round(bot.latency * 1000)}ms")


bot.run(credentials.token)