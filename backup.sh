#!/bin/sh

scp -r sirs@192.168.4.1:/home/sirs /home/back/ 2>/dev/null

find /home/back/sirs -type f -iname "*" -print0 | xargs -I {} -0 chmod 0444 {}
find /home/back/sirs -type d -iname "*" -print0 | xargs -I {} -0 chmod 0544 {}

echo "Successful backup"
