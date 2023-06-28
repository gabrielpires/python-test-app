import unittest
from app import HelloWorld

class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.hw = HelloWorld()

    def test_get_message(self):
        self.assertEqual(self.hw.get_message(), 'Hello, World!')

    def test_get_message_not_empty(self):
        self.assertTrue(bool(self.hw.get_message().strip()))

    def test_get_message_is_string(self):
        self.assertIsInstance(self.hw.get_message(), str)

    def test_get_message_is_not_int(self):
        self.assertNotIsInstance(self.hw.get_message, int)

if __name__ == "__main__":
    unittest.main()