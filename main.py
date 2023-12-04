import os


def main():
    currentDir = os.getcwd()
    print('Текущий каталог:', currentDir)
    while True:
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            print("the end")
            break
    return currentDir


def acceptCommand():
    print("1 - Просмотр каталога")
    print("2 - На уровень вверх")
    print("3 - На уровень вниз")
    print("4 - Количество файлов в каталогах")
    print("5 - Размер текущего каталога (в байтах)")
    print("6 - Поиск файла")
    print("7 - Выход из программы")
    command = int(input("Введите номер команды: "))
    while command < 1 or command > 7:
        command = int(input("Not correct :( Try again :) "))
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
        print(findFiles(target, currentDir))


def directory(directory):
    files_under = os.listdir(directory)
    for i in files_under:
        print(i)
    print('in catalogue:', directory)


def moveUp():
    os.chdir("../")
    currentDir = os.getcwd()
    print('current catalogue:', currentDir)


def moveDown(currentDir):
    tryDir = input('please, write catalogue name: ')
    tryingDir = os.path.join(currentDir, tryDir)
    if os.path.exists(tryingDir):
        os.chdir(tryingDir)
        currentDir = os.getcwd()
        print('current catalogue:', currentDir)
    else:
        print('name is not found, try again')


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
    if not targets:
        print(f"Файлы с '{target}' в имени в каталоге {path} не найдены.")
    return targets


main()
