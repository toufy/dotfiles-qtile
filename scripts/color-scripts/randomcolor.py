#!/bin/python3
import pathlib
import random
import os
import subprocess
homedir = os.getenv("HOME")
curr_file = pathlib.Path(__file__).parent.resolve()
script = random.choice([i for i in os.listdir(curr_file) if i != 'randomcolor.py'])
subprocess.run(f"{homedir}/scripts/color-scripts/{script}")
