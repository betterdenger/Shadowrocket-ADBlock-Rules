#!/bin/bash


CURDIR=$(pwd)
PROJECT_ROOT=$(dirname $0)/..
cd $PROJECT_ROOT

git remote add upstream https://github.com/h2y/Shadowrocket-ADBlock-Rules.git
git fetch --all
git checkout origin/master
git merge upstream/master
git push origin master

cd $CURDIR
/usr/bin/env python 0my_build_confs.py

git add .
git commit -m "Private rules"
git push
