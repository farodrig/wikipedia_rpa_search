# Robotic Researcher

Welcome to Robotic Researcher. This software allows you to extract some basic information from someone using the Wikipedia webpage.

## Prerequisites

- :snake: Python 3.11.1 and poetry
- Chrome Driver / Gecko Driver (Selenium)

## Environment Variables

- WIKIPEDIA_URL: URL for wikipedia site used to extract information. Default: 'https://en.wikipedia.org/'


## How to run

```
poetry install
poetry shell
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
poetry run pytest .
```

## Run coverage
```
poetry run pytest --cov-report=xml --cov=src src # To get the report
poetry run pytest --cov=src src # Without the report
```