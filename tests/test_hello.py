"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, March 2021
"""

import unittest


class TestHello(unittest.TestCase):
    def test_hello(self):
        hello = "Hello, World!"

        self.assertEqual(hello, "Hello, World!")


if __name__ == "__main__":
    unittest.main()
