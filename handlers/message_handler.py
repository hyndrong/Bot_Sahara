from telegram.ext import MessageHandler, filters  
from services.translator import LibreTranslator  
from services.text_utils import is_arabic, format_translation  

translator = LibreTranslator("https://translate.argosopentech.com")  

def handle_text_message(update, context):  
    text = update.message.text  
    if not text:  
        return  

    if is_arabic(text):  
        translation = translator.translate_ar_to_id(text)  
        if translation:  
            update.message.reply_text(  
                format_translation(text, translation, "Arab", "Indonesia"),  
                parse_mode="Markdown"  
            )  
        else:  
            update.message.reply_text("⚠️ Gagal menerjemahkan Arab→Indonesia.")  
    else:  
        translation = translator.translate_id_to_ar(text)  
        if translation:  
            update.message.reply_text(  
                format_translation(text, translation, "Indonesia", "Arab"),  
                parse_mode="Markdown"  
            )  
        else:  
            update.message.reply_text("⚠️ Gagal menerjemahkan Indonesia→Arab.")  

def setup_message_handlers(dispatcher):  
    dispatcher.add_handler(  
        MessageHandler(filters.text & ~filters.command, handle_text_message)  
    )  
