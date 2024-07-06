import discord
from discord.ext import commands, tasks
import random
import asyncio
from collections import defaultdict
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GAME_CHANNEL_ID = YOUR_CHANNEL_ID_HERE!

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)

characters = {
    "Miss Scarlett": "A young and beautiful femme fatale with a mysterious past.",
    "Colonel Mustard": "A dignified and retired military officer with a storied career.",
    "Mrs. White": "The long-serving housekeeper with a no-nonsense attitude.",
    "Reverend Green": "A charming yet suspiciously nervous reverend.",
    "Mrs. Peacock": "A wealthy socialite with a penchant for drama.",
    "Professor Plum": "A brilliant but absent-minded academic."
}

weapons = ["Revolver", "Dagger", "Lead Piping", "Rope", "Spanner", "Candlestick"]
rooms = {
    "Kitchen": "A modern kitchen with shiny appliances and a large island in the middle.",
    "Dining Room": "An elegant dining room with a long table set for a feast.",
    "Lounge": "A cozy lounge with a fireplace and comfortable seating.",
    "Hall": "A grand hall with a chandelier and a sweeping staircase.",
    "Study": "A quiet study filled with books and a large desk.",
    "Library": "A grand library with shelves of books and a reading nook.",
    "Billiard Room": "A room with a billiard table and sports memorabilia.",
    "Conservatory": "A bright conservatory filled with exotic plants.",
    "Ballroom": "A grand ballroom with a polished dance floor and large windows."
}

clues = {
    "Kitchen": {"suspect": "Mrs. White", "weapon": "Dagger", "room": "Kitchen"},
    "Dining Room": {"suspect": "Colonel Mustard", "weapon": "Revolver", "room": "Dining Room"},
    "Lounge": {"suspect": "Miss Scarlett", "weapon": "Candlestick", "room": "Lounge"},
    "Hall": {"suspect": "Reverend Green", "weapon": "Rope", "room": "Hall"},
    "Study": {"suspect": "Professor Plum", "weapon": "Lead Piping", "room": "Study"},
    "Library": {"suspect": "Mrs. Peacock", "weapon": "Spanner", "room": "Library"},
    "Billiard Room": {"suspect": "Miss Scarlett", "weapon": "Revolver", "room": "Billiard Room"},
    "Conservatory": {"suspect": "Colonel Mustard", "weapon": "Candlestick", "room": "Conservatory"},
    "Ballroom": {"suspect": "Mrs. Peacock", "weapon": "Dagger", "room": "Ballroom"}
}

murderer = random.choice(list(characters.keys()))
murder_weapon = random.choice(weapons)
crime_scene = random.choice(list(rooms.keys()))
discovered_clues = []
votes = defaultdict(int)

random_event_enabled = True

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    random_event.start()

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command(name='start_mystery')
async def start_mystery(ctx):
    global discovered_clues
    discovered_clues = []
    await ctx.send("**Welcome to the Murder Mystery game!** :tada:")
    await ctx.send(f"The victim was found in the **{crime_scene}**. Investigate to find out who did it, with what, and where.")
    
    character_descriptions = "\n".join([
        f"🔴 **Miss Scarlett**: {characters['Miss Scarlett']}",
        f"🟡 **Colonel Mustard**: {characters['Colonel Mustard']}",
        f"⚪ **Mrs. White**: {characters['Mrs. White']}",
        f"🟢 **Reverend Green**: {characters['Reverend Green']}",
        f"🔵 **Mrs. Peacock**: {characters['Mrs. Peacock']}",
        f"🟣 **Professor Plum**: {characters['Professor Plum']}"
    ])
    
    room_descriptions = "\n".join([
        f"🍽️ **Kitchen**: {rooms['Kitchen']}",
        f"🍴 **Dining Room**: {rooms['Dining Room']}",
        f"🛋️ **Lounge**: {rooms['Lounge']}",
        f"🏛️ **Hall**: {rooms['Hall']}",
        f"📚 **Study**: {rooms['Study']}",
        f"📖 **Library**: {rooms['Library']}",
        f"🎱 **Billiard Room**: {rooms['Billiard Room']}",
        f"🌿 **Conservatory**: {rooms['Conservatory']}",
        f"💃 **Ballroom**: {rooms['Ballroom']}"
    ])
    
    await ctx.send(f"**Characters:**\n{character_descriptions}")
    await ctx.send(f"**Rooms:**\n{room_descriptions}")

@bot.command(name='search')
async def search(ctx, *, room: str):
    global discovered_clues
    room = room.title().strip()
    if room in clues:
        clue_details = clues[room]
        if room not in discovered_clues:
            discovered_clues.append(room)
            await ctx.send(f"In the {room}, you find clues that point to {clue_details['suspect']} with the {clue_details['weapon']}.")
        else:
            await ctx.send(f"You have already found all clues in the {room}. Try another room.")
    else:
        await ctx.send(f"The {room} is not a valid room. Choose from {', '.join(rooms.keys())}.")

@bot.command(name='accuse')
async def accuse(ctx, suspect: str, weapon: str, room: str):
    if suspect.title().strip() == murderer and weapon.title().strip() == murder_weapon and room.title().strip() == crime_scene:
        await ctx.send(f"Congratulations! {suspect} did it in the {room} with the {weapon}. You solved the mystery!")
    else:
        await ctx.send("That's not correct. Keep investigating!")

@bot.command(name='hint')
async def hint(ctx):
    if len(discovered_clues) < 3:
        await ctx.send("Keep searching for more clues. You don't have enough information yet.")
    else:
        hint = f"Consider the relationship between the clues. Think about {random.choice(['the room', 'the weapon', 'the suspect'])}."
        await ctx.send(hint)

@bot.command(name='vote')
async def vote(ctx, *, suspect: str):
    suspect = suspect.title().strip()
    if suspect in characters:
        votes[suspect] += 1
        await ctx.send(f"Vote registered for {suspect}.")
    else:
        await ctx.send(f"{suspect} is not a valid character.")

@bot.command(name='tally_votes')
async def tally_votes(ctx):
    if votes:
        tally = "\n".join([f"{suspect}: {count}" for suspect, count in votes.items()])
        await ctx.send(f"Current votes:\n{tally}")
    else:
        await ctx.send("No votes have been cast yet.")

@bot.command(name='summary')
async def summary(ctx):
    if discovered_clues:
        summary = "\n".join([f"{room}: suspect is {clues[room]['suspect']}, weapon is {clues[room]['weapon']}" for room in discovered_clues])
        await ctx.send(f"Discovered clues:\n{summary}")
    else:
        await ctx.send("No clues have been discovered yet.")

@bot.command(name='toggle_events')
async def toggle_events(ctx):
    global random_event_enabled
    random_event_enabled = not random_event_enabled
    status = "enabled" if random_event_enabled else "disabled"
    await ctx.send(f"Random events are now {status}.")

@tasks.loop(minutes=5) 
async def random_event():
    if random_event_enabled:
        event = random.choice(["A strange noise echoes through the mansion.", "The lights flicker and go out momentarily.", "A shadow moves across the hallway."])
        channel = bot.get_channel(GAME_CHANNEL_ID)
        await channel.send(event)

bot.run(TOKEN)
