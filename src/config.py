import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    BLOCKCHAIN_API_KEY = os.getenv('BLOCKCHAIN_API_KEY')
    DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
    
    # Monitor Settings
    DEFAULT_MIN_VOLUME = 1.0
    DEFAULT_MIN_MCAP = 10000
    MAX_CONCURRENT_MONITORS = 100
    
    # Neural Processor Settings
    CONFIDENCE_THRESHOLD = 0.75
    RISK_THRESHOLD = 0.5
    
    # Server Settings
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    PORT = int(os.getenv('PORT', 8000)) 