from utile import *

proxy = MysqlWrapper(
    host='140.112.42.193',
    database='test1',
    table='testtable',
    pending_queue = 'Pending',
    register_table = 'Register',
    user='punchshadow',
    password='kiny02153s'
)


inputList = [
    ['f00000000', '謝囉', '螢幕', '9393939-393939', 'No'],
    ['r88888888', '不謝', 'server', '00000-00000000', 'No'],
    ['b03030303', '太感謝', '鑰匙', '999999-9999999', 'No']
]


#proxy.addOne('f88888888', '大感謝', 'server', '000003-02222', 'No')
#proxy.addList(inputList)

#print(proxy.checkPropertyStudID('22222-3333333', 'r02222222'))
proxy.pendingInsert('0000000', 'oooooo', 'eeeeeee', '2020')
#proxy.requestPropChange('000003-02222', 'f88888888', 'r02222222', '2020.12.30-23:33')

#proxy.searchID('r02222222')
#proxy.searchProperty('39302020-3939202038')
