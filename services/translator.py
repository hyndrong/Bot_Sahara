import requests  
import logging  

logger = logging.getLogger(__name__)  

class LibreTranslator:  
    def __init__(self, base_url):  
        self.base_url = base_url  

    def translate(self, text, source_lang, target_lang):  
        try:  
            response = requests.post(  
                f"{self.base_url}/translate",  
                json={  
                    "q": text,  
                    "source": source_lang,  
                    "target": target_lang  
                },  
                headers={"Content-Type": "application/json"}  
            )  
            response.raise_for_status()  
            return response.json().get("translatedText", "")  
        except Exception as e:  
            logger.error(f"Terjemahan gagal: {e}")  
            return None  

    def translate_id_to_ar(self, text):  
        return self.translate(text, "id", "ar")  

    def translate_ar_to_id(self, text):  
        return self.translate(text, "ar", "id")  