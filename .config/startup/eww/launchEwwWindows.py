#!/usr/bin/env python3


# Requires commands.json and eww_windows.json
#   commands.json is a list of commands/startup windows to be executed
#   eww_windows.json is a list of eww containers to be started

import argparse
import os
import json
from subprocess import Popen, PIPE, run
from time import sleep

def execute_command(command, args=[], get_result=False):
    if get_result:
        if len(args) > 0:
            for arg in args:
                command += ' ' + arg
        return run(command, stdout=PIPE, stderr=PIPE, text=True, shell=True).stdout.strip()
    return run([command, *args], capture_output=True, text=True)

def get_node_name(node_id):
    try:
        return execute_command('xtitle', [str(node_id)]).stdout.strip()
    except Exception as e:
        print(f"Error getting node name: {e}")
        return ""


def get_instances(file):
    with open(f"{current_dir}/{file}", "r") as f:
        data = json.load(f)
    return data


parser = argparse.ArgumentParser(description='Process command line arguments')

# Add the command-line arguments
parser.add_argument('-s', action='store_true', help='Start the program')
parser.add_argument('--start-up', action='store_true', help='Start the program')
parser.add_argument('-k', action='store_true', help='Kill the program')
parser.add_argument('--shutdown', action='store_true', help='Kill the program')

# Parse the arguments
args = parser.parse_args()

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get ID of the currently focused node
current_node = execute_command('bspc query', ['--nodes', '--node', 'focused'], get_result=True)

# Check the arguments
if args.s or args.start_up:
    print('Starting the program...')
    
    ewwContainers = get_instances("eww_windows.json")
    for container in ewwContainers:
        execute_command(f"eww", ["open", container, "&"], get_result=True)
    
    
    windows = get_instances("commands.json")
    for win in windows:
        p = Popen(win, stdout=PIPE, stderr=PIPE, shell=False)

    sleep(1)
    pb = Popen(['bspc', 'query', '-N'], stdout=PIPE, stderr=PIPE)
    try:
        stdout, stderr = pb.communicate(timeout=1)
        nodes = stdout.decode().strip().split("\n")

        for node in nodes:
            name = get_node_name(node)
            if "Desktop" in name or "lichess" in name:
                os.system(f"bspc node {node} --flag sticky=on")
                print(node, name, "---- Desktop:", sep="\t")
            elif len(name) > 0:
                print(name)
                
    except Exception as e:
        print(f"Error processing nodes: {e}")
        
elif args.k or args.shutdown:
    print('Killing the program...')
    
    execute_command("killall", ["eww"], get_result=True)
    
    
    windows = get_instances("commands.json")
    for window in windows:
        execute_command("xdo", ["kill", "-n", str(window[2])[5:]])
        
else:
    print('No valid arguments provided.')

# Return focus to the initial window
execute_command('bspc', ['node', f'{current_node}', '--focus'])