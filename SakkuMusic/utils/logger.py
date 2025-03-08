from pyrogram.enums import ParseMode

from SakkuMusic import app
from SakkuMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} Play Log</b>

<b>Qrup ID:</b> <code>{message.chat.id}</code>
<b>Qrup Adı:</b> {message.chat.title}
<b>Qrup linki:</b> @{message.chat.username}

<b>İstifadəçi ID:</b> <code>{message.from_user.id}</code>
<b>Adı:</b> {message.from_user.mention}
<b>İstifadəçi Adı:</b> @{message.from_user.username}

<b>Tələbi:</b> {message.text.split(None, 1)[1]}
<b>Platform:</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return