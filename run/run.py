# coding: utf-8
import unittest
from  BSTestRunner import BSTestRunner
from HTMLTestRunnerNew import HTMLTestRunner
import time,logging
import sys
path='F:\\测试\\软件\\我要自学\\wisdomApi\\'
sys.path.append(path)

test_dir='../case'
report_dir='../reports'

from case.test_technical_disclosure_scheme import TechnicalDisclosureScheme
from case.test_baseMenu import TestBaseMenu
# from business.technical_disclosure_scheme import technicalDisclosureSchemeView

# 未按顺序执行测试用例
# discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

# 测试套件，定义测试用例执行顺序
suite = unittest.TestSuite()

# 技术交底与方案
suite.addTest(TechnicalDisclosureScheme('test_technical_disclosure_scheme_add'))
suite.addTest(TechnicalDisclosureScheme("test_technical_disclosure_scheme_list"))
suite.addTest(TechnicalDisclosureScheme("test_technical_disclosure_scheme_approval"))

suite.addTest(TestBaseMenu('test_base_menu'))
suite.addTest(TestBaseMenu('test_behavior'))
suite.addTest(TestBaseMenu('test_user_info'))
suite.addTest(TestBaseMenu('test_toDoBusiness'))
suite.addTest(TestBaseMenu('test_toDoList'))

# suite.addTest(technicalDisclosureSchemeView("test_technical_disclosure_scheme_add"))

runner = unittest.TextTestRunner()

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='ShortVideo Test Report',description='ShortVideo Android app test report')
    logging.info('start run test case...')
    # runner.run(discover)

    runner.run(suite)