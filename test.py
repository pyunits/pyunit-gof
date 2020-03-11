#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/11 10:20
# @Author: Jtyoui@qq.com
from pyunit_gof import IObserver, IObservable, Singleton


def test_observer():
    class WaterHeater(IObservable):

        def __init__(self):
            self.__observers = []
            self.temperature = 0
            self.message = []

        def subscribe(self, observer):
            self.__observers.append(observer)

        def unsubscribe(self, observer):
            self.__observers.remove(observer)

        def notify(self, *args, **kwargs):
            for o in self.__observers:
                o.notify(self, *args, **kwargs)

        def set_temperature(self, temperature):
            self.temperature = temperature
            self.notify()

    class WashingMode(IObserver):

        def notify(self, observable, *args, **kwargs):
            if 70 > observable.temperature >= 50:
                observable.message.append(f'可以洗澡了，水温{observable.temperature}')

    class DrinkingMode(IObserver):
        def notify(self, observable, *args, **kwargs):
            if observable.temperature >= 100:
                observable.message.append(f'水开了，水温{observable.temperature}')

    water = WaterHeater()
    water.subscribe(WashingMode())
    water.subscribe(DrinkingMode())
    water.set_temperature(40)
    water.set_temperature(60)
    water.set_temperature(100)
    print(water.message)


def test_single():
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

    print(Person)
    print(PersonOther)


if __name__ == '__main__':
    # test_observer()
    test_single()
