import os  
from dotenv import load_dotenv  

load_dotenv()  

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN tidak ditemukan di environment variables")
 
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
