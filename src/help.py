import discord
from discord.ext import commands
from discord import ui
from config.prefix import DEFAULT_PREFIX
import json
import os

PREFIX_FILE = "data/prefixes.json"


# -------------------------
# Prefix Helpers
# -------------------------
def get_server_prefix(guild_id: int | None):
    """Get server prefix from JSON or fallback to default."""
    if guild_id is None:
        return DEFAULT_PREFIX

    if not os.path.exists(PREFIX_FILE):
        return DEFAULT_PREFIX

    try:
        with open(PREFIX_FILE, "r", encoding="utf-8") as f:
            prefixes = json.load(f)
    except (json.JSONDecodeError, OSError):
        return DEFAULT_PREFIX

    return prefixes.get(str(guild_id), DEFAULT_PREFIX)


# -------------------------
# Command Categories
# -------------------------
CUSTOM_COMMANDS = {
    "General": [
        ("ping", "Check bot latency."),
        ("help", "Show this help menu.")
    ],
    "Config": [
        ("setprefix <prefix>", "Change the server prefix."),
    	("setlog <#channel>", "Set the log channel."),
    	("setwelcome <#channel>", "Set the welcome channel."),
    	("setleave <#channel>", "Set the leave channel."),
    	("setautorole <role>", "Set the autorole.")
	],
    "Moderation": [
        ("nuke", "Nuke the current channel safely."),
        ("mute <time> <@user> <reason>", "Mute a user."),
        ("unmute <@user> <reason>", "Manually unmute a member."),
        ("warn <@user>", "Warn a user and save it."),
        ("warnings <@user>", "Check a user's warnings."),
        ("clearwarns <@user>", "Clear a user's warnings.")
    ],
    "Admin": [
        ("kick <@user> <reason>", "Kick a member from the server."),
        ("ban <@user> <reason>", "Ban a member from the server."),
        ("serverban <user_id> <reason>", "Ban a user by ID."),
        ("forcekick <user_id> <reason>", "Kick a user by ID."),
        ("unban <user_id>", "Unban a user by ID."),
        ("lock", "Lock the current channel."),
        ("unlock", "Unlock the current channel."),
        ("slowmode <seconds>", "Set slowmode for the channel."),
        ("setnick <@user> <nickname>", "Change a member's nickname."),
        ("nickname <nickname>", "Change your own nickname."),
        ("announce <message>", "Send an announcement embed."),
        ("purge <amount>", "Delete a number of messages."),
        ("roleadd <@user> <role>", "Give a role to a member."),
        ("roleremove <@user> <role>", "Remove a role from a member."),
        ("dm <@user> <message>", "Send a DM to a member."),
        ("dmall <message>", "Send a DM to all members."),
        ("delchannels", "Delete all channels in the server (Owner only)."),
        ("forcenick <@user> <nickname>", "Force change a member's nickname (admin only).")
    ],
    "BlackList (Bot Owner Only)": [
        ("blacklist_user <@user>", "Add a user to the global blacklist."),
        ("unblacklist_user <@user>", "Remove a user from the global blacklist."),
        ("list_blacklisted_users", "List all blacklisted users."),
        ("blacklist_server <guild_id>", "Add a server to the global blacklist."),
        ("unblacklist_server <guild_id>", "Remove a server from the global blacklist."),
        ("list_blacklisted_servers", "List all blacklisted servers.")
    ],
    "Word": [
        ("setroleword <word> <role>", "Assign a role when a word is said."),
        ("delroleword <word>", "Remove a role-word."),
        ("listrolewords", "Show all role-word configs."),
        ("setdetectword <word> <response>", "Send a custom embed whenever a word is typed."),
        ("deldetectword <word>", "Remove a detect-word."),
        ("listdetectwords", "Show all detect-word configs.")
    ],
    "Word (No Embed)": [
        ("setroleword_plain <word> <role>", "Assign a role when a word is said without embeds."),
        ("delroleword_plain <word>", "Remove a role-word without embeds."),
        ("listrolewords_plain", "Show all role-word configs without embeds."),
        ("setdetectword_plain <word> <response>", "Send a plain message whenever a word is typed."),
        ("deldetectword_plain <word>", "Remove a detect-word without embeds."),
        ("listdetectwords_plain", "Show all detect-word configs without embeds.")
    ],
    "Economy": [
        ("balance / bal", "Check your coin balance."),
        ("daily", "Claim your daily PhaseCoins reward."),
        ("work", "Earn random PhaseCoins."),
        ("inventory / inv", "View your items inventory."),
        ("leaderboard / lb", "See the richest users."),
        ("shop", "View the server shop."),
        ("buy <item>", "Buy an item from the shop."),
        ("ecogive <@user> <amount>", "Give coins to a user (Admin only)."),
        ("ecoset <@user> <amount>", "Set a user's balance (Admin only)."),
        ("ecorem <@user> <amount>", "Remove coins from a user (Admin only)."),
        ("additem <name> <price>", "Add an item to the shop (Admin only)."),
        ("removeitem <name>", "Remove an item from the shop (Admin only).")
    ],
    "Casino": [
        ("slots <amount>", "Spin the slots."),
        ("coinflip <amount> <heads/tails>", "Flip a coin."),
        ("blackjack <amount>", "Play blackjack against the dealer.")
    ],
    "Verify": [
        ("verify_setup <@role> <#log>", "Set the verify role and log channel."),
        ("verify_panel", "Show the verify panel.")
    ],
	"Ticket": [
    	("ticket_setup <@role> <#log>", "Setup the ticket system."),
    	("ticket_panel", "Send the create-ticket panel."),
    	("ticket_buttons", "Send ticket control buttons in a ticket."),
    	("ticket_id", "Show the custom ticket ID."),
    	("transcript", "Export the current ticket transcript."),
    	("close", "Delete the current ticket and save transcript."),
    	("add <@user>", "Add a user to the ticket."),
        ("remove <@user>", "Remove a user from the ticket.")
	],
    "Logs": [
    	("auto", "Logs message delete/edit/join/leave.")
	],
    "afk": [
    	("afk [reason]", "Set yourself as AFK.")
	]
}


