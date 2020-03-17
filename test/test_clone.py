#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/17 16:43
# @Author: Jtyoui@qq.com
from pyunit_gof import Clone


class Person(Clone):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    person = Person('张三')
    p = person.clone()
    p.name = '李四'
    print(person.name)
    print(p.name)
