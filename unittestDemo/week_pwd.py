#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest

class PasswordTestCase(unittest.TestCase):

    def setUp(self):
        print('set up')
        self.test_data = [
            {"name": "jack", "password": "Iloverose"},
            {"name": "rose", "password": "Ilovejack"},
            {"name": "tom", "password": "password123"},
            {"name": "jerry", "password": "password"}
        ]

    def test_week_password(self):
        for data in self.test_data:
            passwd = data['password']
            self.assertTrue(len(passwd) >= 6)
            msg = "user %s has a weak password" %(data['name'])
            self.assertTrue(passwd != 'password', msg)
            self.assertTrue(passwd != 'password123', msg)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()