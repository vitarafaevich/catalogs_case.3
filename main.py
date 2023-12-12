import os
import ru_local as ru

WAY_UP = "../"


def main():
    currentDir = os.getcwd()
    print(ru.CURRENT, currentDir)
    while True:
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            print(ru.END)
            break
    return currentDir


def acceptCommand():
    print(ru.LOOK)
    print(ru.UP)
    print(ru.DOWN)
    print(ru.COUNT_FILE)
    print(ru.SIZE_F)
    print(ru.FIND_F)
    print(ru.EXIT)
    command = int(input(ru.INPUT_NUM))
    while command < 1 or command > 7:
        command = int(input(ru.WRONG_C))
    return command


def runCommand(command):
    currentDir = os.getcwd()
    if command == 1:
        directory(currentDir)
    elif command == 2:
        moveUp()
    elif command == 3:
        moveDown(currentDir)
    elif command == 4:
        print(countFiles(currentDir))
    elif command == 5:
        print(countBytes(currentDir))
    elif command == 6:
        target = input()
        name = findFiles(target, currentDir)
        if name == []:
            print(ru.FILE_WITH, currentDir, ru.F_NOT_FND)
        else:
            print(name)


def directory(directory):
    files_under = os.listdir(directory)
    print(ru.IN_CTLG)
    for i in files_under:
        print(i)


def moveUp():
    os.chdir(WAY_UP)
    currentDir = os.getcwd()
    print(ru.CURRENT, currentDir)


def moveDown(currentDir):
    tryDir = input(ru.INPUT_CTLG)
    tryingDir = os.path.join(currentDir, tryDir)
    if os.path.exists(tryingDir):
        os.chdir(tryingDir)
        currentDir = os.getcwd()
        print(ru.CURRENT, currentDir)
    else:
        print(ru.NOT_FOUND)


def countFiles(path):
    cnt = 0
    if os.path.isfile(path):
        return 1
    else:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            cnt += countFiles(item_path)
    return cnt


def countBytes(path):
    file_size = 0
    if os.path.isfile(path):
        return os.path.getsize(path)
    else:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            file_size += countBytes(item_path)
    return file_size


def findFiles(target, path):
    targets = []
    if os.path.isfile(path):
        if target in os.path.basename(path):
            return [path]
    elif os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            targets.extend(findFiles(target, item_path))
    return targets


main()
