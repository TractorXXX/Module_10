# Задача "Многопроцессное считывание"
# Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
# предварительно закомментировав другой.

import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line != '':
                all_data.append(line)
            else:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов

time_st = time.time()

for i in filenames:
    read_info(i)

time_fin = time.time()
time_w = round(time_fin - time_st, 6)
print(f'Время выполнения линейного вызова: {time_w} сек.')

# Многопроцессный вызов

if __name__ == '__main__':

    time_st = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    time_fin = time.time()
    time_w = round(time_fin - time_st, 6)
    print(f'Время выполнения многопроцессного вызова: {time_w} сек.')
