#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/11 9:59
# @Author: Jtyoui@qq.com
"""观察者模式"""
from abc import ABCMeta, abstractmethod


class IObservable(metaclass=ABCMeta):
    __doc__ = """可观察者对象"""
    __slots__ = []

    @abstractmethod
    def subscribe(self, observer):
        """订阅观察者

        :param observer: 观察者对象。是一个class对象
        """
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        """退订观察者

        :param observer: 观察者对象。是一个class对象
        """
        pass

    @abstractmethod
    def notify(self, *args, **kwargs):
        """通知观察者对象"""
        pass


class IObserver(metaclass=ABCMeta):
    __doc__ = """观察者的抽象类,具体实现"""

    @abstractmethod
    def notify(self, observable, *args, **kwargs):
        """通知观察者对象

        :param observable: 观察者具体的实现方法
        """
        pass