# -------------------------
# Embed Builder
# -------------------------
def build_help_embed(category: str, prefix: str):
    commands_list = CUSTOM_COMMANDS.get(category, [])

    embed = discord.Embed(
        title=f"📘 {category} Commands",
        description=f"Prefix for this server: `{prefix}`",
        color=discord.Color.blurple()
    )

    if not commands_list:
        embed.add_field(
            name="No commands found",
            value="This category is currently empty.",
            inline=False
        )
        return embed

    for cmd_name, desc in commands_list:
        embed.add_field(
            name=f"{prefix}{cmd_name}",
            value=desc,
            inline=False
        )

    embed.set_footer(text=f"{len(commands_list)} command(s) in this category")
    return embed


# -------------------------
# Dropdown Menu
# -------------------------
class HelpDropdown(ui.Select):
    def __init__(self, author_id: int):
        self.author_id = author_id

        options = [
            discord.SelectOption(
                label=category[:100],
                description=f"View commands in {category}"[:100]
            )
            for category in CUSTOM_COMMANDS.keys()
        ]

        super().__init__(
            placeholder="Select a command category...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.author_id:
            await interaction.response.send_message(
                "❌ You cannot use someone else's help menu.",
                ephemeral=True
            )
            return

        category = self.values[0]
        prefix = get_server_prefix(interaction.guild.id if interaction.guild else None)
        embed = build_help_embed(category, prefix)

        await interaction.response.edit_message(embed=embed, view=self.view)


class HelpView(ui.View):
    def __init__(self, author_id: int):
        super().__init__(timeout=120)
        self.add_item(HelpDropdown(author_id))

    async def on_timeout(self):
        for item in self.children:
            item.disabled = True


# -------------------------
# Help Cog
# -------------------------
class Help(commands.Cog):
    """Custom help command with categories and dropdown menu."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help_command(self, ctx):
        prefix = get_server_prefix(ctx.guild.id if ctx.guild else None)

        embed = discord.Embed(
            title="📜 PhaseBot Help Menu",
            description=(
                "Use the dropdown below to view command categories.\n"
                f"Current prefix: `{prefix}`"
            ),
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="Available Categories",
            value="\n".join([f"• {name}" for name in CUSTOM_COMMANDS.keys()]),
            inline=False
        )

        if ctx.guild and ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
            embed.set_author(name=ctx.guild.name)

        embed.set_footer(text="Made by PhaseDev")

        view = HelpView(ctx.author.id)
        await ctx.send(embed=embed, view=view)


# -------------------------
# Setup
# -------------------------
async def setup(bot):
    await bot.add_cog(Help(bot))