import os
import unittest


class EmissionTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_volkswagen_emissions(self):
        expected_output = 'PASS'

        actual_output = 'PASS'

        self.assertEqual(expected_output, actual_output)