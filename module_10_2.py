import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0

# Здесь цикл организован таким образом, чтобы закрыть все возможные варианты параметра power.
# Как для enemies кратного power, так и нет
        while True:
            enemies -= self.power
            days += 1
            if enemies > 0:
                time.sleep(1)
                print(f'{self.name} сражается {days}..., осталось {enemies} воинов.')
            else:
                print(f'{self.name} сражается {days}..., осталось {0} воинов.')
                break

        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


# Если enemies кратно power (как в задании)

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

print()

# Если enemies не кратно power (тоже возможный вариант)

first_knight = Knight('Sir Lancelot', 8)
second_knight = Knight('Sir Galahad', 17)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')