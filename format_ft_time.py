import time
from datetime import datetime, timezone

timestamp = time.time()
print(
    f"Seconds since January 1, 1970: {timestamp:,.4f} "
    f"or {timestamp:.2e} in scientific notation"
)
date = datetime.now(timezone.utc).strftime("%Y %B %d")
print(date)
