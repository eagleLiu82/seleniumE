import unittest
from testcase import baidu,so360

def suite():
	suite = unittest.TestSuite()
	suite.addTest(baidu.BaiduWebdriver("test_baidu_webdriver"))
	suite.addTest(so360.So360("test_so360"))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')