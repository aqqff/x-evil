import discord
from discord.ext import commands
intents=discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True)



bot=commands.Bot(">>",intents=intents)
@bot.event
async def on_ready():
	print('i ready')
@bot.event

async def on_member_join(member):
	channel=discord.utils.get(member.guild.text_channels,name="chat")
	await channel.send(f"{member} welcome my server.")
@bot.event
async def on_member_remove(member):
	channel=discord.utils.get(member.guild.text_channels,name="try")
	await channel.send(f"{member} goodbye.")
@bot.command()
async def kick(ctx,member:discord.Member,*args, reason="..."):
	await member.kick()
@bot.command()
async def ban(ctx,member:discord.Member,*args, reason="..."):
	await member.ban()
@bot.command()
async def unban(ctx,*,member):
	banned_users=await ctx.guild.bans()
	member_name, member_discriminator=member.split("#")
	for bans in banned_users:
		user=bans.user
		if(user.name,user.discriminator)==(member_name,member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'unbanned user {user.mantion}')
			return
@bot.command()
async def hello(msg):
	await msg.send("hello")
bot.run('OTY2MzA1Mzk3NDU3NjgyNDYy.Yl_0Bw.DNPSYkcSPpUTDDgBVFtMxrKNFLs')


