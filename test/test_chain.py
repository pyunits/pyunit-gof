#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time  : 2020/3/19 15:06
# @Author: Jtyoui@qq.com
from pyunit_gof import Chain, IChain


class Request(Chain):
    """请假的请求"""

    def __init__(self, name, day_off):
        self.name = name
        self.day_off = day_off


class Person:
    """请假人"""

    def __init__(self, leader: IChain):
        self.leader = leader

    def send_leander(self, request: Request):
        self.leader.handle_request(request)


class Supervisor(IChain):
    def __init__(self, next_handler):
        super().__init__()
        self.next_handler = next_handler

    def _handle_request(self, chain: Request):
        if chain.day_off <= 2:
            print('主管已经签字')


class DepartmentManager(IChain):
    def __init__(self, next_handler):
        super().__init__()
        self.next_handler = next_handler

    def _handle_request(self, chain: Request):
        if 2 < chain.day_off <= 10:
            print('部门总监签字')


class CEO(IChain):
    def __init__(self):
        super().__init__()

    def _handle_request(self, chain: Request):
        if chain.day_off > 10:
            print('CEO签字')


if __name__ == '__main__':
    req = Request('张三', 21)
    person = Person(Supervisor(DepartmentManager(CEO())))
    person.send_leander(req)
