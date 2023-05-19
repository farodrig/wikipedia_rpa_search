import os
from pathlib import Path
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **os.environ,  # override loaded values with environment variables
}

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]
SRC_PATH = Path(__file__).parent
PROJECT_PATH = SRC_PATH.parent
