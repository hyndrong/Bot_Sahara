def is_arabic(text):  
    arabic_chars = set("ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىي")  
    return any(char in arabic_chars for char in text)  

def format_translation(source, translation, source_lang, target_lang):  
    return f"""  
🔹 **{source_lang}:**  
`{source}`  

🔸 **{target_lang}:**  
`{translation}`  
"""  