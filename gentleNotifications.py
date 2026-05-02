import json
import time
from datetime import datetime
from winotify import Notification

with open("notifications.json", "r", encoding="utf-8") as f:
    notifications = json.load(f)

shown_today = set()
current_day = datetime.now().date()

def show_notification(title, message):
    toast = Notification(
        app_id="Gentle notifications",
        title=title,
        msg=message,
        duration="short"
    )
    toast.show()

# Show startup notifications once when the script starts
for notif in notifications:
    if notif.get("startup") is True:
        show_notification(notif["title"], notif["message"])

while True:
    now = datetime.now()

    if now.date() != current_day:
        shown_today.clear()
        current_day = now.date()

    current_time = now.strftime("%H:%M")

    for notif in notifications:
        if "time" not in notif:
            continue

        notif_id = f"{current_day}-{notif['time']}"

        if notif["time"] == current_time and notif_id not in shown_today:
            show_notification(notif["title"], notif["message"])
            shown_today.add(notif_id)

    time.sleep(30)