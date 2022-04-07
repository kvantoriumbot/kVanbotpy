import discord
from discord.ext import commands
import asyncio
import colorama
import pyowm
import random
import aiohttp
import datetime
import pyfiglet
from aiohttp import ClientSession
import discord
import requests
from discord.ext import commands
import random
import os
import asyncio
import json
import io
import contextlib
import datetime
import cogs


ascii_banner = pyfiglet.figlet_format ( "Kvantum Bot" )
print ( ascii_banner )

client = commands.Bot ( command_prefix='K.' )

token = ''
@client.event
async def on_ready() :
    print ( f'Logged in as: {client.user.name}' )
    print ( f'With ID: {client.user.id}' )


from io import BytesIO
from PIL import Image


def pixel_img(image, pixel_size=10) :
    image = image.resize ( (image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST )
    image = image.resize ( (image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST )
    return image


import discord
from discord import utils
from discord.ext import commands

@client.command()
async def cat(ctx):
    await ctx.send("https://cataas.com/cat")


@client.command ( )
async def pixava(ctx) :
    image = pixel_img (
        Image.open ( BytesIO ( await ctx.author.avatar_url_as ( format='png' ).read ( ) ) ).convert ( 'RGBA' ) )
    output = BytesIO ( )
    image.save ( output, 'png' )
    image_pix = BytesIO ( output.getvalue ( ) )
    await ctx.send ( file=discord.File ( fp=image_pix, filename='pix_ava.png' ) )


@client.command ( name="ping",
                  description="Возращает скорость ответа бота",
                  )
async def ping(ctx) :
    await ctx.send ( 'Понг! Мой Пинг - {0}'.format ( round ( client.latency, 1 ) ) )

@client.event
async def on_message(message) :
    if message.content == "profile" :
        user = message.author.id
        print ( user )
        embed = discord.Embed ( title="Profile", description="Your Profile" )
        embed.add_field ( name="Username:", value=f"{message.author}", inline=True )
        embed.add_field ( name="Id:", value=f"{message.author.id}", inline=True )
        await message.channel.send ( content=None, embed=embed )


import random


@client.event
async def on_message(msg) :
    if random.randint ( 1, 10 ) == 10 :
        await msg.add_reaction ( random.choice ( [emoji for i in client.guilds for emoji in i.emojis] ) )
    await client.process_commands ( msg )


@client.event
async def on_ready() :
    guilds = await client.fetch_guilds ( limit=None ).flatten ( )
    await client.change_presence ( status=discord.Status.idle,
                                   activity=discord.Activity ( name=f'за {len ( guilds )} серверами.',
                                                               type=discord.ActivityType.watching ) )


@client.event
async def on_guild_join() :
    guilds = await client.fetch_guilds ( limit=None ).flatten ( )
    await client.change_presence ( status=discord.Status.idle,
                                   activity=discord.Activity ( name=f'за {len ( guilds )} серверами.',
                                                               type=discord.ActivityType.watching ) )


@client.event
async def on_member_ban(guild, user) :
    print ( guild, user )


@client.command ( )
async def hack(ctx) :
    await ctx.send ( "Хаха, ты взломал себя а не нас!" )
    await ctx.send ( "https://cdn.discordapp.com/attachments/829372012002017333/831890466022227988/9pD_m9LRoN4.jpg" )
    print ( f'[log Command] Была исользована команда - K.hack он мог нас взломать, использовал: {ctx.author}\n' )


@client.event
async def on_member_kick(gulid, user) :
    print ( gulid, user )


@client.event
async def on_guild_join(guild) :
    print ( f'''
{Fore.YELLOW}
==============================================
{Style.RESET_ALL}
[GUILD]   Бот присоединился к серверу!
[GUILD]   Информация о сервере
{Fore.YELLOW}
==============================================
{Style.RESET_ALL}
[GUILD]  Сервер           - {guild.name}
[GUILD]  Владелец сервера - {guild.owner}
[GUILD]  ID бота          - {guild.id}
{Fore.YELLOW}
==============================================
{Style.RESET_ALL}
    ''' )
    embed = discord.Embed ( title='Kvantum BOT',
                            description=f"Добрый день!\n\n Вы получили это сообщение т.к на ваш сервер {guild.name} был добавлен Kvantum Бот.\nЭто информативное сообщение, сделанное для того, чтобы вы знали немного больше о том, чем пользуетесь.",
                            color=0x800080 )
    embed.add_field ( name="Полезная информация:",
                      value=f"Этот бот был создан Арсением Лихвчевым, ITkvant Учитель: Даниил Чикмарёв" )
    embed.set_footer ( text='Kvantum BOT', icon_url=client.user.avatar_url )

    await guild.owner.send ( embed=embed )

    getChannel = client.get_channel ( 777870411810603033 )

    j_e = discord.Embed ( title=f"Бот присоединился к серверу {guild.name}",
                          description=f"Информация о сервере:\n\nСервер - {guild.name}\nID сервера - {guild.id}\nВладелец сервера - {guild.owner}",
                          color=0x800080 )

    await getChannel.send ( embed=j_e )


@client.command ( )
@commands.has_permissions ( administrator=True )
async def kick(ctx, member: discord.Member = None, reason=None) :
    if member is None :

        await ctx.send (
            embed=discord.Embed ( description='**:grey_exclamation: Обязательно укажите: пользователя!**' ) )

    elif reason is None :

        await ctx.send ( embed=discord.Embed ( description='**:grey_exclamation: Обязательно укажите: причину!**' ) )

    else :

        await member.kick ( reason=reason )
        await ctx.send ( embed=discord.Embed (
            description=f'**:shield: Пользователь {member.mention} был исключен.\n:book: По причине: {reason}**',
            color=0x0c0c0c ) )


# Unban

@client.command ( pass_context=True )
@commands.has_permissions ( administrator=True )
async def unban(ctx, *, member: discord.Member) :
    banned = await ctx.guild.bans ( )

    author = ctx.author.mention

    for entry in banned :

        user = entry.user

        user = user.mention

        if user == member :
            await ctx.guild.unban ( user )

            emb = discord.Embed ( title='K.unban', description=f"{author} Имеет UNBAN {user}",
                                  colour=discord.Color.green ( ) )

            await ctx.send ( embed=emb )

            break


@client.command ( )
@commands.has_permissions ( administrator=True )
async def ban(ctx, member: discord.Member = None, reason=None) :
    if member is None :

        await ctx.send (
            embed=discord.Embed ( description='**:grey_exclamation: Обязательно укажите: пользователя!**' ) )

    elif reason is None :

        await ctx.send ( embed=discord.Embed ( description='**:grey_exclamation: Обязательно укажите: причину!**' ) )

    else :

        channel_log = client.get_channel ( 703653241027821658 )  # Айди канала логов

        await member.ban ( reason=reason )
        await ctx.send ( embed=discord.Embed (
            description=f'**:shield: Пользователь {member.mention} был заблокирован.\n:book: По причине: {reason}**',
            color=0x0c0c0c ) )
        await channel_log.send ( embed=discord.Embed (
            description=f'**:shield: Пользователь {member.mention} был заблокирован.\n:book: По причине: {reason}**',
            color=0x0c0c0c ) )


var = ban.error


async def ban_error(ctx, error) :
    if isinstance ( error, commands.MissingPermissions ) :
        await ctx.send ( embed=discord.Embed (
            description=f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**',
            color=0x0c0c0c ) )


@kick.error
async def kick_error(ctx, error) :
    if isinstance ( error, commands.MissingPermissions ) :
        await ctx.send ( embed=discord.Embed (
            description=f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**',
            color=0x0c0c0c ) )


# commands
@client.command ( )
async def commmand_name() :
    pass


@client.command (
    aliases=['Say', 'Сказать', 'сказать', 'Скажи', 'скажи', 'SAY', 'СКАЗАТЬ', 'СКАЖИ', 'Вывести', 'вывести', 'ВЫВЕСТИ',
             'Выведи', 'выведи', 'ВЫВЕДИ'] )
@commands.has_permissions ( administrator=True )
async def say(ctx, *, arg=None) :
    if arg is None :
        await ctx.send ( embed=discord.Embed ( title="Не бузи!",
                                               description=f":x: {ctx.author.mention}, укажи сообщение, которое хочешь отправить от именни бота :x:",
                                               color=0xFF0000 ) )
    else :
        await ctx.message.delete ( )
        embed = discord.Embed ( description=f'{arg}', color=0xa43dd8 )
        embed.set_footer ( text=f'{client.user.name} © 2030 | Все права защищены', icon_url=client.user.avatar_url )
        await ctx.send ( embed=embed )

        print ( f'[log Command] Была исользована команда - >say. Использовал - Администратор: {ctx.author}\n' )


@client.command ( name='weather', aliases=['погода'] )
async def weather(ctx, city: str = None) :
    if not city :
        await ctx.send ( embed=discord.Embed ( description="**Ты не указал город -_-**",
                                               colour=discord.Color.from_rgb ( 47, 49, 54 ) ) )
        await ctx.message.add_reaction ( "🔴" )
    else :
        owm = pyowm.OWM ( '520cc15a2a769ee8bff41ecafe75e412' )
        mgr = owm.weather_manager ( )
        observation = mgr.weather_at_place ( city )
        w = observation.weather
        temp = w.temperature ( 'celsius' )["temp"]
        temp_max = w.temperature ( 'celsius' )["temp_max"]
        temp_min = w.temperature ( 'celsius' )["temp_min"]
        feels_like = w.temperature ( 'celsius' )["feels_like"]

        embed = discord.Embed (
            colour=discord.Color.from_rgb ( 47, 49, 54 ),
            description=f"**Погода в городе {city}**",
            timestamp=ctx.message.created_at
        )
        embed.set_thumbnail (
            url="https://avatars.mds.yandex.net/get-pdb/752643/d215f5fe-77ec-4923-aea7-b2184f2b6598/orig" )
        embed.add_field ( name="Температура", value=f"{temp} °С" )
        embed.add_field ( name="Ощущается как", value=f"{feels_like} °С" )
        embed.add_field ( name="Максимальная температура", value=f"{temp_max} °С" )
        embed.add_field ( name="Минимальная температура", value=f"{temp} °С" )
        await ctx.send ( embed=embed )
        await ctx.message.add_reaction ( "🟢" )


@client.event
async def on_message(msg) :
    print ( msg.content )
    if msg.content == f'<@!{client.user.id}>' or msg.content == f'<@{client.user.id}>' :
        await msg.channel.send ( 'Привет,я Kvantum БОТ Сделан в кванториуме Мой префикс K.' )
        return
    await client.process_commands ( msg )


# Очистка чата
@client.command ( )
@commands.has_permissions ( administrator=True )
async def clear(ctx, amount: int) :
    await ctx.channel.purge ( limit=amount )
    await ctx.send (
        embed=discord.Embed ( description=f'**:heavy_check_mark: Удалено {amount} сообщений.**', color=0x0c0c0c ) )


# Работа с ошибками очистки чата

@clear.error
async def clear_error(ctx, error) :
    if isinstance ( error, commands.MissingPermissions ) :
        await ctx.send ( embed=discord.Embed (
            description=f'**:exclamation: {ctx.author.name},у вас нет прав для использования данной команды.**',
            color=0x0c0c0c ) )

    if isinstance ( error, commands.MissingRequiredArgument ) :
        await ctx.send ( embed=discord.Embed (
            description=f'**:grey_exclamation: {ctx.author.name},обязательно укажите количевство сообщений.**',
            color=0x0c0c0c ) )


@client.command ( )
async def userinfo(ctx, Member: discord.Member = None) :
    if not Member :
        Member = ctx.author
    roles = (role for role in Member.roles)
    emb = discord.Embed ( title='Информация о пользователе.'.format ( Member.name ),
                          description=f"Участник зашёл на сервер: {Member.joined_at.strftime ( '%b %#d, %Y' )}\n\n "
                                      f"Имя: {Member.name}\n\n"
                                      f"Никнейм: {Member.nick}\n\n"
                                      f"Статус: {Member.status}\n\n"
                                      f"ID: {Member.id}\n\n"
                                      f"Высшая роль: {Member.top_role}\n\n"
                                      f"Аккаунт создан: {Member.created_at.strftime ( '%b %#d, %Y' )}",
                          color=0xff0000, timestamp=ctx.message.created_at )

    emb.set_thumbnail ( url=Member.avatar_url )
    emb.set_footer ( icon_url=Member.avatar_url )
    emb.set_footer ( text='Команда вызвана: {}'.format ( ctx.author.name ), icon_url=ctx.author.avatar_url )
    await ctx.send ( embed=emb )


@client.command ( )
async def serverinfo(ctx, member: discord.Member = None) :
    if not member :
        member = ctx.author

    guild = ctx.guild
    embed = discord.Embed ( title=f"{guild.name}",
                            description=f"Сервер создали {guild.created_at.strftime ( '%b %#d, %Y' )}\n\n"
                                        f"Регион {guild.region}\n\nГлава сервера {guild.owner}\n\n"
                                        f"Людей и ботов на сервере {guild.member_count}\n\n", color=0xff0000,
                            timestamp=ctx.message.created_at )

    embed.set_thumbnail ( url=ctx.guild.icon_url )
    embed.set_footer ( text=f"ID: {guild.id}" )

    embed.set_footer ( text=f"ID Пользователя: {ctx.author.id}" )
    await ctx.send ( embed=embed )


@client.command ( )
async def coin(ctx) :
    choices = ['орел', 'решка', 'монетка упала ребром']
    color = discord.Color.green ( )
    emb = discord.Embed ( color=color, title='Подбрасывание:', description=random.choice ( choices ) )
    await ctx.send ( embed=emb )


@weather.error
async def weather_error(ctx, error) :
    if isinstance ( error, commands.CommandInvokeError ) :
        await ctx.send ( embed=discord.Embed (
            colour=discord.Color.from_rgb ( 47, 49, 54 ),
            description=f"**Город не найден**"
        ) )
        await ctx.message.add_reaction ( "🔴" )


@say.error
async def mine_error(ctx, error) :
    if isinstance ( error, commands.CheckFailure ) :
        e = discord.Embed ( title='Не бузи!', color=0xFF0000 )
        e.description = f':x: {ctx.author.mention}, у тебя нет прав, что-бы использовать эту команду! :x:'
        await ctx.send ( embed=e )
    else :
        raise error

@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []

    top = subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    embed = discord.Embed(title = name, color=discord.Color.gold())
    embed.set_image(url = url)
    embed.set_footer(text=f"Asked by {ctx.author.name}")

    await ctx.send(embed=embed)


@client.command ( pass_context=True )
@commands.has_permissions ( administrator=True )
async def dmall(ctx, message=None) :
    await ctx.message.delete ( )
    if message is not None :
        members = ctx.guild.members
        for member in members :
            try :
                await member.send ( message )
                print ( "'" + message + "' Отправлено к:" + member.name )

            except :
                print ( "Не могу отправит: '" + message + "' к: " + member.name )
    else :
        ctx.send ( "Ты забыл написать сообщение!" )


@client.event
async def on_command_error(ctx, error) :
    if isinstance ( error, commands.CommandNotFound ) :
        await ctx.send ( "***Данной команды нету или ты неправильно написал***" )


client.run ( token )
