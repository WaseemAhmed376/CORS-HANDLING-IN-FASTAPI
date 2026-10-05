import os 
from dotenv import load_dotenv
load_dotenv()
class settings:
    origins = [os.getenv("ORIGINS")]
    SECRET_KEY = os.getenv("SECRET_KEY")
    DB_URL = os.getenv("DB_URL")
settings=settings()
 
