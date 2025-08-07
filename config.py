import os
from dotenv import load_dotenv
import getpass

def load_config():
    """Load environment variables and prompt for Google API key if not set."""
    load_dotenv()
    if not os.environ.get("GOOGLE_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Gemini API Key: ")
    return os.environ["GOOGLE_API_KEY"]