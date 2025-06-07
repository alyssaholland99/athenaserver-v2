import json

with open('configs/service_info.json') as f:
    json_data = json.load(f)

def getUserDetails(user_id):
    if not str(user_id in json_data):
        return -1
    return int(json_data[str(user_id)])

def getUserPermissions(user_id):
    if getUserDetails(user_id) == -1:
        return -1
    return getUserDetails(user_id)["level"]

def checkPermission(user_id, requiredPermission):
    return getUserPermissions(user_id) >= requiredPermission

def setPermission(user_id, requiredPermission):
    print("test")