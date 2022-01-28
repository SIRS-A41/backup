# SIRS-A41 Project
import subprocess

# INFO:
# Run this command on the resource-server and auth-server.
# How to run:
# sudo python3 snapshot-script.py

# Get the data in y-m-d
p1 = subprocess.run(['date', '+%y-%m-%d'], capture_output=True, text=True)
s1 = p1.stdout.strip()

# Take Read-only Snapshot of every Project
s2 = '/data/.snapshots/' + s1
p2 = subprocess.run(['sudo', 'btrds', 'subvolume', 'snapshot', '-r', '/data/projects/', s2], shell=True)

# Zip Snapshots
s3 = s1 + '.zip'
p3 = subprocess.run(['sudo', 'zip', '-r', s3, 'data/./snapshots/*'], shell=True)