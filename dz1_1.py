#!/usr/bin/python

import subprocess, os, random
from datetime import timedelta, date

arr = []
date_format = '%d.%m.%Y'
today = date(2022, 11, 1)
for i in range(30):
    arr.append((today+timedelta(days=i)).strftime(date_format))

task_a = subprocess.run('whoami')

task_b = subprocess.run('pwd')

task_c = subprocess.run(['mkdir', 'dz1'])

os.chdir("dz1")

for y in range(len(arr)):
    task_d = subprocess.run(['touch', f'{arr[y]}.log'])

os.chdir("..")

task_e = subprocess.run(['sudo', 'chown', 'root:root', 'dz1'])

os.chdir("dz1")

for y in range(6):
    choice = random.choice(arr)
    task_f = subprocess.run(['rm', f'{choice}.log'])
    arr.remove(choice)