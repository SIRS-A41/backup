# SIRS-A41 Project
import subprocess

# INFO:
# Run this command on the backup-server.
# Via scp connection it will copy the zip file with the snapshots of the machines:
#   resource-server
# How to run:
# sudo python3 backup-script.py

# Get the data in y-m-d
p1 = subprocess.run(['date', '+%y-%m-%d'], capture_output=True, text=True)
s1 = p1.stdout.strip()

# SCP connection to resources-server
# check if the ip is valid!!!!
r_server = 'sirs@192.168.4.1'
s2 = r_server + ':/home/data/' + s1 + '.zip'
s3 = '/home/back/backup/resource-server/'
p2 = subprocess.run(['scp', s2, s3], capture_output=True, text=True)
