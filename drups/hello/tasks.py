"""
This file is part of the Drups.io Engine.

(c) 2021 Drups.io <dev@drups.io>

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

Written by Temuri Takalandze <temo@drups.io>, March 2021
"""

import yaml

import drups.dc.instance as docker
import drups.k8s.instance as k8s
from drups.app import app


@app.task(name="drups.deployment.start")
def start_deployment(name, branch):
    """
    Start project build.

    :param name: Project name.
    :param branch: Project git branch.
    :return: Deployment result.
    """

    chain = build_image.s(name, branch) | deploy.s(name)
    result = chain().get(disable_sync_subtasks=False)

    return {"message": "Successfully Deployed!", "result": result}


@app.task(name="drups.deployment.build_image", bind=True)
def build_image(self, name, branch):
    """

    :param self: Instance of Celery app.
    :param name: Project name.
    :param branch: Project git branch.
    :return: Image tag.
    """

    name_normalized = name.replace("-", "_")
    task_id = self.request.root_id
    image_tag = f"{docker.config.registry}/{name_normalized}:{branch}"

    # Start Docker build and send the output.
    self.update_state(
        task_id=task_id,
        state="PROGRESS",
        meta={"step": "build_image", "type": "section"},
    )
    for line in docker.api.build(
        path="/var/app/drups/hello/example", tag=image_tag, decode=True
    ):
        self.update_state(
            task_id=task_id,
            state="PROGRESS",
            meta={"step": "build_image", "type": "docker_api_output", "value": line},
        )

    # Start Docker push and send the output.
    self.update_state(
        task_id=task_id,
        state="PROGRESS",
        meta={"step": "push_image", "type": "section"},
    )
    for line in docker.client.api.push(repository=image_tag, stream=True, decode=True):
        self.update_state(
            task_id=task_id,
            state="PROGRESS",
            meta={"step": "push_image", "type": "docker_api_output", "value": line},
        )

    return image_tag


@app.task(name="drups.deployment.deploy", bind=True)
def deploy(self, image, name):
    """
    Deploy project to the k8s.

    :param self: Instance of Celery app.
    :param image: Docker image to deploy.
    :param name: Project name.
    :return: Deployment result.
    """

    task_id = self.request.root_id

    # Prepare files.
    deployment_content = open("/var/app/drups/hello/example/deployment.yaml").read()
    service_content = open("/var/app/drups/hello/example/service.yaml").read()

    deployment_content = deployment_content.replace("__projectName__", name).replace(
        "__image__", image
    )
    service_content = service_content.replace("__projectName__", name)

    deployment = yaml.safe_load(deployment_content)
    service = yaml.safe_load(service_content)

    # Create Deployment.
    self.update_state(
        task_id=task_id,
        state="PROGRESS",
        meta={"step": "create_k8k_deployment", "type": "section"},
    )
    apps_v1 = k8s.client.AppsV1Api(k8s.api_client)
    deployment_response = apps_v1.create_namespaced_deployment(
        body=deployment, namespace="default"
    )
    self.update_state(
        task_id=task_id,
        state="PROGRESS",
        meta={
            "step": "create_k8k_deployment",
            "type": "message",
            "value": "Deployment created. name='%s'"
            % deployment_response.metadata.name,
        },
    )

    # Create Service.
    self.update_state(
        task_id=task_id,
        state="PROGRESS",
        meta={"step": "create_k8k_service", "type": "section"},
    )
    core_v1 = k8s.client.CoreV1Api(k8s.api_client)
    service_response = core_v1.create_namespaced_service(
        body=service, namespace="default"
    )
    self.update_state(
        task_id=task_id,
        state="PROGRESS",
        meta={
            "step": "create_k8k_service",
            "type": "message",
            "value": "Service created. name='%s'" % service_response.metadata.name,
        },
    )

    return {
        "deployment_name": deployment_response.metadata.name,
        "service_name": service_response.metadata.name,
    }
