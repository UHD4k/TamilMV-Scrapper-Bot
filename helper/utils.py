import math, time
from datetime import datetime
from pytz import timezone
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001821439025"))

async def send_log(b, u):
    if LOG_CHANNEL is not None:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime('%d %B, %Y')
        time = curr.strftime('%I:%M:%S %p')
        await b.send_message(
            LOG_CHANNEL,
            f"**#New_User\n\n᚛› Name :- {u.mention}\n᚛› ID :- `{u.id}`\n᚛› Date :- {date}\n᚛› Time :- {time}\n\n᚛› From Bot :- {b.mention}**"
        )
