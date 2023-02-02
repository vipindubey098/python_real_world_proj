#import
# time
# psutil
# plyer


import time
import psutil
from plyer import notification

battery = psutil.sensors_battery()
percent = battery.percent

notification.notify(
    title = 'Battery Percentage',
    message = str(percent),
    timeout = 20
)