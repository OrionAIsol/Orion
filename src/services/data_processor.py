import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DataProcessor:
    def __init__(self):
        self.cache = {}
        self.timeframes = {
            '1m': 60,
            '5m': 300,
            '15m': 900,
            '1h': 3600
        }

    def process_market_data(self, data, timeframe='5m'):
        df = pd.DataFrame(data)
        
        # Add technical indicators
        df['sma_20'] = df['price'].rolling(window=20).mean()
        df['sma_50'] = df['price'].rolling(window=50).mean()
        df['volume_sma'] = df['volume'].rolling(window=20).mean()
        
        # Calculate momentum
        df['momentum'] = df['price'].pct_change(periods=10)
        
        # Detect volume spikes
        df['volume_spike'] = df['volume'] > (df['volume_sma'] * 2)
        
        return {
            'processed_data': df.to_dict('records'),
            'indicators': self._calculate_indicators(df),
            'signals': self._generate_signals(df),
            'timestamp': datetime.now().isoformat()
        }

    def _calculate_indicators(self, df):
        return {
            'trend': self._detect_trend(df),
            'volatility': self._calculate_volatility(df),
            'momentum': df['momentum'].iloc[-1]
        }

    def _generate_signals(self, df):
        signals = []
        
        # Volume spike signal
        if df['volume_spike'].iloc[-1]:
            signals.append({
                'type': 'volume_spike',
                'strength': 'high',
                'timestamp': datetime.now().isoformat()
            })
            
        # Trend change signal
        if df['sma_20'].iloc[-1] > df['sma_50'].iloc[-1] and \
           df['sma_20'].iloc[-2] <= df['sma_50'].iloc[-2]:
            signals.append({
                'type': 'trend_change',
                'direction': 'bullish',
                'timestamp': datetime.now().isoformat()
            })
            
        return signals

    def _detect_trend(self, df):
        last_price = df['price'].iloc[-1]
        sma_20 = df['sma_20'].iloc[-1]
        sma_50 = df['sma_50'].iloc[-1]
        
        if last_price > sma_20 and sma_20 > sma_50:
            return 'strong_bullish'
        elif last_price > sma_20:
            return 'bullish'
        elif last_price < sma_20 and sma_20 < sma_50:
            return 'strong_bearish'
        else:
            return 'bearish'

    def _calculate_volatility(self, df):
        return df['price'].std() / df['price'].mean() 