import shutil
import sys
import time
import os


def copyDirs(dirs: str, bakLoc: str):
    if (bakLoc == ""):
        bakLoc = input("Please enter a location: ")

    bakLoc += "\\fc Backup " + time.strftime("%Y-%m-%d %H;%M;%S")

    for dir in dirs:
        for subDir, _, files in os.walk(dir):
            for file in files:
                newLocation = bakLoc + '\\' + file
                if not os.path.exists(bakLoc):
                    os.makedirs(bakLoc)
                shutil.copy(subDir + '/' + file, newLocation)

def listDirs(dirs):
    i = 0
    for dir in dirs:
        i += 1
        print(f"Dir #{i}:\t{dir}")


with open(os.environ["APPDATA"] + "/fc/fc.conf", 'r') as conf:
    for i, line in enumerate(conf):
        if "Default Copy Location:" in line:
            cpLoc = line[23:]  # Where folders are copied

with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'r') as dirstxt:
    dirs = [line.rstrip() for line in dirstxt]
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
