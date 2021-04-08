from header import *

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
            if sys.argv[2] == str(dir):
                print(f"dir '{sys.argv[2]}' is already in the file!")
                listDirs(dirs)
                exit()

        dirs.append(sys.argv[2])
        with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'a') as dirstxt:
            for dir in dirs:
                dirstxt.write(str(dir) + '\n')
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
