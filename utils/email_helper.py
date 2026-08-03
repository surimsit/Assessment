import re
import time
from datetime import datetime, timezone

from imap_tools import MailBox


class EmailHelper:

    @staticmethod
    def get_latest_otp(
            email,
            password,
            received_after,
            imap_server="imap.gmail.com",
            timeout=90
    ):

        start_time = time.time()

        while time.time() - start_time < timeout:

            with MailBox(imap_server).login(
                    email,
                    password
            ) as mailbox:

                for msg in mailbox.fetch(reverse=True, limit=20):

                    msg_time = msg.date

                    if msg_time.tzinfo is None:
                        msg_time = msg_time.replace(
                            tzinfo=timezone.utc
                        )

                    if msg_time <= received_after:
                        continue

                    body = msg.text or msg.html or ""

                    match = re.search(
                        r"\b(\d{6})\b",
                        body
                    )

                    if match:
                        return match.group(1)

            time.sleep(5)

        raise Exception("New OTP not received")