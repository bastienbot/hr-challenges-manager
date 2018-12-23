import os
from pathlib import Path
from dotenv import load_dotenv


dir_path = os.path.dirname(os.path.realpath(__file__))
env_path = Path(dir_path).parent / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)
