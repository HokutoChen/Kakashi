import discord
from discord.ext import commands

class First(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command(aliases=["p"])
    async def ping(self, ctx: commands.Context):
        """Ping command"""
        await ctx.send(
            embed=discord.Embed(
                title="Pong!",
                description=f"Latency: {round(self.bot.latency * 1000)} ms",
                color=discord.Color.green()
        )
        .set_thumbnail(url=self.bot.user.avatar.url)
        .set_footer(text=f"{self.bot.user.name} was created on {self.bot.user.created_at.strftime('%c')}")
        )

def setup(bot: commands.AutoShardedBot):
    bot.add_cog(First(bot))