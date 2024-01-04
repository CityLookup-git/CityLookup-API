# CityLookup API

## Overview
CityLookup API is the Python-based backend portion of CityLookup. It is responsible for processing address datasets and optimized for GeoJSON datasets from OpenAddresses.

## Prerequisites
- Python 3

## Installation
1. Run `setup.sh` to install necessary dependencies. This script checks for Python 3, installs pip3 if not present, and sets up pipenv to manage project dependencies.

## Usage
### Setting Up Data
Place your GeoJSON datasets in the 'datasets' folder.

### Running the Application
- To run the application, use the command: `pipenv run python app.py`

### Testing
- For testing, use the command: `pipenv run pytest test.py`

## Contributing
Contributions are welcome! For any improvements or issues, please open a pull request or issue.
