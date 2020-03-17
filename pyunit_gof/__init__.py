#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/11 9:57
# @Author: Jtyoui@qq.com
from .observer import IObservable, IObserver
from .singleton import Singleton
from .state1 import IState1, IStated
from .state2 import IState2, ContextSate
from .mediator import IMediator, Mediator

__version__ = '2020.3.11'
__author__ = 'Jtyoui'
__description__ = '设计模式接口'
__email__ = 'jtyoui@qq.com'
__names__ = 'pyUnit_gof'
__url__ = 'https://github.com/PyUnit/pyunit-gof'
