#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/14 13:03
# @Author: Jtyoui@qq.com
from abc import ABCMeta, abstractmethod


class IState(metaclass=ABCMeta):

    @abstractmethod
    def behavior(self, *args, **kwargs):
        """具体的行为状态"""
        pass


class IStated(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, state: IState):
        self.state = state

    @abstractmethod
    def set_state(self, state: IState):
        """改变不同的状态类,去实现不同的功能

        self.state = state
        state.behavior(self)
        """
        pass

    @abstractmethod
    def flag_state(self, *args, **kwargs):
        """根据不同的情况实现不同的状态类

        if flag==1:
            self.set_state(IState)
        elif flag==2:
            self.set_state(IState)
        """
        pass

    @abstractmethod
    def behavior(self, *args, **kwargs):
        """具体的行为状态"""
        pass
