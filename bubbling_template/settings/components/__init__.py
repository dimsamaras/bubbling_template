
from pathlib import PurePath
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR.joinpath('some')
# `pathlib` is better than writing: dirname(dirname(dirname(__file__)))
BASE_DIR = PurePath(__file__).parent.parent.parent.parent

# https://github.com/theskumar/python-dotenv
load_dotenv()
