# CityLookup API

## Overview
CityLookup API is the Python-based backend portion of CityLookup. It is responsible for processing address datasets and optimized for GeoJSON datasets from OpenAddresses.

## Prerequisites
- Python 3

## Installation

### Cloning the Repository
You have two options for cloning:

- To clone all CityLookup components at once:

  `git clone https://github.com/CityLookup-git/CityLookup`

If cloned like this, CityLookup API will be located inside the `api` folder.

- To clone only the CityLookup API:

  `git clone https://github.com/CityLookup-git/CityLookup-API.git`

### Environment Setup
1. Navigate into the project directory
2. Run `setup.sh` to install necessary dependencies. This script checks for Python 3, installs pip3 if not present, and sets up pipenv to manage project dependencies.

## Usage

### Setting Up Data
1. Download datasets marked as 'addresses' from OpenAddresses: [OpenAddresses Data](https://batch.openaddresses.io/data)
2. Place your downloaded GeoJSON datasets in the 'datasets' folder.

### Running the Application
- To run the application, use the command: `pipenv run python app.py`

### Testing
- For testing, use the command: `pipenv run pytest test.py`

## Contributing
Contributions are welcome! For any improvements or issues, please open a pull request or issue.
