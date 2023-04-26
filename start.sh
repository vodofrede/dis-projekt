#!/bin/bash

if test -d ".venv"; then
    # source venv
    source ./.venv/bin/activate
else
    echo "setting up environment..."

    # determine folder
    if ! test -f "requirements.txt"; then
        echo "please run this command from the project root folder."
        exit 1
    fi

    # create venv
    python3 -m venv .venv

    # source venv
    source ./.venv/bin/activate

    # install requirements
    python -m pip install --upgrade pip
    pip install -r requirements.txt
fi

# init/upgrade db
flask --app src/app.py db upgrade

# run app
flask --app src/app.py run --debug --extra-files assets/