#!/bin/bash
Green='\033[0;32m'
White='\033[1;37m'
NC='\033[0m'
echo -e "${White}Update Progress...${NC}"
echo -e "${White}=================${NC}"
cd ..
git checkout dev
echo -e "${Green}git checkout to dev --Done${NC}"
rm db.sqlite3
echo -e "${Green}rm db.sqlite3 --Done${NC}"
git pull
echo -e "${Green}git pull --Done${NC}"
git add .
echo -e "${Green}git add . --Done${NC}"
echo -e "${White}=================${NC}"
echo "Comment examples:"
echo "  Add: a function to get user's location"
echo "  Fix: unable to login"
echo "  Change: home page title"
echo "  Chord: test"
echo -e "${White}=================${NC}"
echo "Select your commit type:"
echo "1. Add"
echo "2. Fix"
echo "3. Change"
echo "4. Chord"

read input

case $input in
    1)
        input='Add: '
    ;;
    2)
        input='Fix: '
    ;;
    3)
        input='Change: '
    ;;
    4)
        input='Chord: '
    ;;
esac

echo -e "${White}=================${NC}"
echo -n "Leave your comment here: "

read comment

git commit -m "$input$comment"
echo -e "${Green}git commit -m \"$input\" --Done${NC}"
git push origin dev
echo -e "${Green}git push origin dev --Done${NC}"
echo -e "${White}=================${NC}"
echo -e "${White}Updated Complete${NC}"
