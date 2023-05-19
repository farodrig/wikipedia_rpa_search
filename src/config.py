import os
from pathlib import Path

from dotenv import dotenv_values
from yarl import URL

env_vars = {
    **dotenv_values(".env"),
    **os.environ,  # override loaded values with environment variables
}

WIKIPEDIA_URL = URL(env_vars.get('WIKIPEDIA_URL', 'https://en.wikipedia.org/'))
SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]
SRC_PATH = Path(__file__).parent
PROJECT_PATH = SRC_PATH.parent
