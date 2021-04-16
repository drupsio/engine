"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, April 2021
"""

from drups.env import config

host = config.get("K8S_HOST", None)

del config
