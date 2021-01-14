#!/bin/bash

Path=~/workspace/Shadowrocket-ADBlock-Rules
cd $Path

git checkout origin/master
git pull -s recursive -X theirs origin master
git fetch --all
git merge -X theirs upstream/master origin/master

cd factory
python3 ad.py
python3 gfwlist.py
python3 build_confs.py
cd ..

git add .
git commit -m "Nightly build" -m "已合并最新的去广告规则及 GFWList"
git push origin master
