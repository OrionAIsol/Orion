class Formatters:
    @staticmethod
    def format_volume(volume):
        if volume >= 1_000_000:
            return f"{volume/1_000_000:.2f}M"
        elif volume >= 1_000:
            return f"{volume/1_000:.2f}K"
        return f"{volume:.2f}"
    
    @staticmethod
    def format_address(address):
        if not address:
            return ""
        return address[:6] + "..." + address[-4:]
    
    @staticmethod
    def format_timestamp(timestamp):
        # Add timestamp formatting logic
        return timestamp 