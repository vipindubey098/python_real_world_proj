#importing python modules psutil

import psutil

cpu = psutil.cpu_count()
print(cpu)
while True:
    cpu_percent = psutil.cpu_percent(1)
    print(cpu_percent)