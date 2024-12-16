import unittest
from src.core.monitor import Monitor

class TestMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = Monitor()

    def test_configure(self):
        params = {
            'min_volume': 1.0,
            'min_mcap': 10000,
            'webhook_url': 'https://discord.com/api/webhooks/test'
        }
        self.monitor.configure(params)
        self.assertEqual(self.monitor.parameters['min_volume'], 1.0)
        self.assertEqual(self.monitor.parameters['min_mcap'], 10000)

    def test_start_stop(self):
        self.assertFalse(self.monitor.active)
        self.monitor.start()
        self.assertTrue(self.monitor.active)
        self.monitor.stop()
        self.assertFalse(self.monitor.active)

if __name__ == '__main__':
    unittest.main() 