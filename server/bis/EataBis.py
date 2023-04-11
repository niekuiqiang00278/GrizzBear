#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 12:07
# @Author  : cap669
# @File    : EataBis.py
# @Software: PyCharm
from server.bis.eata.MapiBis import MapiBis
from server.bis.eata.SiegeBis import SiegeBis
class EataBis:
    def __init__(self):
        self.mapi = MapiBis()
        self.siege = SiegeBis()
