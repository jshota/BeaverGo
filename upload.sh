#!/bin/bash
Green='\033[0;32m'
White='\033[1;37m'
NC='\033[0m'
echo -e "${White}Update Progress...${NC}"
echo -e "${White}=================${NC}${Green}"
git add .
echo -n "add commit to the repo: "
read input


git commit -m "$input"
echo -e "${Green}git commit -m \"$input\" --Done${NC}"
git checkout master
echo -e "${Green}git git checkout master --Done${NC}"
git merge dev
echo -e "${Green}git merge dev --Done${NC}"
git push origin master
echo -e "${Green}git push origin master --Done${NC}"
git checkout dev
echo -e "${Green}git checkout dev --Done${NC}"
git push origin dev
echo -e "${Green}git push origin dev --Done${NC}"
echo -e "${White}=================${NC}"
echo -e "${White}Done${NC}"