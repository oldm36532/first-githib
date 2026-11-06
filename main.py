import sys
import os
from dotenv import load_dotenv
load_dotenv()
app_name=os.getenv("APP_NAME")
api_key=os.getenv("API_KEY")
if app_name is None:
    print("Error:APP NAME is None")
    sys.exit(1)
else:
    print("App name is:",app_name)
if api_key is None:
    print("Error:API KEY is None")
    sys.exit(1)
else:
    print("API key:",api_key is not None)

