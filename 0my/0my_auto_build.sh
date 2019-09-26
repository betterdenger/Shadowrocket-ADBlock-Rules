#!/bin/bash


CURDIR=$(pwd)
PROJECT_ROOT=$(dirname $0)/..
cd $PROJECT_ROOT

git remote add upstream https://github.com/h2y/Shadowrocket-ADBlock-Rules.git
git fetch --all
git checkout master
git rebase upstream/master origin/master
git push origin master

cd $CURDIR
/usr/bin/env python3 0my_build_confs.py

git add .
git commit -m "Private rules"
git push origin master
