import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Concexion Exitosa :D')
    print('Nombre del Bot: ',client.user.name)
    print('Numero del ID: ',client.user.id)
    print('----------')

@client.event
async def on_message(message):

    if(message.author.bot): return

    if (message.content == '*help') :
        await client.send_message(message.channel,'------------------------------------------------------------------------------------------------',embed=None)
        em = discord.Embed(title='Comandos', description='Necesitas saber todos los conmando de este bot aqui esta la ayuda todo sobre acerca del bot.\n\n*gi - Quieres mandar un buen GIF entonces usa este genial comando.\n*imga - La necesidad de una imagen es genial.\n*tro - No pos este es un test\n*rand - Un numero random.\n*randpa - Oraciones o palabras random.', colour= 0x5495ff)
        em.set_author(name='')
        await client.send_message(message.channel, embed=em)
        await client.send_message(message.channel,'------------------------------------------------------------------------------------------------',embed=None)

    if(message.content == 'beep'):
        await client.send_message(message.channel,'boop')

    if(message.content == 'boop'):
        await client.send_message(message.channel,'beep')

    if(message.content == '*rand'):
        await client.send_message(message.channel, random.randint(100, 999))

    if(message.content == '*randpa'):
        await client.send_message(message.channel, random.choice(['Te amo','Te odio','La verdad es dura como la verdura','Aqui algo me huele mal','La vida es una lenteja o la tomas o la dejas',':D',':(']))

client.run('NDkzNjIwMjQzNDQ5Nzc0MDgx.DossQg.7_DmTGAe2HcFdc3JXoZeSrRrgpM')