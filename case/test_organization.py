from business.organizationView import Organization
import unittest,logging,time
class TestOrganization(unittest.TestCase):
    def test_department(self):
        '''测试部门列表'''
        O = Organization()
        O.department()
    def test_departmentUser(self):
        '''部门员工列表'''
        O = Organization()
        O.departmentUser()

    def test_station(self):
        '''岗位列表'''
        O = Organization()
        O.station()
    def test_getBasicInfo(self):
        '''学位信息列表'''
        O = Organization()
        O.getBasicInfo()



    def test_addDepartment(self):
        '''添加部门'''
        O = Organization()
        data ={

            'name': '添加部门62',
            'parent_id': 44
        }
        O.addDepartment(data)
    def test_editDepartment(self):
        '''编辑部门'''
        O = Organization()
        data = {
            'id':61,
            'name': '添加部门65',
            'parent_id': 44
        }
        O.editDepartment(data)
if __name__ == '__main__':
    O = TestOrganization()
    # O.test_department()
    O.test_addDepartment()
    # O.test_editDepartment()