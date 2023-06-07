import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from controller.user_controller import UserController
from controller.group_controller import GroupController
from controller.bill_controller import BillController

from services.user_service import UserService
from services.group_service import GroupService
from services.bill_service import BillService

'''
Should not use services directly. Instead use factory pattern
eg:
def bill_factory(type):
    if type == 'bill1':
        return BillService()
    elif type == 'bill2':
        return BillService2()

In driver
bill_controller = BillController(bill_factory('bill1')) 
'''

user_controller = UserController(UserService())
group_controller = GroupController(GroupService())
bill_controller = BillController(BillService())

user1 = user_controller.add_user('user1', 'Japteg')
user2 = user_controller.add_user('user2', 'Abhinav')
user3 = user_controller.add_user('user3', 'Raghav')
user4 = user_controller.add_user('user4', 'Bandar')
user5 = user_controller.add_user('user5', 'Aditya')

members = [user1, user2, user3, user4, user5]
group1 = group_controller.add_group('group1', 'friends', members)

paid_by = {
    'user1': 100,
    'user2': 50,
    'user3': 100,
    'user4': 200,
    'user5': 50,
}

contribution = {
    'user1': 100,
    'user2': 100,
    'user3': 100,
    'user4': 100,
    'user5': 100,
}

bill = bill_controller.add_bill('bill1', group1.get_id(), 500, contribution, paid_by)

for user in group1.get_members():
    balance = bill_controller.get_user_balance(user.get_id())
    print(f'{user.get_id()}: {balance} Rs')
