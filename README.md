# Robotic Researcher

Welcome to Quandri's Robotic Researcher. This software allows you to extract some basic information from someone using wikipedia webpage.

## Prerequisites

- :snake: Python 3.11.1
- Chrome Driver / Gecko Driver (Selenium)


## Installation

```
python -m venv venv # Optional
source venv/bin/activate # Optional
pip install -r requirements.txt
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

For an explanation on how to use them run:
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