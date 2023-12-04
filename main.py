import os


'программа начинается в текущем каталоге'
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

'''
(1. просмотр каталога. 2. на уровень вверх. 3. на уровень вниз. 
4. количество файлов в каталогах. 5. размер текущего каталога (в байтах). 
6. поиск файла. 7. выход из программы.
'''

'''
определяет по номеру command, какую функцию следует выполнить. 
'''
def runCommand(command):
    currentDir = os.getcwd()
    if command == 1:
        directory(currentDir)
    elif command == 2:
        moveUp(currentDir)
    elif command == 3:
        moveDown(currentDir)
    elif command == 4:
        countFiles(currentDir)
    elif command == 5:
        countBytes(currentDir)
    elif command == 6:
        findFiles(target, currentDir)




'''
доп функция, показывает весь каталог
'''
def directory(directory):
    files_under = os.listdir(directory)
    for i in files_under:
        print(i)
    print('in catalogue:', directory)


'''
показывает каталоги ниже текущего в дереве
'''
def moveUp():
    os.chdir("..")
    currentDir = os.getcwd()
    print('current catalogue:', currentDir)


'''
запрашивает имя подкаталога, при корректности делать каталог находящийся в currentDir текущим.
проверка идет только внииииз!!! значит должны присоединять к текущему пути
'''
def moveDown(currentDir):
    tryDir = input('please, write catalogue name: ')
    tryingDir = os.path.join(currentDir, tryDir)
    if os.path.exists(tryingDir):
        currentDir = os.getcwd()
        print('current catalogue:', currentDir)
    else:
        print('name is not found, try again')


'''
делать walk, но судя по всему через 3 кортежа - путь к файлу, папака внутри и сам файл
'''
def countFiles(path):
    cntr = 0
    for address, dirs, files in os.walk(path):
        cntr += len(files)
    return cntr


'''
аналогично предыдущему
'''
'''address на каждой итерации связывается с первым элементом очередного кортежа (строкой, содержащей адрес каталога) 
dirs – со вторым элементом (списком подкаталогов), 
files - со списком файлов этого каталога. Во вложенном цикле извлекается имя каждого файла из списка файлов.'''
def countBytes(path):
    file_size = 0
    for address, dirs, files in os.walk(path):
        for name in files:
            path = os.path.join(address, name)
            file_size += os.path.getsize(path)
    return file_size


def findFiles(target, path):
    targets = []
    for address, dirs, files in os.walk(path):
        for name in files:
            if target in name:
                targets.append(os.path.join(address, name))
    if not targets:
        print(f"Файлы с '{target}' в имени в каталоге {path} не найдены.")
    else:
        print(f"Найденные файлы с '{target}' в имени:")
        for file_path in targets:
            print(file_path)
    return targets

main()
