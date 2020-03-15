#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/15 13:47
# @Author: Jtyoui@qq.com
from pyunit_gof import IObserver, IObservable


class WaterHeater(IObservable):

    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.message = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for o in self.observers:
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


if __name__ == '__main__':
    water = WaterHeater()
    water.subscribe(WashingMode())
    water.subscribe(DrinkingMode())
    water.set_temperature(40)
    water.set_temperature(60)
    water.set_temperature(100)
    print(water.message)
