import csv

def getCsv():
    with open('../configs/permissions.csv', mode ='r') as permissionStore:
        return csv.reader(permissionStore)
        

def getPermission(user):
    csv_data = getCsv()
    for line in csv_data:
        if line["id"] == user:
            return line['permission']
        
def setTrusted(user):
