import os
import discord
#from dotenv import load_dotenv
from discord import app_commands

# load_dotenv()
#botToken = os.getenv("DISCORD_BOT_TOKEN")

guild = discord.Object(id=int(os.environ["DISCORD_GUILD_ID"]))

class TestBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync(guild=guild)

bot = TestBot()

@bot.tree.command(name="ping", description="봇 연결 확인", guild=guild)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")

bot.run(os.environ["DISCORD_BOT_TOKEN"])