#!/usr/bin/env bash

# Run tests if no arguments are given
if [ $# -eq 0 ]; then
    poetry run pytest -s
fi

# Confirm test success
read -r -p "Did the tests run without errors? (y/n) " CONFIRM
if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
    echo "Aborting deployment"
    exit 1
fi

# Choose version bump level
read -r -p "What version bump level do you want to use? [major, minor, patch (default)] " BUMP_LEVEL
case "$BUMP_LEVEL" in
    major) poetry version major ;;
    minor) poetry version minor ;;
    ""|patch) poetry version patch ;;
    *) echo "Invalid bump level, defaulting to patch"; poetry version patch ;;
esac

VERSION=$(poetry version --short)
echo "Deploying version $VERSION to PyPI..."
read -r -p "Is this correct? (y/n) " CONFIRM
if [[ ! "$CONFIRM" =~ ^[Yy]$ ]]; then
    echo "Aborting deployment"
    exit 1
fi

# Load PyPI token from file
TOKEN=$(<"/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/ApiKeysAndPasswordFiles/pypi-token.txt")

# Publish to PyPI
poetry publish --build --username __token__ --password "$TOKEN"