"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, April 2021
"""

from kubernetes import client

import drups.k8s.config as config

configuration = client.Configuration()
configuration.host = config.host

api_client = client.ApiClient(configuration)
