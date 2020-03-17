#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/17 15:29
# @Author: Jtyoui@qq.com
from pyunit_gof import IMediator, Mediator


class NongFuWater(IMediator):
    def __init__(self):
        self.data = '农夫山泉，有点甜'


class MineralWater(IMediator):
    def __init__(self):
        self.data = '矿泉水，健康'


class TapWater(IMediator):
    def __init__(self):
        self.data = '自来水，便宜'


class Water(Mediator):
    def __init__(self):
        super().__init__()

    def notify(self, data):
        for mediator in self.mediators:
            if data in mediator.data:
                return mediator


if __name__ == '__main__':
    water = Water()
    water.add(NongFuWater())
    water.add(MineralWater())
    water.add(TapWater())
    w = water.notify('便宜')
    print(w.data)
