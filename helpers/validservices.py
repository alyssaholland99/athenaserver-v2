valid_services_file = open("configs/allowed_services.txt", "r")
valid_services = valid_services_file.read().splitlines()
valid_services_file.close()

# Checks to see if the service can be conrolled, returns boolean
def valid_service_bool(service):
    return service in valid_services

def valid_service(service):
    if not valid_service_bool(service):
        print("{} is not a valid service".format(service))
        return("{} is not a valid service".format(service))