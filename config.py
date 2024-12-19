import os
from dotenv import load_dotenv

# load env from .env file
load_dotenv()

class Config:
    TOKEN = os.getenv('DISCORD_TOKEN')