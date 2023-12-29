from datetime import datetime
import time

t = datetime.now()
time.sleep(1)

t1 = datetime.now()

print((t1-t).total_seconds())