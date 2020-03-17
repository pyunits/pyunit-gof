#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/17 15:08
# @Author: Jtyoui@qq.com
"""中介模式
用一个中介对象来封装一系列的对象交互。
中介者使各个对象不需要显式地相互引用，
从而使其耦合松散，而且可以独立地改变它们之间的交互。
"""
from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):
    """每一个中介的组件类"""
    pass


class Mediator(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        self.mediators = []

    def add(self, mediator: IMediator):
        """增加组件"""
        self.mediators.append(mediator)

    def remove(self, mediator: IMediator):
        """去除组件"""
        self.mediators.remove(mediator)

    @abstractmethod
    def notify(self, *args, **kwargs):
        """判断组件的信息

         for _mediator in self.mediators:
             if _mediator != mediator:
                 return _mediator

        :return: 返回组件
        """
        pass
