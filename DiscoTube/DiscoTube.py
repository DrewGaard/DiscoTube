import discord
from bs4 import BeautifulSoup as bs
import requests

client = discord.Client()

base = "https://www.youtube.com/results?search_query="

@client.event
async def on_ready():
    print("GET READY TO DISCO")
    await client.change_presence(activity = discord.Game(name = "Disco Dancing"))
##  await bot.join_voice_channel(DiscoTube)


@client.event
async def on_message(message):
    if message.author == client.user:
          return
    if message.content.startswith('!'):
        print("! Detected")
        if message.content == "rickroll":
            print("rickroll detected")
            await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        r = requests.get(base+message.content)
        page = r.text
        soup = bs(page, 'html.parser')
        vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
        videolist=[]
        for v in vids:
            tmp = 'https://www.youtube.com' + v['href']
            videolist.append(tmp)
        await message.channel.send(videolist[0])
##        if (message.channel.voice.channel):
##            print("Joined voice channel")
##            connection = await message.channel.voice.channel.join()
    else:
        print("No ! Detected")
        return


client.run("NTgzNDk1NDQ5OTY1NzU2NDIy.XO9M2g.fhtnmfW6UCXiurOoFGuc-Kwo2xs")
