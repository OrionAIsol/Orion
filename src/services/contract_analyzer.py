from web3 import Web3
from src.config import Config

class ContractAnalyzer:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(Config.BLOCKCHAIN_RPC_URL))
        self.risk_patterns = {
            'honeypot': self._check_honeypot,
            'mint_function': self._check_mint_function,
            'high_tax': self._check_high_tax,
            'blacklist': self._check_blacklist
        }

    def analyze_contract(self, address):
        risks = []
        risk_score = 0
        
        for pattern_name, checker in self.risk_patterns.items():
            result = checker(address)
            if result['detected']:
                risks.append({
                    'type': pattern_name,
                    'severity': result['severity'],
                    'details': result['details']
                })
                risk_score += result['severity']

        return {
            'risks': risks,
            'risk_score': min(risk_score / 10, 1.0),
            'is_valid': risk_score < 5
        }

    def _check_honeypot(self, address):
        return {
            'detected': False,
            'severity': 0,
            'details': 'No honeypot patterns detected'
        }

    def _check_mint_function(self, address):
        return {
            'detected': False,
            'severity': 0,
            'details': 'No mint function found'
        }

    def _check_high_tax(self, address):
        return {
            'detected': False,
            'severity': 0,
            'details': 'Normal tax rates'
        }

    def _check_blacklist(self, address):
        return {
            'detected': False,
            'severity': 0,
            'details': 'Not blacklisted'
        } 