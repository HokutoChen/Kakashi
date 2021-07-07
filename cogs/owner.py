import discord

from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx: commands.Context, cog):
        try:
            self.bot.load_extension(cog)
            await ctx.message.add_reaction("\u2705")
            await ctx.send(f"Loaded `{cog}`")
        except commands.ExtensionError as e:
            await ctx.message.add_reaction(":x:")
            await ctx.send(f"Failed to load `{cog}`\nReason: `{e}`")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, cog):
        try:
            self.bot.reload_extension(cog)
            await ctx.message.add_reaction("\u2705")
            await ctx.send(f"Reloaded `{cog}`")
        except commands.ExtensionError as e:
            await ctx.message.add_reaction(":x:")
            await ctx.send(f"Failed to reload `{cog}`\nReason: `{e}`")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, cog):
        try:
            self.bot.unload_extension(cog)
            await ctx.message.add_reaction("\u2705")
            await ctx.send(f"Unloaded `{cog}`")
        except commands.ExtensionError as e:
            await ctx.message.add_reaction(":x:")
            await ctx.send(f"Failed to unload {cog}\nReason: {e}")


def setup(bot: commands.AutoShardedBot):
    bot.add_cog(Owner(bot))
