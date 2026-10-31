import os
from dotenv import load_dotenv
load_dotenv()
app_name=os.getenv("APP_NAME")
api_key=os.getenv("API_KEY")
print("App name is:",app_name)
print("API key:",api_key is not None)

