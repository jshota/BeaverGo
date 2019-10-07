#!/bin/bash
echo 'Update Progress...'
echo '================='
git checkout master
git merge dev
git push origin dev
git checkout dev
echo '================='
echo 'Done'