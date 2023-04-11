#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/11 10:28
# @Author  : cap669
# @File    : XConfig.py
# @Software: PyCharm
from pydantic import BaseModel, BaseSettings
from functools import lru_cache
from typing import Any
from enum import Enum
class Env(str, Enum):
    DEV = 'dev'
    PRO = 'pro'
class XConfig:

    @classmethod
    @lru_cache()
    def get_config(cls, env: Env) -> Any:
        pass