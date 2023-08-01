# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 18:31
# @Author  : Ricky
# @IDE: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2023/8/1 16:04
# @Author  : Ricky
# @IDE: PyCharm
import pytest
def test01():
    print('你好呀~~~')

def test02():
    print('我爱你')

if __name__ == '__main__':
    pytest.main(['-vs'])
