import discord
import requests


@commands.command(name='ds', aliases=['status', 'dstatus'])
async def discordstatus(self, ctx):
    async with ctx.channel.typing():
        await ctx.send('Пожалуйста подождите...', delete_after=5)
        ret = requests.get('https://status.discordapp.com/index.json')
        rec = json.loads(ret.text)
        color = 0x000000
        if rec['status']['description'] == "Все системы в рабочем состоянии":
            color = 0x00D800
        else:
            color = 0xAA00AA
        embed = discord.Embed(title=rec['status']['description'], colour=color,
                              description='Данные получены из [Discord\'s status](https://status.discordapp.com/index.json).')
        if rec["components"][0]["status"] == "operational":
            embed.add_field(name="API", value="Отлично", inline=True)
        else:
            embed.add_field(name="API", value='Не работает', inline=True)
        if rec["components"][1]["status"] == "operational":
            embed.add_field(name="Шлюз", value='Отлично', inline=True)
        else:
            embed.add_field(name="Шлюз", value='Не работает', inline=True)
        if rec["components"][2]["status"] == "operational":
            embed.add_field(name="CloudFlare", value='Отлично', inline=True)
        else:
            embed.add_field(name="CloudFlare", value='Не работает', inline=True)
        if rec["components"][3]["status"] == "operational":
            embed.add_field(name="Медиа прокси", value='Отлично', inline=True)
        else:
            embed.add_field(name="Шлюз", value='Не работает', inline=True)
        if rec["components"][3]["status"] == "operational":
            embed.add_field(name="Голосовые серверы", value='Отлично', inline=True)
        else:
            embed.add_field(name="Шлюз", value='Не работает', inline=True)
    await ctx.send(embed=embed)