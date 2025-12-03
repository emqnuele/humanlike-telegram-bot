import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from bot.ai import generate_response
from bot.utils import calculate_typing_delay

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How can i help?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text
    chat_type = update.message.chat.type
    bot_username = context.bot.username

    should_respond = False

    if chat_type == 'private':
        should_respond = True
    else:
        # Group logic
        if bot_username and f"@{bot_username}" in text:
            should_respond = True
        elif "bot" in text.lower():
            should_respond = True
        elif update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
            should_respond = True

    if should_respond:
        # Generate response (this might take a moment, so show typing initially)
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
        response = generate_response(update.effective_chat.id, text)
        
        # Split response by newlines and filter empty strings
        messages = [msg.strip() for msg in response.split('\n') if msg.strip()]
        
        for msg in messages:
            # Calculate delay for this specific message
            delay = calculate_typing_delay(msg)
            
            # Show typing action while "typing" the message
            await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
            await asyncio.sleep(delay)
            
            # Send the message part
            await update.message.reply_text(msg)
