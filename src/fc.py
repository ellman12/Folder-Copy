import sys
import os

# def copyDirs(dirs, location):


def listDirs(dirs):
    i = 0
    for dir in dirs:
        i += 1
        print(f"Dir #{i}:\t{dir}")


with open(os.environ["APPDATA"] + "/fc/fc.conf", 'r') as conf:
    # https://stackoverflow.com/a/3277515
    config = [line.rstrip() for line in conf]
    # config = { } TODO: dictionary for config shit

with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'r') as dirstxt:
    dirs = [line.rstrip() for line in dirstxt]

if (len(sys.argv) == 1):
    # TODO: copy()
    exit()

elif (sys.argv[1] == "add"):
    try:
        dirs.append(sys.argv[2])
    except IndexError:
        print("add requires a directory")
    # finally:
        # exit()

elif (sys.argv[1] == "ls"):
    listDirs(dirs)
    exit()

elif (sys.argv[1] == "clr") or (sys.argv[1] == "clear"):
    with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'w') as dirstxt:
        dirstxt.write("")

else:
    print(f"Unknown argument: '{sys.argv[1]}'")

listDirs(dirs)

with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'a') as dirstxt:
    for dir in dirs:
        dirstxt.write(dir + '\n')
