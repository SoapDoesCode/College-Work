import discord
from discord.ext import commands
import asyncio
import os

# Set up the client and command prefix
intents = discord.Intents.all()
client = commands.Bot(prefix='!', intents=intents)

my_name = "Soph"
message_load_count = 10

def cache_message(message):
    with open("message_cache.txt", 'a', encoding='utf-8') as file:
        file.write(message)
    file.close()

def read_cache(num_messages):
    with open("message_cache.txt", 'r', encoding='utf-8') as file:
        data = "".join(file.readlines()[-num_messages:])
        # print(data)
        file.close()
    return data

def clear():
    os.system("cls")

def refresh_terminal():
    clear()
    cached_messages = read_cache(message_load_count)
    print(cached_messages)

async def term_user():
    global bypass_channel
    bypass_channel = client.get_channel(1293936472554209371) # Bi-Pass
    # bypass_channel = client.get_channel(1293936397165658247) # General
    while True:
        user_input = await asyncio.to_thread(input) # Run input in a non-blocking way
        if user_input != "":
            user_input = f"{my_name}: {user_input}"
            await bypass_channel.send(f"{user_input}")
            await asyncio.sleep(0)  # Let the event loop continue

@client.event
async def on_ready():
    print(f"{client.user} online!")
    # Run term_user and the bot concurrently
    refresh_terminal()
    asyncio.create_task(term_user())  # Schedule term_user as a background task

@client.event
async def on_message(message):
    message_text = message.content
    if not message_text.startswith(f"{my_name}:") or ": " not in message_text:
        message_text = f"{message.author.display_name}: {message_text}"

    message_text = f"[{message.channel}] {message_text}\n"

    cache_message(message_text)
    refresh_terminal()

    await client.process_commands(message)

@client.event
async def on_raw_reaction_add(payload):
    cache_message(f"{payload.member.display_name} reacted with {payload.emoji}\n")

@client.event
async def on_raw_reaction_remove(payload):
    cache_message(f"{payload.member.display_name} reacted with {payload.emoji}\n")

from bot_token import TOKEN

client.run(TOKEN)
