#-*- codeing = utf-8 -*-
# @Time : 2022/4/21 20:36 
# @Author : wu
# @File : 02_unitMymath.py 
# @Software: PyCharm
import datetime
import os
import unittest
import myMath
from HTMLTestRunner111 import HTMLTestRunner

class unitMymath(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("我是setupclass 方法")

    @classmethod
    def tearDownClass(cls) -> None:
        print("我是tearDownClass 方法")

    def setUp(self) -> None:
        print("我是setup方法")
        self.mm = myMath.mymath()

    def test_add_1(self):
        print("我是第一条测试用例")
        actualValue = self.mm.jia(9,13)
        expectValue = 22
        # self.assertEqual(actualValue,expectValue,"预期结果与实际不相符")
        # self.assertFalse(False)
        # self.assertTrue(True)
        # self.assertIs(actualValue,expectValue,"身份不相同")
        # self.assertIsNot(actualValue, expectValue, "身份相等")
        # self.assertIsNotNone(expectValue,"是空的")
        # self.assertNotIn('a','bc')
        # self.assertIn('a','abc')
        # self.assertIsInstance(self.mm,myMath.mymath)
        # self.assertIsInstance("ss",str)
        self.assertNotIsInstance("ss",int)


    def test_add_3(self):
        print("我是第3条测试用例")

    def test_add_2(self):
        print("我是第2条测试用例")

    def tearDown(self) -> None:
        print("我是teardown方法")
        self.mm = None

if __name__ == '__main__':
    # unittest.main()

    # TestSuite
    # 创建测试集合
    # suitt = unittest.TestSuite()
    # 追加单个测试用例到测试集合
    # suitt.addTest(unitMymath("test_add_1"))
    # suitt.addTest(unitMymath("test_add_3"))
    # suitt.addTest(unitMymath("test_add_2"))
    # 追加单个测试用例到测试集合
    # suitt.addTests(map(unitMymath,['test_add_1','test_add_3',]))

    # TestLoader
    # loader = unittest.TestLoader()
    # suitt = loader.loadTestsFromName("unitMymath")
    # suitt = loader.loadTestsFromName("unitMymath.unitMymath")
    # suitt = loader.loadTestsFromName("unitMymath.unitMymath.test_add_1")

    # 指的是以unit开头，以.py结尾
    case_path = os.path.dirname(__file__)
    suitt = unittest.defaultTestLoader.discover(case_path,pattern='unit*.py')
    # print(suitt.countTestCases())

    # res = unittest.TestResult()
    # suitt.run(res)
    # print(res.__dict__)

    # 格式化当前时间
    cur_time = datetime.datetime.now()
    str_time = "{}-{}-{}-{}-{}-{}".format(cur_time.year, cur_time.month, cur_time.day, cur_time.hour, cur_time.minute, cur_time.second)

    #TextTestRunner（）提供的run方法运行测试集合
    # with open(str_time+'.html',"w",encoding="utf-8") as f:
    #     runner = unittest.TextTestRunner(f,descriptions="单元测试报告执行",verbosity=2)
    #     runner.run(suitt)

    #HTMLTestRunner（）使用第三方库
    with open(str_time+'.html',"wb") as f:
        runner = HTMLTestRunner(f,verbosity=2,title="单元测试报告",description="第一次运行的结果")
        runner.run(suitt)









