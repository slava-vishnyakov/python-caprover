#!/bin/bash

set -euo pipefail

echo -n "Directory name: "; read PROJECT
git clone git@github.com:slava-vishnyakov/python-caprover $PROJECT
cd $PROJECT
git checkout orator
rm -rf .git
python3 initialize.py
rm initialize.py init.sh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
echo "Done! Run:  (npm run start-db &); npm run serve"
