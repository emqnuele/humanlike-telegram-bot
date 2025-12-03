import threading
import asyncio
from web.app import run_flask
from bot.core import create_bot

def main():
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    print("Flask server started on port 5000")

    # Start Telegram Bot
    print("Starting Telegram Bot...")
    try:
        app = create_bot()
        app.run_polling()
    except Exception as e:
        print(f"Error starting bot: {e}")

if __name__ == "__main__":
    main()
