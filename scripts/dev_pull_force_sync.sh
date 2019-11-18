#!/bin/bash
Green='\033[0;32m'
White='\033[1;37m'
NC='\033[0m'
echo -e "${White}Update Progress...${NC}"
echo -e "${White}=================${NC}"
git fetch --all && git reset --hard origin/dev && git pull
echo -e "${Green}git fetch --all && git reset --hard origin/dev && git pull --Done${NC}"
echo -e "${White}=================${NC}"
echo -e "${White}Updated Complete${NC}"
