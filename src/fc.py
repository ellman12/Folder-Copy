import sys
import os


def copyDirs(dirs, location):
    print("copy ")


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
    dirstxt.close()

if (len(sys.argv) == 1):
    copyDirs()
    exit()

elif (sys.argv[1] == "cp"):
    copyDirs()
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
