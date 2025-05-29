from telegram import ReplyKeyboardMarkup  
from telegram.ext import CommandHandler  
from config import BOT_DESCRIPTION  
from services.translator import LibreTranslator  
from services.text_utils import format_translation  

translator = LibreTranslator("https://translate.argosopentech.com")  

def get_main_menu():  
    keyboard = [  
        ["/id_ar Terjemah ID→AR", "/ar_id Terjemah AR→ID"],  
        ["/help", "/about"]  
    ]  
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)  

def start(update, context):  
    update.message.reply_text(  
        BOT_DESCRIPTION,  
        reply_markup=get_main_menu(),  
        parse_mode="Markdown"  
    )  

def help_command(update, context):  
    update.message.reply_text(  
        "🔷 **Cara Pakai Bot** 🔷\n\n"  
        "1. Kirim teks dalam bahasa Indonesia/Arab untuk terjemahan otomatis\n"  
        "2. Atau gunakan perintah:\n"  
        "/id_ar [teks] → Terjemah Indonesia-Arab\n"  
        "/ar_id [teks] → Terjemah Arab-Indonesia\n\n"  
        "Contoh: `/id_ar Selamat pagi`",  
        parse_mode="Markdown"  
    )  

def about(update, context):  
    update.message.reply_text(  
        "🤖 **Bot Penerjemah ID-AR**\n\n"  
        "Versi: 1.0\n"  
        "Menggunakan LibreTranslate (gratis)\n"  
        "Hosting: Railway.app",  
        reply_markup=get_main_menu()  
    )  

def translate_id_ar(update, context):  
    text = " ".join(context.args)  
    if not text:  
        update.message.reply_text("Contoh: /id_ar Selamat pagi")  
        return  

    translation = translator.translate_id_to_ar(text)  
    if translation:  
        update.message.reply_text(  
            format_translation(text, translation, "Indonesia", "Arab"),  
            parse_mode="Markdown"  
        )  
    else:  
        update.message.reply_text("⚠️ Gagal menerjemahkan.")  

def translate_ar_id(update, context):  
    text = " ".join(context.args)  
    if not text:  
        update.message.reply_text("Contoh: /ar_id صباح الخير")  
        return  

    translation = translator.translate_ar_to_id(text)  
    if translation:  
        update.message.reply_text(  
            format_translation(text, translation, "Arab", "Indonesia"),  
            parse_mode="Markdown"  
        )  
    else:  
        update.message.reply_text("⚠️ Gagal menerjemahkan.")  

def setup_command_handlers(dispatcher):  
    dispatcher.add_handler(CommandHandler("start", start))  
    dispatcher.add_handler(CommandHandler("help", help_command))  
    dispatcher.add_handler(CommandHandler("about", about))  
    dispatcher.add_handler(CommandHandler("id_ar", translate_id_ar))  
    dispatcher.add_handler(CommandHandler("ar_id", translate_ar_id))  