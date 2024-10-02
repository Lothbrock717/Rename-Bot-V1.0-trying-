import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26444821")

API_HASH = os.environ.get("API_HASH", "a58efd1d6483e3f0d5b2757d9f665c24")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6850113253:AAGVAqUX4Q73TvgycRd6Mx3lggX5ezIOvxg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "WebXBots") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://abhay:store@store.nmvpb5w.mongodb.net/?retryWrites=true&w=majority&appName=STORE")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1581901379').split()]

PORT = os.environ.get("PORT", "8080")
