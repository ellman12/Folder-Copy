import shutil
import sys
import time
import os
import pathlib


class colors:  # https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def copyDirs(dirs: list[pathlib.PurePath], bakLoc: str):
    if (bakLoc == ""):
        bakLoc = input("Please enter a location: ")

    bakLoc = bakLoc / ("fc Backup " + time.strftime("%Y-%m-%d %H;%M;%S"))

    for dir in dirs:
        try:
            shutil.copytree(dir, bakLoc / dir.name)
            print(f"{colors.OKGREEN}{dir}\t->\t{bakLoc / dir.name}{colors.ENDC}")
        except:
            print(f"{colors.FAIL}An error occurred while trying to copy {dir} to {bakLoc / dir.name}{colors.ENDC}")


def listDirs(dirs):
    i = 0
    for dir in dirs:
        i += 1
        print(f"Dir #{i}:\t{dir}")


with open(os.environ["APPDATA"] + "/fc/fc.conf", 'r') as conf:
    for i, line in enumerate(conf):
        if "Default Copy Location:" in line:
            cpLoc = pathlib.PurePath(line[23:])  # Where folders are copied

with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'r') as dirstxt:
    dirs = [pathlib.PurePath(line.rstrip()) for line in dirstxt]
    dirstxt.close()

if (len(sys.argv) == 1):
    copyDirs(dirs, cpLoc)
    exit()

elif (sys.argv[1] == "cp"):
    copyDirs(dirs, cpLoc)
    exit()

elif (sys.argv[1] == "add"):
    try:
        for dir in dirs:  # Check for duplicates
            if sys.argv[2] == dir:
                print(f"{sys.argv[2]} is already in the file!")
                exit()

        dirs.append(sys.argv[2])
        with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'a') as dirstxt:
            for dir in dirs:
                dirstxt.write(dir + '\n')
    except IndexError:
        print("'add' requires a directory")
        exit()

elif (sys.argv[1] == "ls"):
    listDirs(dirs)
    exit()

elif (sys.argv[1] == "clr"):
    with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'w') as dirstxt:
        dirstxt.write("")

else:
    print(f"Unknown command: '{sys.argv[1]}'")
