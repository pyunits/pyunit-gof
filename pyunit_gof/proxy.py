#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/19 15:50
# @Author: Jtyoui@qq.com
"""代理模式
代理模式的定义：为其他对象提供一种代理以控制对这个对象的访问。在某些情况下，
一个对象不适合或者不能直接引用另一个对象，而代理对象可以在客户端和目标对象之间起到中介的作用。
"""
from abc import ABCMeta, abstractmethod


class IProxy(metaclass=ABCMeta):

    @abstractmethod
    def method(self, *args, **kwargs):
        """代理类"""
        pass
