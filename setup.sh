#!/bin/bash

# Function to check if a command exists
command_exists() {
    type "$1" &> /dev/null
}

# Update PATH for the current session to include user-installed binaries
update_path() {
    export PATH="$HOME/.local/bin:$PATH"
}

# Check if Python 3 is installed
if command_exists python3; then
    echo "Python 3 is installed."

    # Check if pip is installed
    if command_exists pip3; then
        echo "pip3 is already installed."
    else
        echo "Attempting to install pip3 (requires sudo access)..."
        sudo apt update
        sudo apt install python3-pip -y
    fi

    # Check if pipenv is installed
    if command_exists pipenv; then
        echo "Pipenv is already installed."
    else
        echo "Installing pipenv..."
        python3 -m pip install --user pipenv
        update_path  # Update PATH for pipenv
    fi

    # Set PIPENV_VENV_IN_PROJECT to create the virtual environment in the project directory
    export PIPENV_VENV_IN_PROJECT=1

    # Install dependencies using pipenv
    echo "Installing dependencies from Pipfile..."
    pipenv install

    echo "Setup complete."
else
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi
