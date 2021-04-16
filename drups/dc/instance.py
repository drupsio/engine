"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, April 2021
"""

import os

import docker

import drups.dc.config as config

os.environ["DOCKER_HOST"] = config.host
os.environ["DOCKER_TLS_VERIFY"] = config.tls_verify
os.environ["DOCKER_CERT_PATH"] = config.cert_path

# Connect to Docker and log-in to the registry.
client = docker.from_env()
auth_data = client.login(
    username=config.registry_username,
    password=config.registry_password,
    registry=config.registry,
    reauth=True,
)
del os
