import os

ssh_command = "ssh root@192.168.0.121 -t"

def startVM(vm):
    os.system('{} "virsh start {}"'.format(ssh_command, vm))

def stopVM(vm):
    os.system('{} -t "virsh shutdown {}"'.format(ssh_command, vm))
