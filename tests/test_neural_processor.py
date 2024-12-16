import unittest
from src.core.neural_processor import NeuralProcessor

class TestNeuralProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = NeuralProcessor()

    def test_process_data(self):
        result = self.processor.process_data({})
        self.assertIn('processed', result)
        self.assertIn('confidence', result)
        self.assertIn('valid', result)
        self.assertTrue(isinstance(result['confidence'], float))

    def test_analyze_pattern(self):
        result = self.processor.analyze_pattern({})
        self.assertIn('pattern_detected', result)
        self.assertIn('risk_score', result)
        self.assertIn('recommendation', result)

if __name__ == '__main__':
    unittest.main() 