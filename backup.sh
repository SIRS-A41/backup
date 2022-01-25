#!/bin/sh

scp -r -q sirs@192.168.1.112:~ /home/backup/projects 2> /dev/null

find /home/backup/projects -type f -iname "*" -print0 | xargs -I {} -0 chmod 0444 {}
find /home/backup/projects -type d -iname "*" -print0 | xargs -I {} -0 chmod 0644 {}

echo "Successful backup"
