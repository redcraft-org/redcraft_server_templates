import unittest
from utils.updater import generate_new_wildcard_version

class UpdaterTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_cases = [
            {
                'old': '1.2.*',
                'new': '1.3.1',
                'expected': '1.3.*'
            },
            {
                'old': '2.*',
                'new': '3.1',
                'expected': '3.*'
            },
            {
                'old': '2.*',
                'new': '3.2.1',
                'expected': '3.*'
            },
            {
                'old': '9.*',
                'new': '10.2.1',
                'expected': '10.*'
            },
            {
                'old': '1.9.*',
                'new': '2.1.1',
                'expected': '2.1.*'
            }
        ]

    def test_new_wildcard_generation(self):
        for test_case in self.test_cases:
            test_case['output'] = generate_new_wildcard_version(test_case['old'], test_case['new'])
            self.assertEqual(test_case['expected'], test_case['output'])
