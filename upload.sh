#!/bin/bash
echo 'Update Progress...'
echo '================='
git add .
echo 'add commit to the repo:'
read input


git commit -m "$input"
echo 'git commit -m "$input" --Done'
git checkout master
echo 'git git checkout master --Done'
git merge dev
echo 'git merge dev --Done'
git push origin master
echo 'git push origin master --Done'
git checkout dev
echo 'git checkout dev --Done'
git push origin dev
echo 'git push origin dev --Done'
echo '================='
echo 'Done'