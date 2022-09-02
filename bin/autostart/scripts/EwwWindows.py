#! /bin/python3
def getWindows():
    windows = [
        ['konsole', '-p', 'name=clear-m3-1', '--name', 'clear-m3-1', '--profile', 'Clear', '-e', 'applicationLauncher', 'thokr', '&'],
        ['konsole', '-p', 'name=clear-m2-2', '--name', 'clear-m2-2', '--profile', 'Clear', '-e', 'applicationLauncher', 'sssnake -S -s 10 -f -j 5','&'],
        ['konsole', '-p', 'name=clear-m1', '-p', 'font=Iosevka,10', '--name', 'clear-m1', '--profile', 'Clear', '-e', 'applicationLauncher', 'neofetch', '&'],
        ['konsole', '-p', 'name=clear-m2-1', '--name', 'clear-m2-1', '--profile', 'Clear','-e', 'applicationLauncher', 'ssh laptop','&']
    ]
    return windows

