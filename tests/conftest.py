import pytest
from src.core.monitor import Monitor
from src.core.neural_processor import NeuralProcessor
from src.services.blockchain_scanner import BlockchainScanner
from src.services.pattern_detector import PatternDetector
from src.services.market_analyzer import MarketAnalyzer

@pytest.fixture
def monitor():
    return Monitor()

@pytest.fixture
def processor():
    return NeuralProcessor()

@pytest.fixture
def scanner():
    return BlockchainScanner()

@pytest.fixture
def pattern_detector():
    return PatternDetector()

@pytest.fixture
def market_analyzer():
    return MarketAnalyzer()

@pytest.fixture
def sample_market_data():
    return {
        'price': 100.0,
        'volume': 1000.0,
        'trades': 50,
        'timestamp': '2024-01-01T00:00:00Z'
    }

@pytest.fixture
def sample_monitor_params():
    return {
        'min_volume': 1.0,
        'min_mcap': 10000,
        'webhook_url': 'https://discord.com/api/webhooks/test'
    } 