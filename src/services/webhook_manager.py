import aiohttp
import asyncio
from src.config import Config

class WebhookManager:
    def __init__(self):
        self.webhook_url = Config.DISCORD_WEBHOOK_URL
        self.session = None

    async def initialize(self):
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def close(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def send_alert(self, data):
        if not self.session:
            await self.initialize()

        embed = {
            "title": "🚨 Alert: Pattern Detected",
            "color": 3447003,  # Blue
            "fields": [
                {"name": "Pattern Type", "value": data.get('pattern', 'Unknown'), "inline": True},
                {"name": "Confidence", "value": f"{data.get('confidence', 0)*100:.1f}%", "inline": True},
                {"name": "Risk Score", "value": f"{data.get('risk_score', 0)*100:.1f}%", "inline": True}
            ],
            "footer": {"text": "Orion Neural Monitor"}
        }

        payload = {
            "embeds": [embed]
        }

        try:
            async with self.session.post(self.webhook_url, json=payload) as response:
                return response.status == 200
        except Exception as e:
            print(f"Error sending webhook: {str(e)}")
            return False 