#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/15 13:48
# @Author: Jtyoui@qq.com
from pyunit_gof import IState1, IStated


class SolidWater(IState1):
    def behavior(self, *args, **kwargs):
        return '我是固态'


class LiquidWater(IState1):
    def behavior(self, *args, **kwargs):
        return '我是液态'


class GaseousWater(IState1):
    def behavior(self, *args, **kwargs):
        return '我是气态'


class Water(IStated):
    """根据温度不同，实现不同的水的形态"""

    def __init__(self, state: IState1, temperature):
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

    def set_state(self, state: IState1):
        self.state = state  # 改变状态
        return self.behavior()


if __name__ == '__main__':
    water = Water(SolidWater(), -10)
    water.flag_state(80)
    water.flag_state(120)
