import os  
from dotenv import load_dotenv  

load_dotenv()  

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  
LIBRE_TRANSLATE_URL = os.getenv("LIBRE_TRANSLATE_URL")  

BOT_DESCRIPTION = """  
🕌 **Bot Penerjemah Indonesia-Arab** 🕌  

🔹 **Fitur:**  
- Terjemahkan Indonesia → Arab  
- Terjemahkan Arab → Indonesia  
- Deteksi otomatis bahasa  

🔸 **Perintah:**  
/start - Mulai bot  
/help - Tampilkan bantuan  
/id_ar [teks] - Terjemahkan ID→AR  
/ar_id [teks] - Terjemahkan AR→ID  
/about - Tentang bot  
"""  