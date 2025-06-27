# Powered By Team DeadlineTech

import asyncio
import importlib

from pyrogram.types import BotCommand
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DeadlineTech import LOGGER, app, userbot
from DeadlineTech.core.call import Anony
from DeadlineTech.misc import sudo
from DeadlineTech.plugins import ALL_MODULES
from DeadlineTech.utils.database import get_banned_users, get_gbanned
from DeadlineTech.utils.crash_reporter import setup_global_exception_handler
from config import BANNED_USERS

async def init():
    # ✅ Enable global crash handler
    setup_global_exception_handler()

    # ✅ Check Assistant Strings
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()

    await sudo()

    # ✅ Load Banned Users
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()

    # ✅ Set Commands
    await app.set_bot_commands([
        BotCommand("start", "Start the bot"),
        BotCommand("clone", "Start your own bot"),
        BotCommand("ping", "Check bot is alive"),
        BotCommand("help", "Get command list"),
        BotCommand("music", "Download songs"),
        BotCommand("play", "Play music in VC"),
        BotCommand("vplay", "Stream video song"),
        BotCommand("playforce", "Force play song"),
        BotCommand("vplayforce", "Force play video"),
        BotCommand("pause", "Pause the stream"),
        BotCommand("resume", "Resume the stream"),
        BotCommand("skip", "Skip current song"),
        BotCommand("end", "End the stream"),
        BotCommand("player", "Interactive player"),
        BotCommand("queue", "Queued track list"),
        BotCommand("auth", "Add auth user"),
        BotCommand("unauth", "Remove auth user"),
        BotCommand("authusers", "List of auth users"),
        BotCommand("cplay", "Play on channel"),
        BotCommand("cvplay", "Video on channel"),
        BotCommand("channelplay", "Link channel"),
        BotCommand("shuffle", "Shuffle queue"),
        BotCommand("seek", "Seek stream"),
        BotCommand("seekback", "Seek back"),
        BotCommand("speed", "Adjust speed"),
        BotCommand("loop", "Loop song")
    ])

    # ✅ Import all plugin modules
    for all_module in ALL_MODULES:
        importlib.import_module("DeadlineTech.plugins." + all_module)

    LOGGER("DeadlineTech.plugins").info("Successfully Imported Modules...")

    await userbot.start()
    await Anony.start()

    # ✅ Start dummy stream to initiate VC
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("DeadlineTech").error(
            "Please start the videochat in your log group/channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass

    await Anony.decorators()
    LOGGER("DeadlineTech").info("DeadlineTech Music Bot started successfully")

    await idle()

    await app.stop()
    await userbot.stop()
    LOGGER("DeadlineTech").info("Stopping DeadlineTech Music Bot...")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
