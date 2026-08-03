
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = "https://www.stumbleguys.com"
TEST_EMAIL = os.getenv("TEST_EMAIL")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")