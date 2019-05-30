import discord

client = discord.Client()

@client.event
async def on_ready():
    print("GET READY TO DISCO")
    await client.change_presence(activity = discord.Game(name = "Disco Dancing"))


@client.event
async def on_message(message):
    print("rickroll detected")
    if message.author == client.user:
          return
    if message.content == "rickroll":
          await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


client.run("NTgzNDk1NDQ5OTY1NzU2NDIy.XO9M2g.fhtnmfW6UCXiurOoFGuc-Kwo2xs")
