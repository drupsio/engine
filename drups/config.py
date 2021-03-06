"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, March 2021
"""

# pylint: disable=C0103

from drups.env import config

broker_url = config.get("BROKER_URL", None)
result_backend = config.get("RESULT_BACKEND", None)

imports = ("drups.hello.tasks",)

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]

del config
