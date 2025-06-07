import json

with open('configs/permissions.json') as f:
    json_data = json.load(f)

def getUserDetails(user_id):
    print (json_data[str(user_id)]["level"])
    try:
        return int(json_data[str(user_id)])
    except:
        return -1
    
def getUserLevel(user_id):
    try:
        return int(json_data[str(user_id)]["level"])
    except:
        return -1

def checkPermission(user_id, requiredPermission):
    return getUserLevel(user_id) >= requiredPermission

def setPermission(user_id, requiredPermission):
    print("test")