#!/usr/bin/env sh

# This is a basic setup script for this driver.
# Jens Dede <jd@comnets.uni-bremen.de>

echo "Checking if git is installed..."
if command -v git >/dev/null 2>&1; then
    echo "Git is installed. Proceeding..."
else
    echo "Error: Git is not installed." >&2
    echo "Please install git and make sure you pull this repository directly using git!"
    exit
fi

echo "Checking out external libs..."
git submodule update --init --recursive
echo "Copy everything to the lib directory..."
cp source/extern/*.py source/lib/

echo "Done."
echo "This project is managed using uv. Carefully read the README.md!"

