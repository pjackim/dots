#!/usr/bin/env python3
from customlibs import PrintUtil
from customlibs import RofiUtil
from subprocess import Popen, PIPE, run
import argparse
import sys
import os
import logging


def execute(file):
    extension = os.path.splitext(file)[1]
    executor = ""
    if extension == ".py":
        executor = "python3"
    elif extension == ".sh":
        executor = "bash"
    elif extension == ".bat":
        executor = "cmd"
    
    pb = Popen([executor, file], stdout=PIPE, stderr=PIPE)
    


#logging.basicConfig(filename='./error_log.txt', level=logging.ERROR, format='%(asctime)s %(message)s')
try:
    f = "/home/pjackim/coding/personal/scripting"
    if len(sys.argv) == 2:
        f = sys.argv[1]

    file = RofiUtil.SelectFile(f, skip=os.path.basename(__file__))
    print(file)
    if os.path.isfile(file):
        execute(file)
except Exception as e:
    pass
