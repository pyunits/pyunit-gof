#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/15 13:48
# @Author: Jtyoui@qq.com
from pyunit_gof import Singleton
import threading
import time


@Singleton
class Person:

    def __init__(self, name):
        self.name = name

    def __call__(self):
        time.sleep(0.1)
        if self.name != 0:
            print(self.name)


@Singleton
class PersonOther:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        time.sleep(0.1)
        if self.name != 1:
            print(self.name)


threads = []
for i in range(1_0000):
    t = threading.Thread(target=Person(i))
    t.start()
    threads.append(t)

for i in range(1_0000):
    t = threading.Thread(target=PersonOther(i + 1))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

if __name__ == '__main__':
    print(Person)
    print(PersonOther)
