import time
import unittest
from script.testlogin import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner

suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(TestLogin))

report_file ="./report/report{}.html".format(time.strftime("%Y%m%d_%H%M%S"))
with open(report_file,"wb") as f:
    runner =HTMLTestRunner(f,title="charles接口自动化测试报告",description="V0.1")
    #testsuite
    runner.run(suit)
