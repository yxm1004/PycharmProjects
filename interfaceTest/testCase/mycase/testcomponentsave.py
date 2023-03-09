from interfaceTest.common.Logger import Logger
import unittest
from interfaceTest.requestsApi.confirmComponentAndBomApi import confirmComponentAndBomApi
from interfaceTest import readConfig

localReadConfig = readConfig.ReadConfig()


class testcomponentsave(unittest.TestCase):
    def setUp(self):
        # 引入新增构建类
        self.cm=confirmComponentAndBomApi()
    def test_post_componentsave(self):
        """
        新增-构建清单case
        """
        response=self.cm.componentsave()
        print("新增构建清单case",response.json())
        self.assertEqual(response.status_code, 200)
    def test_get_confimcomponentAndBom(self):
        """
        确认新增-构件清单case
        """
        response=self.cm.confirmComponentAndBom()
        print("确认新增构建清单case", response.json())
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()