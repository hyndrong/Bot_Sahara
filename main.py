import logging  
from telegram.ext import Updater, Application 
from config import TELEGRAM_TOKEN  
from handlers.command_handler import setup_command_handlers  
from handlers.message_handler import setup_message_handlers  

load.dotenv()

logging.basicConfig(  
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  
    level=logging.INFO  
)  
logger = logging.getLogger(__name__)  
async def post_init(app):
    logging.info("Bot berjalan dengan baik...")

def main():
    try:
        # Get token from environment
        token = os.getenv('TELEGRAM_TOKEN')
        
        if not token:
            raise ValueError("TELEGRAM_TOKEN tidak ditemukan di environment variables")
        
        # Initialize application
        app = Application.builder().token(token).build()
        
        # Import and setup handlers
        from handlers.command_handler import setup_command_handlers
        from handlers.message_handler import setup_message_handlers
        
        setup_command_handlers(app)
        setup_message_handlers(app)
        
        logger.info("🤖 Bot starting...")
        app.run_polling()
        
    except Exception as e:
        logger.error(f"❌ Bot crashed: {e}")

if __name__ == '__main__':
    main()
