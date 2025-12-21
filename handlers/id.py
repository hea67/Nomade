 from pyrogram import filters

def register_id_handler(app):
    @app.on_message(filters.command("id"))
    async def id_cmd(client, message):
        await message.reply_text(
            f"User ID: {message.from_user.id}\n"
            f"Chat ID: {message.chat.id}"
        ) 
