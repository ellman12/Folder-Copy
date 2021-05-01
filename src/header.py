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


def help():
    print(f"{colors.OKCYAN}-----------------------\nFolder Copy (FC) V. 1.0\n-----------------------\nCommand Line Args\n-----------------------\nNo args\t\tCopy folders\nhelp\t\tShows this\nadd <dir>\tAdd <dir> to dirs.txt\nrm <dir>\tRemove <dir>\nls\t\tList dirs\nclr\t\tClear the dirs.txt file")
    print(f"cp <dir>\tIf no <dir> arg given, copy to default dir. If arg given, copy there instead{colors.ENDC}")


def copyDirs(dirs: list[pathlib.PurePath], bakLoc: str):
    if (bakLoc == ""):
        bakLoc = input("Please enter a location: ")

    bakLoc = bakLoc / ("fc Backup " + time.strftime("%Y-%m-%d %H;%M;%S"))

    print(f"{colors.OKCYAN}Copying folders/files to {bakLoc}{colors.ENDC}\n")
    for dir in dirs:
        print(f"{colors.OKCYAN}Copying {dir}{colors.ENDC}", end="")
        try:
            shutil.copytree(dir, bakLoc / dir.name)
            print(f"{colors.OKGREEN}\t✓ copied{colors.ENDC}")
        except:
            print(f"{colors.FAIL}\nAn error occurred while trying to copy {dir} to {bakLoc / dir.name}{colors.ENDC}")
            exit()


def listDirs(dirs):
    i = 0
    print("\n")
    for dir in dirs:
        i += 1
        print(f"{colors.OKCYAN}{i}: {dir}{colors.ENDC}")
    print("\n")
