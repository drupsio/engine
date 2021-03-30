"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, March 2021
"""

import datetime

from drups.app import app


@app.task
def say_hello(name):
    """
    An example task.

    :param name: Parameter Name.
    :return: Some response.
    """

    return {"time": datetime.datetime.now().timestamp(), "message": f"Hello, {name}!"}
