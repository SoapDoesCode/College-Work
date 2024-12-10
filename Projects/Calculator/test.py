# def is_number(value):
#     try:
#         float(value)
#         return True
#     except:
#         return False
    
# print(is_number("1."))

from discord.ext import commands
import discord
import random


print("discord successfully imported!")

BOT_TOKEN = "TOKEN"

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("SHOWTIME!")

@client.command()
async def say(ctx, *, user_message):
    await ctx.send(user_message) # sends message without mention

@client.command()
async def reply(ctx, *, user_message):
    await ctx.respond(user_message) # sends message in the discord reply format

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    await client.process_commands(message)

    if "hello" in message.content: # message.content is just the message text
        greetings = ["Hello!", "Hi", "hey", "hello there"]
        greeting = random.choice(greetings)
        await message.channel.send(f"{greeting}, <@{message.author.id}>")


client.run(BOT_TOKEN)