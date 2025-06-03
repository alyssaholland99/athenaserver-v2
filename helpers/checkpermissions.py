import json

with open('configs/service_info.json') as f:
    json_data = json.load(f)

def getUserDetails(user_id):
    return int(json_data[str(user_id)])

def getUserPermissions(user_id):
    return getUserDetails(user_id)["level"]

def checkPermission(user_id, requiredPermission):
    return getUserPermissions(user_id) >= requiredPermission

def setPermission(user_id, requiredPermission):
    print("test")