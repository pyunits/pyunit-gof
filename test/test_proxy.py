#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/19 15:52
# @Author: Jtyoui@qq.com
from pyunit_gof import IProxy


class RealSubject(IProxy):

    def method(self, *args, **kwargs):
        print("real something")


class ProxySubject(IProxy):
    def __init__(self):
        self.subject = RealSubject()

    def method(self, *args, **kwargs):
        self.subject.method(*args, **kwargs)


if __name__ == '__main__':
    subject = ProxySubject()
    subject.method()
