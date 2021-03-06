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
from case.test_building import TestBuilding
from case.test_contract_sign_apply_record import TestContractSignApplyRecord
from case.test_contract import TestContract
from case.test_labour_services import TestLabourServices
from case.test_meterial import TestMeterial
from case.test_meterialtype import TestMeterialtype
from case.test_organization import TestOrganization
from case.test_staff import TestStaff
from case.test_user import TestUsers
from case.test_warehouse import TestWarehouse
from case.test_work_type import TestWorkType
from case.test_progress_plan import TestProgressPlan
from case.test_quality_check import TestQualityCheck
from case.test_sub_project import TestSubProject
from case.test_month_bulk_meterial_plan import TestMonthBulkMeterialPlan
from case.test_meterial_warehousing import TestMeterialWarehousing
from case.test_meterial_plan import TestMeterialPlan
from case.test_meterial_outbound import TestMeterialOutbound
from case.test_meterial_inventory import TestMeterialInventory
# 未按顺序执行测试用例
# discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

# 测试套件，定义测试用例执行顺序
suite = unittest.TestSuite()

# 技术交底与方案
suite.addTest(TechnicalDisclosureScheme('test_technical_disclosure_scheme_add'))
suite.addTest(TechnicalDisclosureScheme("test_technical_disclosure_scheme_list"))
suite.addTest(TechnicalDisclosureScheme("test_technical_disclosure_scheme_approval"))
suite.addTest(TechnicalDisclosureScheme("test_technical_disclosure_scheme_detail"))
suite.addTest(TechnicalDisclosureScheme("test_technical_disclosure_scheme_approval_detail"))


suite.addTest(TestBaseMenu('test_base_menu'))
suite.addTest(TestBaseMenu('test_behavior'))
suite.addTest(TestBaseMenu('test_user_info'))
suite.addTest(TestBaseMenu('test_toDoBusiness'))
suite.addTest(TestBaseMenu('test_toDoList'))

# 楼栋管理
suite.addTest(TestBuilding('test_builds'))
suite.addTest(TestBuilding('test_builds_add'))

# 合同签订申请
suite.addTest(TestContractSignApplyRecord('test_contract_sign_apply_record_index'))
suite.addTest(TestContractSignApplyRecord('test_contract_sign_apply_record_add'))

# 合同管理
suite.addTest(TestContract('test_contract_apply_record'))
suite.addTest(TestContract('test_labourContract_add'))

# 劳务公司管理
suite.addTest(TestLabourServices('test_get_labour_services'))
suite.addTest(TestLabourServices('test_get_labour_services_black'))
suite.addTest(TestLabourServices('test_labour_services_add'))

# 材料管理
suite.addTest(TestMeterial('test_get_meterial'))
suite.addTest(TestMeterial('test_meterial_add'))
suite.addTest(TestMeterial('test_get_meterial_approval'))
suite.addTest(TestMeterial('test_meterial_approval_check'))

# 材料分类
suite.addTest(TestMeterialtype('test_get_meterial_type'))
suite.addTest(TestMeterialtype('test_meterial_type_add'))

# 组织架构
suite.addTest(TestOrganization('test_department'))
suite.addTest(TestOrganization('test_departmentUser'))
suite.addTest(TestOrganization('test_station'))
suite.addTest(TestOrganization('test_getBasicInfo'))
suite.addTest(TestOrganization('test_addDepartment'))
suite.addTest(TestOrganization('test_editDepartment'))

# 劳务人员

suite.addTest(TestStaff('test_get_staff'))
suite.addTest(TestStaff('test_labourForceDetails'))
suite.addTest(TestStaff('test_get_staff_black'))
suite.addTest(TestStaff('test_staff_add'))

# 员工管理
suite.addTest(TestUsers('test_users'))
suite.addTest(TestUsers('test_userinfo'))

# 工种列表
suite.addTest(TestWorkType('test_work_type'))
suite.addTest(TestWorkType('test_work_type_add'))

# 仓库列表
suite.addTest(TestWarehouse('test_get_warehouse'))
suite.addTest(TestWarehouse('test_warehouse_add'))

# 进度计划

suite.addTest(TestProgressPlan('test_progress_plan_index'))
suite.addTest(TestProgressPlan('test_progress_plan_add'))
suite.addTest(TestProgressPlan('test_progress_plan_testSave'))
suite.addTest(TestProgressPlan('test_progress_plan_submit'))
suite.addTest(TestProgressPlan('test_progress_plan_approval_add'))
suite.addTest(TestProgressPlan('test_progress_plan_detail'))

# 质量检查
suite.addTest(TestQualityCheck('test_quality_check_add'))
suite.addTest(TestQualityCheck('test_quality_check_index'))
suite.addTest(TestQualityCheck('test_quality_check_approval'))
suite.addTest(TestQualityCheck('test_quality_check_detail'))


# 工程结算
suite.addTest(TestSubProject('test_sub_project_index'))
suite.addTest(TestSubProject('test_sub_project_detail'))
suite.addTest(TestSubProject('test_sub_project_add'))
suite.addTest(TestSubProject('test_sub_project_check'))

# 月大宗材料计划
suite.addTest(TestMonthBulkMeterialPlan('test_month_bulk_meterial_plan_index'))
suite.addTest(TestMonthBulkMeterialPlan('test_month_bulk_meterial_plan_detail'))
suite.addTest(TestMonthBulkMeterialPlan('test_month_bulk_meterial_plan_add'))
suite.addTest(TestMonthBulkMeterialPlan('test_month_bulk_meterial_plan_approval'))


# 入库
suite.addTest(TestMeterialWarehousing('test_meterial_warehousing_index'))
suite.addTest(TestMeterialWarehousing('test_meterial_warehousing_detail'))
suite.addTest(TestMeterialWarehousing('test_meterial_warehousing_add'))
suite.addTest(TestMeterialWarehousing('test_warehousing_approval_check'))

# 日常材料计划
suite.addTest(TestMeterialPlan('test_meterial_plan_index'))
suite.addTest(TestMeterialPlan('test_meterial_plan_detail'))
suite.addTest(TestMeterialPlan('test_meterial_plan_add'))
suite.addTest(TestMeterialPlan('test_meterial_plan_approval'))

# 出库
suite.addTest(TestMeterialOutbound('test_meterial_outbound_index'))
suite.addTest(TestMeterialOutbound('test_meterial_outbound_detail'))
suite.addTest(TestMeterialOutbound('test_meterial_outbound_add'))
suite.addTest(TestMeterialOutbound('test_outbound_approval_check'))


# 盘点
suite.addTest(TestMeterialInventory('test_meterial_inventory_index'))
suite.addTest(TestMeterialInventory('test_meterial_inventory_detail'))
suite.addTest(TestMeterialInventory('test_meterial_inventory_add'))
suite.addTest(TestMeterialInventory('test_inventory_approval_check'))



runner = unittest.TextTestRunner()

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='智慧工程接口测试报告',description='2020年3月份，王梅芳编写的脚本')
    logging.info('start run test case...')
    # runner.run(discover)

    runner.run(suite)