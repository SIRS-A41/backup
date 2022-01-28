import pymongo
import hashlib
import os
import sys
import datetime
import base64

BUF_SIZE = 65536
rootdir = sys.argv[1]
log_path = ''
if len(sys.argv) > 2:
    log_path = sys.argv[2]

mongo = pymongo.MongoClient('localhost', 27017)

# go through every user
for user in os.listdir(rootdir):
    user_dir = os.path.join(rootdir, user)

    # go through every project of that user
    for project in os.listdir(user_dir):
        project_dir = os.path.join(user_dir, project)

        for path, subdirs, files in os.walk(project_dir):
            for filename in files:
                file_path = os.path.join(path, filename)

                # hash file
                sha256 = hashlib.sha256()
                with open(file_path, 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        sha256.update(data)
                file_hash = base64.b64encode(sha256.digest()).decode()

                # compare to filename
                if file_hash != filename:
                    if log_path:
                        with open(log_path, 'a') as log:
                            ts = datetime.datetime.now()
                            log.write(f'{ts}\tFile {filename}: incorrect name (should be {file_hash}).\n')
                    exit(1)

                # compare to hash in database
                db_version = mongo.versions[project].find_one({"version": file_hash})
                if db_version == None:
                    with open(log_path, 'a') as log:
                        ts = datetime.datetime.now()
                        log.write(f'{ts}\tFile {filename}: hash ({file_hash}) doesn\'t match any version in the database.\n')
                    exit(1)