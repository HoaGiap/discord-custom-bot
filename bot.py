import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#HoaGiap
# Khởi tạo bot với prefix và intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Sự kiện khi bot sẵn sàng
@bot.event
async def on_ready():
    print(f'Bot đã sẵn sàng: {bot.user}')
    # Tải tất cả cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Đã tải cog: {filename[:-3]}')
            except Exception as e:
                print(f'Lỗi khi tải cog {filename[:-3]}: {e}')

# Lệnh /hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Xin chào, {ctx.author.mention}!')

# Lệnh /info
@bot.command()
async def info(ctx):
    await ctx.send(f'Tên bot: {bot.user.name}\nServer: {ctx.guild.name}')

# Chạy bot
bot.run(TOKEN)