from pyrogram.filters import create
from pyrogram.enums import MessageEntityType
from re import match
import os

AUTO_BYPASS = bool(os.getenv("AUTO_BYPASS", "False") == "True")

async def auto_bypass(_, c, message):
    if (
        AUTO_BYPASS
        and message.entities
        and not match(r"^\/(bash|shell)($| )", message.text)
        and any(
            enty.type in [MessageEntityType.TEXT_LINK, MessageEntityType.URL]
            for enty in message.entities
        )
    ):
        return True
    elif (
        not AUTO_BYPASS
        and (txt := message.text)
        and match(rf"^\/(bypass|bp)(@{c.me.username})?($| )", txt)
        and not match(r"^\/(bash|shell)($| )", txt)
    ):
        return True
    return False


BypassFilter = create(auto_bypass)

# Bypass function for auto bypass checking (from your previous code)
async def auto_bypass1(_, c, message):
    """
    Auto-bypass filter function to check if a message contains valid links
    or commands for auto-bypass handling.
    """
    # Check if AUTO_BYPASS is enabled and message contains valid entities
    if (
        AUTO_BYPASS
        and message.entities
        and not match(r"^\/(bash|shell)($| )", message.text)
        and any(
            entity.type in [MessageEntityType.TEXT_LINK, MessageEntityType.URL]
            for entity in message.entities
        )
    ):
        return True

    # Check for manual commands to trigger the bypass function
    if (
        not AUTO_BYPASS
        and (txt := message.text)
        and match(rf"^\/(st|send_torrents|sendtorrents)(@{c.me.username})?($| )", txt)
        and not match(r"^\/(bash|shell)($| )", txt)
    ):
        return True

    # If no conditions are met, return False
    return False

BypassFilter1 = create(auto_bypass1)

async def auto_bypass2(_, c, message):
    """
    Auto-bypass filter function to check if a message contains valid links
    or commands for auto-bypass handling.
    """
    # Check if AUTO_BYPASS is enabled and message contains valid entities
    if (
        AUTO_BYPASS
        and message.entities
        and not match(r"^\/(bash|shell)($| )", message.text)
        and any(
            entity.type in [MessageEntityType.TEXT_LINK, MessageEntityType.URL]
            for entity in message.entities
        )
    ):
        return True

    # Check for manual commands to trigger the bypass function
    if (
        not AUTO_BYPASS
        and (txt := message.text)
        and match(rf"^\/(sm|send_magnets|sendmagnets)(@{c.me.username})?($| )", txt)
        and not match(r"^\/(bash|shell)($| )", txt)
    ):
        return True

    # If no conditions are met, return False
    return False

BypassFilter2 = create(auto_bypass2)
# Send Torrent link to group 

async def auto_bypassg(_, c, message):
    """
    Auto-bypass filter function to check if a message contains valid links
    or commands for auto-bypass handling.
    """
    # Check if AUTO_BYPASS is enabled and message contains valid entities
    if (
        AUTO_BYPASS
        and message.entities
        and not match(r"^\/(bash|shell)($| )", message.text)
        and any(
            entity.type in [MessageEntityType.TEXT_LINK, MessageEntityType.URL]
            for entity in message.entities
        )
    ):
        return True

    # Check for manual commands to trigger the bypass function
    if (
        not AUTO_BYPASS
        and (txt := message.text)
        and match(rf"^\/(al|auto_leech|autoleech)(@{c.me.username})?($| )", txt)
        and not match(r"^\/(bash|shell)($| )", txt)
    ):
        return True

    # If no conditions are met, return False
    return False

BypassFilterg = create(auto_bypassg)

def convert_time(seconds):
    mseconds = seconds * 1000
    periods = [("d", 86400000), ("h", 3600000), ("m", 60000), ("s", 1000), ("ms", 1)]
    result = ""
    for period_name, period_seconds in periods:
        if mseconds >= period_seconds:
            period_value, mseconds = divmod(mseconds, period_seconds)
            result += f"{int(period_value)}{period_name}"  # Removed space between value and period_name
    if result == "":
        return "0ms"
    return result
