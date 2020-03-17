#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/17 16:40
# @Author: Jtyoui@qq.com
from copy import copy, deepcopy


class Clone:
    def clone(self):
        """浅拷贝"""
        return copy(self)

    def deep_clone(self):
        """深拷贝"""
        return deepcopy(self)
