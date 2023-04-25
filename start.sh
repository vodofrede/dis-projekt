#!/bin/bash

if test -d ".venv/linux"; then
    # source venv
    source ./.venv/linux/bin/activate
else
    echo "setting up environment..."

    # determine folder
    if ! test -f "requirements.txt"; then
        echo "please run this command from the project root folder."
        exit 1
    fi

    # create venv
    python3 -m venv .venv/linux

    # source venv
    source ./.venv/linux/bin/activate

    # install requirements
    pip install -r requirements.txt
fi

# run app
flask --app src/app.py --debug run