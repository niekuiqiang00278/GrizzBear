#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 10:31
# @Author  : cap669
# @File    : Utils.py
# @Software: PyCharm
from pathlib import Path

tac = ['java', 'go', 'py']


class Natc:
    def __init__(self, path: Path, tag):
        self.path = path.joinpath(tag)
        self.path.mkdir()
        self.base(self.__na0('base'))
        self.bis(self.__na0('bis'))
        self.config(self.__na0('config'))
        self.err(self.__na0('err'))
        self.plux(self.__na0('plux'))
        self.utils(self.__na0('utils'))

    def __na0(self, tag):
        p0 = self.path.joinpath(tag)
        p0.mkdir()
        return p0

    def base(self, path):
        wrapper, cur = self._base0(path)

    def _base0(self, path) -> (Path, Path):
        wrapper = path.joinpath('wrapper')
        cur = path.joinpath('cur')
        wrapper.mkdir()
        cur.mkdir()
        return wrapper, cur

    def bis(self, path):
        pass

    def config(self, path):
        pass

    def err(self, path):
        pass

    def plux(self, path):
        pass

    def utils(self, path):
        pass


class Utils:
    def __init__(self, path, ta):
        if ta in tac:
            pass
        else:
            raise Exception
        path = Path(path)
        self.data = self.Data(path)
        self.root = self.Root(path)
        self.server = self.Server(path)

    class Data(Natc):
        def __init__(self, path):
            Natc.__init__(self, path, 'data')

    class Root(Natc):
        def __init__(self, path):
            Natc.__init__(self, path, 'root')

    class Server(Natc):
        def __init__(self, path):
            Natc.__init__(self, path, 'server')


if __name__ == '__main__':
    Utils(r'C:\Kac\Java\Poic\src', 'java')
