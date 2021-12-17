
import discord
from discord.ext import commands, tasks
from pathlib import Path


intents = discord.Intents.default()
intents.members = True

BOT_PREFIX = ('sudo ')
bot = commands.Bot(command_prefix=BOT_PREFIX, intents = intents)

@bot.event
async def on_ready():
	print (f"\nLogged in as:\t {str(bot.user)}")
	print ("-----------------")
	change_presence.start()

@tasks.loop(seconds = 3600)
async def change_presence():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="sudo help"))

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		embed = discord.Embed(description=f"○ Invalid command\n○ Type `sudo help` to know about each command.",colour=discord.Colour.red())
		await ctx.send(embed = embed)
		return

if __name__ == '__main__':
	res = Path("res")

	with open(res / "TOKEN", 'r') as TokenObj:
		TOKEN = TokenObj.read()

	cogs = [
		'cogs.admin.mod',
		'cogs.admin.admin_misc',
		'cogs.admin.info',
		'cogs.admin.src',
		'cogs.admin.announcement'
		]

	for cog in cogs:
		print ("Loading Cog:\t", cog, "...")
		bot.load_extension(cog)

	bot.run(TOKEN)