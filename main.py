
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os
from keep_alive import keep_alive
from datetime import datetime
import asyncio
import requests
import random
import pytz
from PIL import Image, ImageDraw, ImageFont

nigeria_tz = pytz.timezone('Africa/Lagos')

api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH'])
session_string = os.environ['SESSION_STRING']

client = TelegramClient(StringSession(session_string), api_id, api_hash)

source_channels = [
    'firepipsignals',
    'Forex_Top_Premium_Signals',
    'forexsignals01_trade',
    'forexgdp0',
    'Goldforexsignalfx11',
    'habbyforex',
    'kojoforextrades',
    'HONG-SOCIETY'
]

target_channel = '@DonwiseVault'

keywords = ['buy', 'sell', 'tp', 'sl', 'xauusd', 'nas100', 'us30', 'eurusd', 'gbpusd', 'gold', 'gbpjpy']
blocked_phrases = [
    'weekly performance result', 'see you on monday', 'celebrate', 'instagram.com',
    'go check and comment to win', 'By @RealDonwise 🔥 | Donwise Copytrade Vault',
    'tp1', 'tp2', 'running', 'easy hit', 'smassshedd', 'closed another',
    'set breakeven', 'tp 1', 'tp 2', 'tp3'
]

signature = "\n\nBy @RealDonwise\nDonwise Copytrade Vault"

motivational_quotes = [
    "Start your day with clarity and conviction. The pips you seek are on the other side of fear. Take the shot. 🧠📈",
    "Every pip is a step closer to freedom. Trade smart, stay disciplined, and keep building your edge. 💪📉",
    "The market doesn’t care about excuses—only execution. Stick to the plan and grow your account. 🚀📈",
    "Let your strategy speak louder than your emotions today. Risk little. Win big. 👊🔥",
    "There’s no growth in the comfort zone. Make smart moves today. Don’t chase—calculate. 📉📈",
    "No one became great by guessing. Analyze. Execute. Elevate. Today’s another shot. 🎯📈",
    "The charts don’t lie. Your discipline defines your destiny. Let’s get to work. 📈🔐"
]

motivational_images = [
    'https://i.ibb.co/g7Zwqft/motivation1.jpg',
    'https://i.ibb.co/LNRXJjJ/motivation2.jpg',
    'https://i.ibb.co/0ncsCK5/motivation3.jpg',
    'https://i.ibb.co/QJQPDKT/motivation4.jpg',
    'https://i.ibb.co/MfGmMLy/motivation5.jpg'
]

forwarded_today = set()
daily_count = 0
last_reset_date = datetime.now(nigeria_tz).date()
morning_posted = False
signal_log = []

# Function definitions follow here...
# (for brevity, this version will include just the files setup)

