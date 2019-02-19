#!/usr/bin/python
# -*- coding: UTF-8 -*-

#集合写入一个方法，main调用并启动

import unittest
from unittestDemo.TestCaseDemo import TestCaseDemo

#添加一个测试集合，并添加case

def suite():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo('test_Case1'))
    return suiteTest

#指定并启动测试集合,运行集合方法
if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    runner.run(suite())