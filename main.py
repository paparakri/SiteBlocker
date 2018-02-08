import time
from datetime import datetime as dt
import os

path = os.path.realpath(__file__)[:-7]
file = open('{}setup.txt'.format(path), 'r')

file_ar = file.readlines()

length = int(file_ar[0])
time1  = int(file_ar[1])
time2  = int(file_ar[2])
print(length)
print(time1)
print(time2)

website_list = []
for i in range(0,length):
    website_list.append(file_ar[i+3])
    print(website_list[i])

hosts_path = "/etc/hosts"
redirect = "194.30.242.10"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22):
        with open(hosts_path, "r+") as file:
            content = file .read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(10)
