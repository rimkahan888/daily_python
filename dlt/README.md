# DLT (Data Load Tool) Project

This project demonstrates the usage of DLT (Data Load Tool) for efficient data ingestion and transformation. The project specifically showcases integration with the PokeAPI as an example use case.

## Project Overview

This project is part of the Data Engineering Zoomcamp 2025, focusing on data ingestion techniques using DLT. It demonstrates how to:
- Extract data from REST APIs (specifically the PokeAPI)
- Transform and normalize the data
- Load it into a destination for further analysis

## Prerequisites

- Python 3.13.2 or higher
- Virtual environment management tool (venv)
- pip package manager

## Installation

1. Clone the repository or navigate to the project directory

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
venv\Scripts\activate  # On Windows
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
dlt/
├── README.md
├── dlttest1.py        # Main script for PokeAPI data ingestion
├── requirements.txt   # Project dependencies
└── venv/             # Virtual environment
```

## Usage

The main script `dlttest1.py` demonstrates how to use DLT to ingest data from the PokeAPI. To run the script:

```bash
python dlttest1.py
```

## Dependencies

The project's main dependencies are listed in `requirements.txt`. Key packages include:
- dlt
- requests
- Other supporting packages

## Development

To contribute to this project:

1. Create a new virtual environment
2. Install dependencies from requirements.txt
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

Refer to the LICENSE file in the project root directory.

## Acknowledgments

- Data Engineering Zoomcamp 2025
- PokeAPI for providing the example data source
- DLT team for the data ingestion framework