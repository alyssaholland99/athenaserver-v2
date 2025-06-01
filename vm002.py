from helpers.beanstalk import *
from helpers.validservices import *

import os, time
from dotenv import load_dotenv

load_dotenv()

def send_command(command):
    if False:
        print(command)
    else:
        os.system(command)

def get_docker_compose_path(service):
    return "/mnt/game_servers/{}".format(service)

def start_service(service):
    match service:
        case "minecraft":
            send_command("systemctl start minecraft")
        case "ftb":
            send_command("systemctl start ftb")
        case _:
            send_command("docker compose -f {}/docker-compose.yml up -d >> /dev/null 2>&1".format(get_docker_compose_path(service)))


def stop_service(service):
    match service:
        case "minecraft":
            send_command("systemctl stop minecraft")
        case "ftb":
            send_command("systemctl stop ftb")
        case _: 
            send_command("docker compose -f {}/docker-compose.yml down >> /dev/null 2>&1".format(get_docker_compose_path(service)))

def restart_service(service):
    stop_service(service)
    start_service(service)

def services_running():
    return int(os.popen("docker ps | wc -l").read())

for message in getAllMessages():
    splitMessage = message.split(" ")
    if not valid_service_bool(splitMessage[1]):
        continue
    match splitMessage[0]:
        case "start":
            start_service(splitMessage[1])
        case "stop":
            stop_service(splitMessage[1])
        case "restart":
            restart_service(splitMessage[1])
        case _:
            print("'{}' is not in the service controls".format(splitMessage[0]))
    time.sleep(15)

if services_running() <= 2:
    for retry in range(11):
        time.sleep(30)
        if retry == 10:
            os.system("shutdown now")


service_retry_count = 0
service_timeout = 2 # Minutes until the vm shuts down when no services are running

while services_running <= 2:
    service_retry_count += 1
    time.sleep(30)
    if service_retry_count == service_timeout*2:
        os.system("shutdown now")