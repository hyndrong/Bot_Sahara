import logging  
from telegram.ext import Updater, Application 
from config import TELEGRAM_TOKEN  
from handlers.command_handler import setup_command_handlers  
from handlers.message_handler import setup_message_handlers  

logging.basicConfig(  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    level=logging.INFO  
)  
logger = logging.getLogger(__name__)  
async def post_init(app):
    logging.info("Bot berjalan dengan baik...")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).post_init(post_init).build()
    
    from handlers.command_handler import setup_command_handlers
    from handlers.message_handler import setup_message_handlers
    
    setup_command_handlers(app)
    setup_message_handlers(app)
    
    app.run_polling()

if __name__ == '__main__':
    main()
