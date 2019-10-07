#!/bin/bash
LightGreen='\033[1;32m'
White='\033[1;37m'
echo -e "${White}Update Progress..."
echo -e "${White}================="
git add .
echo -n "add commit to the repo: "
read input


git commit -m "$input"
echo -e "${LightGreen}git commit -m \"$input\" --Done"
git checkout master
echo -e "${LightGreen}git git checkout master --Done"
git merge dev
echo -e "${LightGreen}git merge dev --Done"
git push origin master
echo -e "${LightGreen}git push origin master --Done"
git checkout dev
echo -e "${LightGreen}git checkout dev --Done"
git push origin dev
echo -e "${LightGreen}git push origin dev --Done"
echo -e "${White}================="
echo -e "${White}Done"