#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/11 10:20
# @Author: Jtyoui@qq.com
from pyunit_gof import IObserver, IObservable, Singleton, IStated, IState


def test_observer():
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


def test_state():
    class SolidWater(IState):
        def behavior(self, *args, **kwargs):
            return '我是固态'

    class LiquidWater(IState):
        def behavior(self, *args, **kwargs):
            return '我是液态'

    class GaseousWater(IState):
        def behavior(self, *args, **kwargs):
            return '我是气态'

    class Water(IStated):
        """根据温度不同，实现不同的水的形态"""

        def __init__(self, state: IState, temperature):
            super().__init__(state)
            self.temperature = temperature

        def flag_state(self, temperature):
            print('改变前是：', self.temperature, self.state.behavior())
            if temperature <= 0:
                value = self.set_state(SolidWater())
            elif 0 < temperature <= 100:
                value = self.set_state(LiquidWater())
            else:
                value = self.set_state(GaseousWater())
            print('改变后是', temperature, value)
            self.temperature = temperature

        def behavior(self):
            return self.state.behavior(self)  # 调用具体的状态方法

        def set_state(self, state: IState):
            self.state = state  # 改变状态
            return self.behavior()

    water = Water(SolidWater(), -10)
    water.flag_state(80)
    water.flag_state(120)


if __name__ == '__main__':
    # test_observer()
    # test_single()
    test_state()
