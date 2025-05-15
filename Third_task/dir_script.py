import sys
from pathlib import Path
from re import match
import colorama 

#->->->->->->->->->->***THIRD TASK***<-<-<-<-<-<-<-<-<-<

print ('\n\tTHIRD TASK\n')

# функція для виводу детальної довідки по запиту '-h', '--help', '/?'
def show_detailed_help():
    print("""
Зразок використання:
    python dir_script.py <path_to_dir>

🔹 Аргументи:
    <path_to_dir>       Шлях до текстового файлу, який потрібно прочитати.
    -h, --help, /?  Показати це повідомлення.

Приклад:
    python script.py .\dir\
    python script.py 'D:\path to lib\dir'
""")
    
# функція для виводу короткої довідки при невідповідності параметрів
def show_short_help():
    print("""
Для отримання довідки введіть: 
    python script.py -h
    python script.py --help
    python script.py /?
""")

# функція для перевірки чи в аргумент передано шлях до теки
def path_validation(path_str: str) -> bool:
    path = Path(path_str)
    return path.is_dir()

# функція перевірки правильності передачі аргументів
def validation_arg(list_of_arg: list) -> Path:
    if len(list_of_arg) == 2 and path_validation(list_of_arg[1]): #якщо кількість аргументів 1 одразу перевіряємо чи це шлях до папки і чи вона існує
        path_to_dir = Path(list_of_arg[1])
        print('Тека ', colorama.Fore.RED, path_to_dir, '\b\\', colorama.Fore.WHITE, 'обробляється')
        return path_to_dir
    elif len(list_of_arg) == 2 and list_of_arg[1] in ('-h', '--help', '/?'): #перевіряємо чи аргумент не є запитом на довідку
        show_detailed_help()
    elif len(list_of_arg) == 2 and not(path_validation(list_of_arg[1])): #якщо аргументом не є шлях або така тека не існує
        print (colorama.Fore.RED, 'Даний шлях не існує або аргумент не є шляхом', colorama.Fore.WHITE )
        show_short_help()
    else:
        show_short_help()

path_to_dir = validation_arg(sys.argv) #виконання перевірки аргументів

#функція для виводу несортованої структури, а також формування списків шляхів до папокі файлів
def iter_object_in_dir(path: Path) -> list[Path]:
    string_with_space = "|" + len(path_to_dir.parts) * "--"
    print (colorama.Fore.BLUE, string_with_space, path.name, '\b\\')
    for i in path.iterdir():
        if i.is_file(): #перевіряємо чи об'єкт файл
            string_with_space ="|" + len(i.parts) * "--"
            print(colorama.Fore.GREEN, string_with_space, i.name)
        elif i.is_dir():  #перевіряємо чи об'єкт папка
            iter_object_in_dir(i) #рекурсивно викикаємо функцію 


# list_of_dir = [] #буде містити перелік папок
# list_of_file = [] #буде містити перелік файлів
#функція для виводу несортованої структури, а також формування списків шляхів до папокі файлів
def list_of_dir_and_files(path: Path) -> list[Path]:
    try:
        list_of_dir.append(path) #формуємо список усіх шляхів до папок
    except NameError:
        list_of_dir = [path]
    for i in path.iterdir():
        if i.is_file(): #перевіряємо чи об'єкт файл
            try:
                list_of_file.append(i) #формуємо список усіх шляхів до папок
            except NameError:
                list_of_file = [i]
        elif i.is_dir():  #перевіряємо чи об'єкт папка
            list_of_dir_and_files(i) #рекурсивно викикаємо функцію
    return list_of_dir, list_of_file 


def print_sorted_structure(dir:list[Path], file:list[Path]):
    string_with_space = ''
    for i in dir:
        print (colorama.Fore.BLUE, string_with_space, i.name,'\b\\')
        string_with_space += "    "
        for k in file:
            if k.parent == i:
                print(colorama.Fore.GREEN, string_with_space, k.name)

print (colorama.Fore.RED, '\n\nНе сортована структура теки\n', colorama.Fore.RESET)
iter_object_in_dir(path_to_dir)
print (colorama.Fore.RED, '\n\nCортована структура теки\n', colorama.Fore.RESET)
print(list_of_dir_and_files(path_to_dir)[0], list_of_dir_and_files(path_to_dir)[1])
print_sorted_structure(list_of_dir_and_files(path_to_dir)[0], list_of_dir_and_files(path_to_dir)[1])
print(colorama.Fore.RESET)