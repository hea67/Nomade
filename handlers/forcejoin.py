from pyrogram import filters
from config import UPDATE_CHANNEL

def register_forcejoin_handler(app):
    @app.on_message(filters.private)
    async def force_join(client, message):
        try:
            await client.get_chat_member(UPDATE_CHANNEL, message.from_user.id)
        except:
            await message.reply_text(
                f"🚫 Pehle channel join karo:\n{UPDATE_CHANNEL}"
            )
            return
