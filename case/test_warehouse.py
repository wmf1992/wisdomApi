from business.warehouseView import WarehouseView
import unittest,logging,time
class TestWarehouse(unittest.TestCase):
    def test_get_warehouse(self):
        '''测试仓库列表接口'''  # 此注释将展示到测试报告的测试组类
        M = WarehouseView()
        M.get_warehouse()
    def test_warehouse_add(self):
        '''测试添加仓库接口'''  # 此注释将展示到测试报告的测试组类
        M = WarehouseView()
        form_data = {
            'warehouse_name': '仓库031802',
            'warehouse_address': '福建省厦门市集美区',
            'manager_user': 76,
            'approval_user': 17,
            'contract_id': 41,
            'is_build': 1
        }
        M.warehouse_add(form_data)