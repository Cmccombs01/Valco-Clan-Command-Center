import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Your exact Valco Clan #general channel ID
CHANNEL_ID = 1476143077977489471 

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')
    
    # 1. Find the #general channel
    channel = client.get_channel(CHANNEL_ID)
    
    if channel:
        print("📡 Transmitting Valco Daily Report...")
        
        # --- THE HEAVY HITTERS REPORT ---
        top_players = [
            ("2Grilles1Lootbox", 2397), ("Lock_Load", 1603), 
            ("ClutchedCALIBER", 1579), ("majorsethdawg", 1448), 
            ("Leamund", 1424), ("paragate", 1350), 
            ("Sloppapotamus", 1210), ("OY12", 1200),
            ("Retiredgamerdad", 1100), ("Yoshikage_Kira__", 1050)
        ]
        
        embed1 = discord.Embed(title="🏆 Valco Weekly Top 10 (Heavy Hitters)", color=discord.Color.gold())
        leaderboard_text = ""
        for i, (name, dmg) in enumerate(top_players, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🔹"
            leaderboard_text += f"{medal} **{name}**: {dmg:,} Avg Dmg\n"
        embed1.description = leaderboard_text
        embed1.set_footer(text="Data synced with Valco Tableau Dashboard")
        await channel.send(embed=embed1)
        
        # --- THE INACTIVITY RADAR ---
        embed2 = discord.Embed(title="📡 Inactivity Radar: Roster Risks", color=discord.Color.red())
        critical = "Thumper64, Failedninja24, ChristianEpps007"
        warning = "Cap_Stank, JoaoKessler, Schwap, mrcinajr"
        embed2.add_field(name="🔴 Critical (100+ Days)", value=critical, inline=False)
        embed2.add_field(name="🟡 Warning (14+ Days)", value=warning, inline=False)
        embed2.set_footer(text="Check the 'Inactivity Radar' tab on Tableau for details.")
        await channel.send(embed=embed2)
        
        print("✅ Transmission complete.")
    else:
        print(f"❌ Error: Could not find channel {CHANNEL_ID}.")

    # 2. THE MOST IMPORTANT PART: Tell the bot to go to sleep so GitHub can finish!
    print("🌙 Shutting down the bot engine...")
    await client.close()

client.run(TOKEN)
