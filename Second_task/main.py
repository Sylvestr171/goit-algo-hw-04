from pathlib import Path

#->->->->->->->->->->***SECOND TASK***<-<-<-<-<-<-<-<-<-<

print ('\n\tSECOND TASK\n')

path_to_file = Path('.\cats.txt')

# function for generating dictionaries from file data
def get_cats_info(path:Path) -> list[dict]:
    '''
    The function for generating dictionaries from file data:
        - function takes one argument - the path to a text file (path)
        - The function should return a list of dictionaries, 
        where each dictionary contains information about one cat,
        with key "id", "name", "age"
        - Use with to read the file securely.
        - Remember to set the encoding when opening files
        - For each line in the file, use split(',') to get the cat's ID, name, and age.
        - add dictionary to the list that will be returned.
        - work out possible exceptions related to reading the file.
    Input:
    :param date: Path

    Output:
    :return: dict
    '''
    list_of_cats_dictionary = [] #ініціалізація списку для збереження словників 
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file: #построково читаємо файл
                    '''
                    порядково читаємо файл і 
                    за допомогою zip формуємо словник з ключів і значень 
                    розбитих через  .split(',') 
                    '''
                    list_of_cats_dictionary.append(dict(zip(["id", "name", "age"], line.split(","))))
    except FileNotFoundError: 
        print ('Sorry File Not Found')
    except UnicodeError:
        print ('Decode error')
    return list_of_cats_dictionary

print (get_cats_info(path_to_file))
