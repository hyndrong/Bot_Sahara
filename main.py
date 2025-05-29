import logging  
from telegram.ext import Updater  
from config import TELEGRAM_TOKEN  
from handlers.command_handler import setup_command_handlers  
from handlers.message_handler import setup_message_handlers  

logging.basicConfig(  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    level=logging.INFO  
)  
logger = logging.getLogger(__name__)  

def main():  
    try:  
        updater = Updater(TELEGRAM_TOKEN, use_context=True)  
        dispatcher = updater.dispatcher  

        setup_command_handlers(dispatcher)  
        setup_message_handlers(dispatcher)  

        logger.info("🤖 Bot sedang berjalan...")  
        updater.start_polling()  
        updater.idle()  

    except Exception as e:  
        logger.error(f"❌ Bot crash: {e}")  

if __name__ == "__main__":  
    main()  