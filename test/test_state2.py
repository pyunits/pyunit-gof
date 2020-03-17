#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/15 13:48
# @Author: Jtyoui@qq.com
from pyunit_gof import IState2, ContextSate


class SolidWater(IState2):

    def is_match(self, info, *args, **kwargs) -> bool:
        return info <= 0

    def behavior(self, context, *args, **kwargs):
        return '我是固态'


class LiquidWater(IState2):
    def is_match(self, info, **kwargs) -> bool:
        return 0 < info < 100

    def behavior(self, context, *args, **kwargs):
        return '我是液态'


class GaseousWater(IState2):
    def is_match(self, info, *args, **kwargs) -> bool:
        return 2000 > info >= 100

    def behavior(self, context, *args, **kwargs):
        return '我是气态'


class SuperGaseousWater(IState2):
    def is_match(self, info, *args, **kwargs) -> bool:
        return info >= 2000

    def behavior(self, context, *args, **kwargs):
        return '我是超气态'


class Water(ContextSate):

    def __init__(self):
        super().__init__()

    def is_match(self, info, **kwargs):
        for state in self.states:
            if state.is_match(info):
                self.cur_state = state
                break

    def behavior(self):
        return self.cur_state.behavior(self)


if __name__ == '__main__':
    water = Water()
    water.states.append(SolidWater())
    water.states.append(LiquidWater())
    water.states.append(GaseousWater())
    water.states.append(SuperGaseousWater())
    water.is_match(-10)
    print(water.behavior())
    water.is_match(10)
    print(water.behavior())
    water.is_match(110)
    print(water.behavior())
    water.is_match(11110)
    print(water.behavior())
