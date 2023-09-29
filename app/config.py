import os
from dotenv import load_dotenv

dotenv_path = r'../.env'
load_dotenv(dotenv_path)

class Config:
    API_KEY = os.environ.get('SEMANTIC_SCHOLAR_API_KEY')


if os.environ.get('SEMANTIC_SCHOLAR_API_KEY') is None or os.environ.get('SEMANTIC_SCHOLAR_API_KEY') == '':
    SEMANTIC_API_KEY = None
else:
    SEMANTIC_API_KEY = os.environ.get('SEMANTIC_SCHOLAR_API_KEY')
