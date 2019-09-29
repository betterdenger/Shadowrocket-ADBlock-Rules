#!/bin/bash


CURDIR=$(pwd)
PROJECT_ROOT=$(dirname $0)/..
cd $PROJECT_ROOT

git fetch --all
git merge upstream/master origin/master -m "Auto merge"

cd $CURDIR
/usr/bin/env python3 0my_build_confs.py

git add .
git commit -m "Private rules"
git push origin master
