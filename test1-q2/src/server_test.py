import server
import unittest
import json

class MyTestCase(unittest.TestCase):
    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_description(self):
        response = self.app.get('/status')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['myapplication']['description'], 'pre-interview technical test')
    
if __name__ == '__main__':
    unittest.main()
