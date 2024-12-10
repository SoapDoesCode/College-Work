import discord
from discord.ext import commands
import asyncio
import os

# Set up the client and command prefix
intents = discord.Intents.all()
client = commands.Bot(prefix='!', intents=intents)

my_name = "Soph"
message_load_count = 10

invis_map = {
    "0": "\u200b",  # Zero Width Space
    "1": "\u200c",  # Zero Width Non-Joiner
    "2": "\u200d",
    "3": "\uFEFF"
}

# Reverse the invis_map for decoding
reverse_map = {v: k for k, v in invis_map.items()}

def encode_text_base4(text: str) -> str:
    # Convert text to binary and then to base-4
    binary = ''.join(format(ord(char), '08b') for char in text)
    base4 = ''.join(str(int(binary[i:i+2], 2)) for i in range(0, len(binary), 2))
    # Map base-4 digits to invisible characters
    encoded = ''.join(invis_map[digit] for digit in base4)
    return encoded

def decode_text_base4(encoded: str) -> str:
    try:
        # Map invisible characters back to base-4 digits
        base4 = ''.join(reverse_map[char] for char in encoded)
        # Convert base-4 digits back to binary
        binary = ''.join(format(int(digit), '02b') for digit in base4)
        # Convert binary to ASCII
        ascii_text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    except:
        ascii_text = encoded  # If decoding fails, return the encoded string as is
    return ascii_text

def encode_text_base2(text: str) -> str:
    binary = ''.join(format(ord(char), '08b') for char in text)  # Continuous binary
    for key, value in invis_map.items():
        binary = binary.replace(key, value)
    return binary

def decode_text_base2(binary: str) -> str:
    for key, value in invis_map.items():
        binary = binary.replace(value, key)

    try:
        # Process every 8 characters (1 byte) as a binary number
        ascii = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    except ValueError:
        ascii = binary  # If decoding fails, return the binary string as is
    return ascii

print(decode_text_base2("010001000110100101100100001000000111100101101111011101010010000001101000011001010110000101110010001000000110000101100010011011110111010101110100001000000111010001101000011001010010000001101101011011110110111001101011011001010111100101110011001000000111011101101000011011110010000001110011011010000110000101110010011001010110010000100000011000010110111000100000010000010110110101100001011110100110111101101110001000000110000101100011011000110110111101110101011011100111010000100000010101000110100001100101011110010010000001110111011001010111001001100101001000000101000001110010011010010110110101100101001000000110110101100001011101000110010101110011"))

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
            user_input = encode_text_base4(f"{my_name}: {user_input}")
            if len(user_input) <= 2000:
                await bypass_channel.send(f"{user_input}")
            else:
                print(f"Your message exceeded the 2000 character limit with: {len(user_input)} characters")
            await asyncio.sleep(0)  # Let the event loop continue

@client.event
async def on_ready():
    print(f"{client.user} online!")
    # Run term_user and the bot concurrently
    refresh_terminal()
    asyncio.create_task(term_user())  # Schedule term_user as a background task

@client.event
async def on_message(message):
    message_text = decode_text_base4(message.content)
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

# from bot_token import TOKEN

# client.run(TOKEN)