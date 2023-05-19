# Robotic Researcher

Welcome to Quandri's Robotic Researcher. This software allows you to extract some basic information from someone using the Wikipedia webpage.

## Prerequisites

- :snake: Python 3.11.1
- Chrome Driver / Gecko Driver (Selenium)

## Environment Variables

- WIKIPEDIA_URL: URL for wikipedia site used to extract information. Default: 'https://en.wikipedia.org/'


## Installation

```
python -m venv venv # Optional
source venv/bin/activate # Optional
pip install -r requirements_dev.txt # If testing libraries are not needed, you can use the requirements.txt file
```

## How to run

```
cd src
python main.py
```

## Available commands

- find-wikipedia-people-by-name
- find-wikipedia-people-from-file
- find-wikipedia-person-by-name

For an explanation of how to use them, run:
```
python main.py [COMMAND] --help
```

## Run tests

```
pytest .
```

## Run coverage
```
pytest --cov-report=xml --cov=src src # To get the report
pytest --cov=src src # Without the report
```