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
    try:
        copyDirs(dirs, pathlib.PurePath(sys.argv[2]))
    except IndexError:
        copyDirs(dirs, cpLoc)
    exit()

elif (sys.argv[1] == "add"):
    try:
        for dir in dirs:  # Check for duplicates
            if str(sys.argv[2]) == str(dir):
                print(f"{colors.FAIL}dir '{str(sys.argv[2])}' is already in the file!{colors.ENDC}")
                listDirs(dirs)
                exit()

        dirs.append(sys.argv[2])
        with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'w') as dirstxt:
            for dir in dirs:
                dirstxt.write(str(dir) + '\n')
    except IndexError:
        print("'add' requires a directory")
        exit()

elif (sys.argv[1] == "ls"):
    listDirs(dirs)
    exit()

elif (sys.argv[1] == "rm"):
    with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'r') as f:
        lines = f.readlines()
    with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'w') as f:
        for line in lines:
            if line.strip("\n") != sys.argv[2]:
                f.write(line)
    listDirs(dirs)
    exit()

elif (sys.argv[1] == "clr"):
    with open(os.environ["APPDATA"] + "/fc/dirs.txt", 'w') as dirstxt:
        dirstxt.write("")

elif (sys.argv[1] == "help"):
    help()
    exit()

else:
    print(f"{colors.FAIL}Unknown command: '{sys.argv[1]}'")
    help()
    exit()
