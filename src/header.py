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

    print(f"{colors.OKGREEN}Copying folders/files to {bakLoc}")
    for dir in dirs:
        try:
            shutil.copytree(dir, bakLoc / dir.name)
            print(f"{colors.OKGREEN}{dir}copied {colors.ENDC}")
        except:
            print(f"{colors.FAIL}An error occurred while trying to copy {dir} to {bakLoc / dir.name}{colors.ENDC}")


def listDirs(dirs):
    i = 0
    for dir in dirs:
        i += 1
        print(f"Dir #{i}:\t{dir}")