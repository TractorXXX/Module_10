from threading import Thread
from queue import Queue
from random import randint
import time

threads = []

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        wait = randint(3, 10)
        time.sleep(wait)


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)


    def guest_arrival(self, *guests):
        guests_list = list(guests)

        for n in range(len(self.tables)):
            self.tables[n].guest = guests_list[n].name
            thread_n = guests_list[n]
            thread_n.start()
            threads.append(thread_n)
            print(f'{guests_list[n].name} сел(-а) за стол номер {self.tables[n].number}')
        if len(guests_list) > len(self.tables):
            for m in range(len(self.tables), len(guests_list)):
                self.queue.put(guests_list[m])
                print(f'{guests_list[m].name} в очереди')


    def discuss_guests(self):

        while not (self.queue.empty()) and Cafe.table_free(self):
            k = 0
            for table in self.tables:
                if not threads[k].is_alive() and Cafe.table_free(self):
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    guest_queue = self.queue.get()
                    table.guest = guest_queue.name
                    print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thread_k = guest_queue
                    thread_k.start()
                    threads[k] = thread_k

    def table_free(self):
        for table in self.tables:
            if table.guest is None:
                flag = False
            else:
                flag = True
            if flag:
                return True


# Создание столов
tables = [Table(number) for number in range(1, 7)]
# tables = [Table(1), Table(2), Table(3), Table(4), Table(5), Table(6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# guests = [Guest('M'), Guest('O')]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

for thread in threads:
    thread.join()

print()
print('Все гости размещены за столами')
