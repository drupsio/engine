"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, April 2021
"""

from drups.env import config

host = config.get("DOCKER_HOST", None)
tls_verify = config.get("DOCKER_TLS_VERIFY", 0)
cert_path = config.get("DOCKER_CERT_PATH", None)
registry = config.get("DOCKER_REGISTRY_HOST", None)
registry_username = config.get("DOCKER_REGISTRY_USER", None)
registry_password = config.get("DOCKER_REGISTRY_PASS", None)

del config
