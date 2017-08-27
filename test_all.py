import unittest
from testcase import test1,test2

def suite():
	suite = unittest.TestSuite()
	suite.addTest(test1.BaiduWebdriver("test_baidu_webdriver"))
	suite.addTest(test2.So360("test_so360"))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
