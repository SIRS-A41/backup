python3 check_files.py /data/projects filecheck.log

exit_status=$?
if [ "${exit_status}" -ne 0 ]
then
    echo "Error checking files. Shutting down..."
    shutdown -h now
else
    echo "All files ok."
fi
