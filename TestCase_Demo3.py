#!/usr/bin/python
# -*- coding: UTF-8 -*-

#包含集合，多集合

import unittest
from TestCaseDemo import TestCaseDemo

#添加不同的集合

def Suite1():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo('test_Case1'))
    suiteTest.addTest(TestCaseDemo('test_Case2'))
    print('Suite1 running')
    return suiteTest

def Suite2():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(TestCaseDemo('test_Case3'))
    suiteTest.addTest(TestCaseDemo('test_Case4'))
    print('Suite2 running')
    return suiteTest

#包含所有的Suite
def AllSuite():
    allTest = unittest.TestSuite((Suite1(), Suite2()))
    return allTest

#运行的时候，可以根据不同的要求，运行不同的Suite,或者全部运行，这样就方便管理每次运行的case
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(AllSuite())
