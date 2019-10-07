#!/bin/bash
echo 'Update Progress...'
echo '================='
git add .
echo 'add commit to the repo:'
read input

git commit -m "$input"
git checkout master
git merge dev
git push origin master
git checkout dev
echo '================='
echo 'Done'