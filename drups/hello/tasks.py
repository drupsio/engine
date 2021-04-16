"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, March 2021
"""

import datetime

import yaml

import drups.dc.instance as docker
import drups.k8s.instance as k8s
from drups.app import app


@app.task
def example_deployment():
    """
    An example deployment task.

    :return: Deployment response.
    """

    registry = docker.config.registry

    # Docker.

    docker.client.images.build(
        path="/var/app/drups/hello/example", tag=f"{registry}/hello_world"
    )
    docker.client.images.push(repository=f"{registry}/hello_world")

    # Kubernetes.

    # Prepare files.
    deployment_file = open("/var/app/drups/hello/example/hello-world-deployment.yaml")
    service_file = open("/var/app/drups/hello/example/hello-world-service.yaml")
    deployment = yaml.safe_load(deployment_file)
    service = yaml.safe_load(service_file)

    # Create Deployment.
    apps_v1 = k8s.client.AppsV1Api(k8s.api_client)
    deployment_response = apps_v1.create_namespaced_deployment(
        body=deployment, namespace="default"
    )
    k8s_deployment_result = (
        "Deployment created. status='%s'" % deployment_response.metadata.name
    )

    # Create Service.
    core_v1 = k8s.client.CoreV1Api(k8s.api_client)
    service_response = core_v1.create_namespaced_service(
        body=service, namespace="default"
    )
    k8s_service_result = "Service created. status='%s'" % service_response.metadata.name

    return {
        "k8s_deployment_result": k8s_deployment_result,
        "k8s_service_result": k8s_service_result,
    }


@app.task
def say_hello(name):
    """
    An example task.

    :param name: Parameter Name.
    :return: Some response.
    """

    return {"time": datetime.datetime.now().timestamp(), "message": f"Hello, {name}!"}
