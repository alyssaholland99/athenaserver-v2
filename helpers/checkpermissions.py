import json

with open('configs/permissions.json') as f:
    json_data = json.load(f)

def getUserDetails(user_id):
    try:
        return int(json_data[str(user_id)])
    except:
        return -1
    

def getUserPermissions(user_id):
    if getUserDetails(user_id) == -1:
        return -1
    return getUserDetails(user_id)["level"]

def checkPermission(user_id, requiredPermission):
    print(getUserPermissions(user_id))
    print(requiredPermission)
    return getUserPermissions(user_id) >= requiredPermission

def setPermission(user_id, requiredPermission):
    print("test")