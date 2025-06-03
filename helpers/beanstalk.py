#!/usr/bin/python

from pystalk import BeanstalkClient
from helpers.serviceinfo import getServiceField

client = BeanstalkClient('vm001.hippocampus-augmented.ts.net', 11300)

def convert_for_beanstalk(service):
    match service:
        case "sotf" | "sons of the forest":
            return "sons_of_the_forest"
        case "feed the beast":
            return "ftb"
        case "beam":
            return "beammp"
        case _:
            return service

def sendMessage(message_to_send):
    print(message_to_send)
    client.put_job(message_to_send)

def getAllMessages(vm):
    jobs = []
    for job in client.reserve_iter():
        try:
            jobs.append(str(job.job_data.decode('utf-8')))
        except Exception:
            client.release_job(job.job_id)
            raise
        if getServiceField(str(job.job_data.decode('utf-8')).split(" ")[1], "vm") == vm: # Only delete the message if the vm for the service is running on the vm
            client.delete_job(job.job_id)
    return jobs