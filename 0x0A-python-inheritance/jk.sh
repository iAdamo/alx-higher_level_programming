#!/bin/bash
git add .
git add ..

ech0 -n read $1

git commit -m "{message}"

git push
