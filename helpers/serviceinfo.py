import json

with open('configs/service_info.json') as f:
    service_json = json.load(f)

def getServiceDetails(service):
    return service_json[service]

def getServiceField(service, field):
    return getServiceDetails(service)[field]

print(getServiceField("minecraft", "port"))
print(getServiceField("minecraft", "url"))