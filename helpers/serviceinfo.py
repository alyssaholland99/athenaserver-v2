import json

with open('configs/service_info.json') as f:
    service_json = json.load(f)

def getServiceDetails(service):
    return service_json[service]

def getServiceField(service, field):
    return getServiceDetails(service)[field]

def getServiceNames():
    return service_json.keys()

def getServiceAlias(user_input):
    for service in getServiceNames:
        for alias in getServiceField(service):
            if user_input == alias:
                return service
    return False