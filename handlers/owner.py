from pyrogram import filters
from config import OWNER_ID

def register_owner_handler(app):
    @app.on_message(filters.command("ping"))
    async def ping_cmd(client, message):
        if message.from_user.id != OWNER_ID:
            return
        await message.reply_text("✅ Bot alive (Owner only)")
