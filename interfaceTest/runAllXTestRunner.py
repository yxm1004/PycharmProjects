from datetime import datetime
import os
import unittest
from XTestRunner import HTMLTestRunner

from interfaceTest import readConfig

resultPath = os.path.join(readConfig.proDir, "result")
resultPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))

resultPath = os.path.join(resultPath, "test_result.html")

class TestDemo(unittest.TestCase):
    """测试用例说明"""

    def test_success(self):
        """执行成功"""
        self.assertEqual(2 + 3, 5)

    @unittest.skip("skip case")
    def test_skip(self):
        """跳过用例"""
        pass

    def test_fail(self):
        """失败用例"""
        self.assertEqual(6, 6)

    def test_error(self):
        """错误用例"""
        self.assertEqual(6, 6)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests([
        TestDemo("test_success"),
        TestDemo("test_skip"),
        TestDemo("test_fail"),
        TestDemo("test_error")
    ])
    fp = open(resultPath, 'wb')
    print("4444444444444444444444",fp)
    runner = HTMLTestRunner(
        stream=fp,
        title='<project name>test report',
        description='describe: ... ',
        language='en',
        rerun=3
    )
    runner.run(suit)
