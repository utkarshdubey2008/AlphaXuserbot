#!/usr/bin/env python3
# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")
APP_ID = int(os.environ.get("19500615", None))
API_HASH = os.environ.get("7ee1d55d072add75a01e617fc0cef635", None)

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
