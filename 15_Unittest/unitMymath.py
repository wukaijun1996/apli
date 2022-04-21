#-*- codeing = utf-8 -*-
# @Time : 2022/4/21 20:36 
# @Author : wu
# @File : 02_unitMymath.py 
# @Software: PyCharm

import unittest
import myMath

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
        self.assertEqual(actualValue,expectValue,"预期结果与实际不相符")

    def test_add_3(self):
        print("我是第3条测试用例")

    def test_add_2(self):
        print("我是第2条测试用例")

    def tearDown(self) -> None:
        print("我是teardown方法")
        self.mm = None

if __name__ == '__main__':
    # unittest.main()
    suitt = unittest.TestSuite()

    # 追加单个测试用例到测试集合
    # suitt.addTest(unitMymath("test_add_1"))
    # suitt.addTest(unitMymath("test_add_3"))
    # suitt.addTest(unitMymath("test_add_2"))
    # 追加单个测试用例到测试集合
    # suitt.addTests(map(unitMymath,['test_add_1','test_add_3',]))


    loader = unittest.TestLoader()
    # suitt = loader.loadTestsFromName("unitMymath")
    # suitt = loader.loadTestsFromName("unitMymath.unitMymath")
    # suitt = loader.loadTestsFromName("unitMymath.unitMymath.test_add_1")

    # 指的是以unit开头，以.py结尾
    suitt = unittest.defaultTestLoader.discover(r"./15_Unittest/",pattern="unit*.py")

    res = unittest.TestResult()
    suitt.run(res)
    print(res.__dict__)






