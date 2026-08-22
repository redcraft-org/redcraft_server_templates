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
            },
            {
                'old': '1.9.2.*',
                'new': '2.0',
                'expected': '2.*'
            },
            {
                # Year based Minecraft versions have one part less than the old 1.x.y scheme,
                # the pin backs off a level so it still matches the new version
                'old': '1.20.*',
                'new': '26.2',
                'expected': '26.*'
            },
            {
                'old': '1.20.*',
                'new': '26.2.1',
                'expected': '26.2.*'
            },
            {
                # Fabric style versions carry a +mcversion suffix in their last part,
                # the wildcard swallows it and stays free of + characters
                'old': '0.96.*',
                'new': '0.157.0+26.2',
                'expected': '0.157.*'
            }
        ]

    def test_new_wildcard_generation(self):
        for test_case in self.test_cases:
            test_case['output'] = generate_new_wildcard_version(
                test_case['old'], test_case['new'])
            self.assertEqual(test_case['expected'], test_case['output'])
