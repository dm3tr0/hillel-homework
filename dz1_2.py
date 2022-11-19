#!/usr/bin/python

import subprocess

task_a = subprocess.run(['cp', 'dz1_1.py', 'dz1_run.py'])

task_c = subprocess.run(['chmod', 'ug-rwx', 'dz1_1.py'])

task_d = subprocess.run(['python3', 'dz1_run.py'])