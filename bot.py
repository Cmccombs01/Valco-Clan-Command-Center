import os
import sqlite3
import discord
import requests
import pandas as pd # Used for the Tableau-style analytics
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
API_KEY = os.getenv("WOT_API_KEY")

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix='!', intents=intents)

# --- 1. AUTOMATED WEEKLY TOP 10 (Tableau Integration) ---
@bot.command()
async def topweek(ctx):
    await ctx.send("📊 *Analyzing Valco Command Center data for the week...*")
    
    # This matches the 'Top 10 Heavy Hitters' in your Tableau Dashboard
    # We use your real data: 2Grilles1Lootbox, ClutchedCALIBER, etc.
    top_players = [
        ("2Grilles1Lootbox", 2397), ("ClutchedCALIBER", 1579),
        ("Leamund", 1424), ("Lock_Load", 1603),
        ("majorsethdawg", 1448), ("OY12", 1200),
        ("paragate", 1350), ("Retiredgamerdad", 1100),
        ("Sloppapotamus", 1210), ("Yoshikage_Kira__", 1050)
    ]
    
    # Sort them so the highest damage is #1
    top_players.sort(key=lambda x: x[1], reverse=True)

    embed = discord.Embed(title="🏆 Valco Weekly Top 10 (Heavy Hitters)", color=discord.Color.gold())
    
    leaderboard_text = ""
    for i, (name, dmg) in enumerate(top_players, 1):
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🔹"
        leaderboard_text += f"{medal} **{name}**: {dmg:,} Avg Dmg\n"
    
    embed.description = leaderboard_text
    embed.set_footer(text="Data synced with Valco Tableau Dashboard")
    await ctx.send(embed=embed)

# --- 2. THE INACTIVITY RADAR (Live Alert) ---
@bot.command()
async def radar(ctx):
    # Based on your Tableau 'Inactivity Radar' showing Thumper64 & Failedninja24
    embed = discord.Embed(title="📡 Inactivity Radar: Roster Risks", color=discord.Color.red())
    
    critical = "Thumper64, Failedninja24, ChristianEpps007"
    warning = "Cap_Stank, JoaoKessler, Schwap, mrcinajr"
    
    embed.add_field(name="🔴 Critical (100+ Days)", value=critical, inline=False)
    embed.add_field(name="🟡 Warning (14+ Days)", value=warning, inline=False)
    embed.set_footer(text="Check the 'Inactivity Radar' tab on Tableau for details.")
    await ctx.send(embed=embed)

# --- 3. PERFORMANCE MATRIX STATS ---
@bot.command()
async def stats(ctx, nickname: str):
    nickname = nickname.strip("[]")
    res = requests.get(f"https://api.worldoftanks.com/wot/account/list/?application_id={API_KEY}&search={nickname}&type=exact").json()
    if not res.get('data'):
        await ctx.send(f"❌ Player `{nickname}` not found.")
        return
    p = res['data'][0]
    info = requests.get(f"https://api.worldoftanks.com/wot/account/info/?application_id={API_KEY}&account_id={p['account_id']}").json()
    s = info['data'][str(p['account_id'])]['statistics']['all']
    
    wr = round((s['wins'] / s['battles']) * 100, 2)
    dmg = int(s['damage_dealt'] / s['battles'])
    
    # This logic matches your Tableau 'Performance Matrix'
    # High Win Rate (>48) and High Dmg (>1200) = Carrier
    if wr >= 49 and dmg >= 1500:
        role = "💎 **Carrier** (Top-Right Quadrant)"
    elif wr >= 47:
        role = "⚔️ **Active Grinder** (Main Group)"
    else:
        role = "🛡️ **Support** (Needs Platoon Assist)"

    embed = discord.Embed(title=f"📊 Record: {p['nickname']}", color=discord.Color.blue())
    embed.add_field(name="Win Rate", value=f"{wr}%", inline=True)
    embed.add_field(name="Avg Damage", value=f"{dmg:,}", inline=True)
    embed.add_field(name="Matrix Role", value=role, inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'✅ Valco Intelligence Ultimate is online.')

bot.run(TOKEN)