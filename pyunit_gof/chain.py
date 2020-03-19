#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/19 14:52
# @Author: Jtyoui@qq.com
"""责任链模式
责任链模式（Chain of Responsibility Pattern）为请求创建了一个接收者对象的链。
这种模式给予请求的类型，对请求的发送者和接收者进行解耦。这种类型的设计模式属于行为型模式。
在这种模式中，通常每个接收者都包含对另一个接收者的引用。如果一个对象不能处理该请求，那么它会把相同的请求传给下一个接收者，依此类推。
"""
from abc import ABCMeta, abstractmethod


class Chain:
    """具体的实现类"""
    pass


class IChain(metaclass=ABCMeta):
    """责任链抽象类"""

    @abstractmethod
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    def get_next_handler(self):
        return self.next_handler

    def handle_request(self, chain: Chain):
        self._handle_request(chain)
        if self.next_handler is not None:
            self.next_handler.handle_request(chain)

    @abstractmethod
    def _handle_request(self, chain: Chain):
        """真正处理请求的方法"""
        pass
