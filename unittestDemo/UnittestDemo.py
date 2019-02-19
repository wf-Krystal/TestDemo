#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from parameterized import parameterized
from HTMLTestRunner import HTMLTestRunner


class Testadd(unittest.TestCase):
    @classmethod  # 这里的装饰器@classmethod必须有，标识为一个类方法
    def setUpClass(cls):
        """setUpClass为类的初始化方法，在整个类运行前执行只执行一次"""
        pass

    def setUp(self):
        """为测试方法的初始化，每个case运行前执行一次"""
        self.a = 20
        self.b = 10

    def tearDown(self):
        """清理函数，和setUp类似，每个case执行后执行一次"""
        pass

    @classmethod
    def tearDownClass(cls):
        """和setUpclass类似，在调用整个类测试方法完成后执行一次"""
        pass

    def test_add(self):
        """验证加法"""
        result = self.a + self.b
        self.assertEqual(result, 30)

    def test_sub(self):
        """验证减法"""
        result = self.a - self.b
        self.assertEqual(result, 10)

    @unittest.skip('skipping test')
    def test_err(self):
        """错误验证"""
        result = self.a + self.b
        self.assertEqual(result, 3)

    @parameterized.expand([
        ('测试pass', 30,),
        ('测试error', 20,),
        ('测试error', 10,),
    ])
    def test_para(self, case, p):
        """参数化"""
        self._testMethodDoc = case  #这里将_testMethodDoc属性赋值可以解决测试报告中a.png的问题
        result = self.a + self.b
        self.assertEqual(result, p)

if __name__ == "__main__":
    # suite = unittest.TestSuite()
    # suite.addTest(Testadd('test_add'))
    # suite.addTest(Testadd('test_sub'))
    # suite.addTests([Testadd('test_add'), Testadd('test_sub'), Testadd('test_err')])
    suite = unittest.makeSuite(Testadd)
    # suite = unittest.TestLoader().loadTestsFromTestCase(Testadd)
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    with open('aa.html', 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,  # 测试报告需要写入到的文件
            verbosity=2,  # 控制台输出信息的详细程度
            title='test',  # 测试报告的标题
            # description='test'  # 测试报告的描述
        )
        runner.run(suite)

"""
需要写测试case的类都需要继承自unittest.testcase类
unittest.Testsuite()是测试套件对象
suite.addTest(testcase class(方法名))可以逐个添加想要运行的testcase至测试套件
suite.addTests()可以添加一个testcase的列表至测试套件
suite.addTest(testcase class)这里还可以添加testcase class,但是必须在testcase class中定义一个runTest方法

    def runTest(self):
        self.test_add()
        self.test_sub()
    suite.addTest(Testadd())

unittest.makesuite(testcase class)可以直接创建一个测试套件
unittest.TestLoader().loaderTestsFromTestCase(testcase classs)从指定的testcase class类构建一个测试套件
unittest.TextTestRunner()创建一个运行器
runer.run(suite)运行指定的测试套件
suite.countTestCases()返回测试套件中的case数
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test.py')这个方法可以去test_dir目录下查找以test开头的.py文件，并自动加载这些test.py中的testcase class生成一个测试套件
parameterized模块为unittest的一个扩展模块，可以很方便的对case进行参数化，使用@parameterized.expand()参数为一个list，每个list中为每次需要参数化数据的一个元祖

作者：忆江南_1569
链接：https://www.jianshu.com/p/d52c20cd7021
來源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。
"""