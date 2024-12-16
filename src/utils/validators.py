from web3 import Web3

class Validators:
    @staticmethod
    def is_valid_address(address):
        return Web3.isAddress(address)
    
    @staticmethod
    def validate_monitor_params(params):
        required = ['min_volume', 'webhook_url']
        errors = []
        
        for field in required:
            if field not in params:
                errors.append(f"Missing required field: {field}")
        
        if params.get('min_volume', 0) < 0:
            errors.append("Minimum volume cannot be negative")
            
        if params.get('min_mcap', 0) < 0:
            errors.append("Minimum market cap cannot be negative")
            
        return len(errors) == 0, errors 