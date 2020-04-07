from business.buildingView import BuildingView
import unittest,logging,time
class TestBuilding(unittest.TestCase):
    def test_builds(self):
        '''测试楼栋列表接口'''  # 此注释将展示到测试报告的测试组类
        B = BuildingView()
        B.builds()
    def test_builds_add(self):
        '''测试添加楼栋接口'''  # 此注释将展示到测试报告的测试组类
        B = BuildingView()
        form_data = {
            'contract_id': 253,
            'building_num': '楼栋031601',
            'building_area': 2000000,
            'floor_up': 10,
            'floor_down': 2,
            'height': 10,
            'building_structure': '钢筋水泥',
            'building_basic': '钢筋',
            'tech_user': 19,
            'civil_user': 39,
            'water_user': 33,
            'elec_user': 124,
            'deco_user': 124,
            'tester': 87,
            'safer': 83,
            'quality_user': 25,
            'data_user': 27,
            'budget_user': 63,
            'logistics_user': 105

        }
        B.building_add(form_data)