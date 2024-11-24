import threading
import time
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.deposit_count = 100
        self.take_count = 100

    def deposit(self):
        self.lock.acquire()
        for i in range(self.deposit_count):
            deposit_random = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                self.balance += deposit_random
                print(f'Пополнение: {deposit_random}. Баланс: {self.balance}')
                self.deposit_count -= 1
            time.sleep(0.001)

    def take(self):

        for i in range(self.take_count):
            take_random = randint(50, 500)
            print(f'Запрос на {take_random}')
            if take_random <= self.balance:
                self.balance -= take_random
                print(f'Снятие: {take_random}. Баланс: {self.balance}')
                self.deposit_count -= 1
            else:
                print('Запрос отклонён, недостаточно средств')
                if not self.lock.locked():
                    self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')