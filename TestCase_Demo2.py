#!/usr/bin/python
# -*- coding: UTF-8 -*-

#集合可以写在main

import unittest
from TestCaseDemo import TestCaseDemo

#指定并启动测试集合

if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTests([TestCaseDemo('test_Case1'), TestCaseDemo('test_Case2')]) // case列表
    #suiteTest.addTest(TestCaseDemo('test_Case1'))
    #suiteTest.addTest(TestCaseDemo('test_Case2'))

    #直接启动集合
    runner = unittest.TextTestRunner()
    runner.run(suiteTest)