class Monitor:
    def __init__(self):
        self.parameters = {}
        self.active = False
        
    def configure(self, params):
        self.parameters = {
            'min_volume': params.get('min_volume', 0),
            'min_mcap': params.get('min_mcap', 0),
            'max_mcap': params.get('max_mcap', float('inf')),
            'min_unique_buyers': params.get('min_unique_buyers', 0),
            'webhook_url': params.get('webhook_url', None)
        }
        return self

    def start(self):
        self.active = True
        # Initialize monitoring logic
        return self

    def stop(self):
        self.active = False
        return self 