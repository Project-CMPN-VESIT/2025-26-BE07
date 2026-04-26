import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
MODEL1 = os.getenv("MODEL1")

# Individual API Keys

API_KEY_MINDMAP = os.getenv("API_KEY_MINDMAP")

def initialize_mindmap_client():
    return OpenAI(api_key=API_KEY_MINDMAP, base_url=BASE_URL)
