from pathlib import Path
import re

#->->->->->->->->->->***FIRST TASK***<-<-<-<-<-<-<-<-<-<

print ('\n\tFIRST TASK\n')

# The function analyzes a file with developer salary amounts and returns the total and average salary amount of all developers
def total_salary(path:str) -> tuple[int, float]:
    '''
    The function analyzes a file "salary_for_developers.txt" with developer salary amounts 
    and returns the total and average salary amount of all developers.
        - The function must take one argument - the path to a text file (path).
        - The file contains data on developers' salaries, separated by commas. Each line indicates one developer.
        - The function must analyze the file, calculate the total and average salary.
        - The result of the function is a tuple of two numbers: the total salary and the average salary.
        - The function should accurately calculate the total and average.
        - There should be handling for cases when the file is missing or corrupted.
        - The code should be clean, well-structured and understandable
    
    Input:
    :param date: string

    Output:
    :return: tuple[int, float]

    '''
    path_to_file = Path(path)
    number_of_developers = 0
    total_salary = 0
    average_salary = 0
    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:

            for line in file:
                total_salary += int(line.split(',')[1])
                number_of_developers += 1
        average_salary = int(total_salary/number_of_developers)
    except FileNotFoundError:
        print ('Sorry File Not Found')
    except UnicodeError:
        print ('Decode error')
    return (total_salary, average_salary)
    

total, average = total_salary('./salary_for_developers.txt')
print(f"Загальна сума заробітної плати: {total}, \nСередня заробітна плата: {average}")
