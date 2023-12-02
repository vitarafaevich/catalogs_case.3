import os


'программа начинается в текущем каталоге'
def main():
    currentDir = os.getcwd
    print('Текущий каталог:', currentDir)
    while True:
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            print("the end")
            break


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
    if command == 1:
        directory(currentDir)
    elif command == 2:
        moveUp(currentDir)
    elif command == 3:
        moveDown(currentDir)
    elif command == 4:




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
        currentDir = tryingDir
        print('current catalogue:', currentDir)
    else:
        print('name is not found, try again')


'''
делать walk, но судя по всему через 3 кортежа - путь к файлу, папака внутри и сам файл
'''
def countFiles(path):
    cntr = 0
    for /// in os.walk(path):
        cntr += len()
    return cntr


'''
аналогично предыдущему
'''
def countBytes(path):




'''
кто такой target
'''
def findFiles(target, path):


main()
