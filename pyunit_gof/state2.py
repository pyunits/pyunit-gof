#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/15 13:23
# @Author: Jtyoui@qq.com
from abc import ABCMeta, abstractmethod


class IState2(metaclass=ABCMeta):

    @abstractmethod
    def is_match(self, *args, **kwargs) -> bool:
        """状态属性是否满足"""
        pass

    @abstractmethod
    def behavior(self, context, *args, **kwargs):
        """具体的行为方法"""
        pass


class ContextSate(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        self.states = []  # 所有的状态集合
        self.cur_state = None  # 当前状态

    @abstractmethod
    def is_match(self, *args, **kwargs):
        """判断条件是否要执行具体的类

        for state in self.states:
            if state.is_match(state_info):
                self.cur_state=state
        """
        pass

    @abstractmethod
    def behavior(self):
        """执行当前状态,当前状态是满足条件的状态

        self.cur_state.behavior(self)
        """
        pass
