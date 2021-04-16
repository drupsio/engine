"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, April 2021
"""

import os

from dotenv import dotenv_values

config = {**dotenv_values(".env"), **dotenv_values(".env.local"), **os.environ}

del os, dotenv_values
