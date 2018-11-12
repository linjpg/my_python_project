#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/29 14:36
# @Author  : linjunpeng
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# @Desc

dict = {"daily_limit20180929110525133_12": "50", "pond_type20180929110525133_19": "1",
        "pond_type20180929110525133_18": "1", "id20180929110525133_9": "9", "daily_limit20180929110525133_13": "150",
        "pond_type20180929110525133_13": "1", "pond_type20180929110525133_12": "1",
        "pond_type20180929110525133_11": "1", "id20180929110525133_8": "8", "pond_type20180929110525133_17": "1",
        "dynamic_num20180929110525133_19": "962", "pond_type20180929110525133_15": "1",
        "pond_type20180929110525133_14": "1", "daily_limit20180929110525133_1": "-1",
        "daily_limit20180929110525133_2": "-1", "daily_limit20180929110525133_3": "0",
        "daily_limit20180929110525133_4": "-1", "daily_limit20180929110525133_5": "-1",
        "daily_limit20180929110525133_6": "-1", "daily_limit20180929110525133_7": "-1", "id20180929110525133_7": "7",
        "id20180929110525133_6": "6", "id20180929110525133_5": "5", "id20180929110525133_4": "4",
        "id20180929110525133_3": "3", "id20180929110525133_2": "2", "id20180929110525133_1": "1",
        "id20180929110525133_12": "12", "daily_limit20180929110525133_19": "-1",
        "dynamic_num20180929110525133_8": "800", "id20180929110525133_11": "11", "daily_limit20180929110525133_8": "-1",
        "id20180929110525133_10": "10", "pond_type20180929110525133_16": "1", "dynamic_num20180929110525133_15": "397",
        "id20180929110525133_14": "14", "dynamic_num20180929110525133_11": "3", "id20180929110525133_20": "20",
        "id20180929110525133_17": "17", "id20180929110525133_16": "16", "daily_limit20180929110525133_10": "-1",
        "daily_limit20180929110525133_11": "1", "daily_limit20180929110525133_16": "-1",
        "daily_limit20180929110525133_17": "-1", "daily_limit20180929110525133_14": "-1",
        "daily_limit20180929110525133_15": "-1", "dynamic_num20180929110525133_13": "200",
        "dynamic_num20180929110525133_12": "50", "daily_limit20180929110525133_18": "-1",
        "dynamic_num20180929110525133_10": "4080", "dynamic_num20180929110525133_17": "2900",
        "dynamic_num20180929110525133_16": "1976", "id20180929110525133_19": "19", "id20180929110525133_18": "18",
        "dynamic_num20180929110525133_3": "20", "dynamic_num20180929110525133_2": "0",
        "dynamic_num20180929110525133_1": "0", "dynamic_num20180929110525133_7": "100",
        "pond_type20180929110525133_20": "1", "dynamic_num20180929110525133_5": "0",
        "dynamic_num20180929110525133_4": "0", "id20180929110525133_13": "13", "dynamic_num20180929110525133_9": "5000",
        "dynamic_num20180929110525133_14": "233", "daily_limit20180929110525133_9": "-1",
        "pond_type20180929110525133_4": "0", "dynamic_num20180929110525133_18": "1940",
        "daily_limit20180929110525133_20": "-1", "pond_type20180929110525133_10": "0",
        "pond_type20180929110525133_1": "0", "pond_type20180929110525133_9": "0", "pond_type20180929110525133_8": "0",
        "pond_type20180929110525133_7": "0", "pond_type20180929110525133_6": "0", "pond_type20180929110525133_5": "0",
        "id20180929110525133_15": "15", "pond_type20180929110525133_3": "0", "pond_type20180929110525133_2": "0",
        "dynamic_num20180929110525133_20": "1009", "dynamic_num20180929110525133_6": "0"}


# for i in dict:
#     print("dict[%s]=" % i,dict[i])
#
# # for item in dict:
# #     print(item)
#
# for (k,v) in  dict.items():
#         print ("dict[%s]=" % k,v )

# str = 'daily_limit_20180929151838354_20'
#
# #print(str.split('_')[-1])
# print('id' in str)
#
# config = dict
# data = {}
# id_list = []
# item_list = []
# if config:
#     for k, v in config.items():
#         if 'id' in k:
#             data['id'] = v
#             id_list.append(v)
#     for i in id_list:
#         item_data = {}
#         for k, v in config.items():
#             if (k.split('_')[-1] == i):
#                 item_data[k] = v
#         item_list.append(item_data)
#
# config_list = []
# #config_data = self.reset_data(config_data)
# for item in item_list:
#     status = 0
#     for k,v in item.items():
#         if 'pond_type' in k and int(v)==int(1):
#             status = 1
#         if 'dynamic_num' in k and int(v)<=int(2000):
#             print(v)
#             status = status+1
#     if status == 2:
#         config_list.append(item)
# print(config_list)


# def set(config_list):
#     # 所有符合条件的奖品
#     cfg_list = []
#     # 所有的非限制性奖
#     item_data_list = []
#     # 所有的限制性奖
#     limit_data_list = []
#     # 所有符合条件的非限制性奖品
#     non_list = []
#     # 幸运符
#     luck_item = None
#     config_list_data = [{'id_20180929164151546_18': '18', 'daily_limit_20180929164151546_18': '-1', 'pond_type_20180929164151546_18': '1', 'dynamic_num_20180929164151546_18': '1940'}, {'pond_type_20180929164151546_20': '1', 'dynamic_num_20180929164151546_20': '1009', 'id_20180929164151546_20': '20', 'daily_limit_20180929164151546_20': '-1'}]
#
#     version = '20180929164151546'
#     for config in config_list:
#         if int(config['pond_type']) == int(1):
#             if config['daily_limit'] == -1:
#                 item_data_list.append(config)
#             else:
#                 limit_data_list.append(config)
#             # 幸运符
#             if ['item_id'] == 1005:
#                 luck_item = config
#         i_id = config['id']
#         for item in config_list_data:
#             id_key = 'id_' + '%s_%s' % (version, i_id)
#             if id_key in item.keys():
#                 dynamic_num_key = 'dynamic_num_' + '%s_%s' % (version, i_id)
#                 daily_limit_key = 'daily_limit_' + '%s_%s' % (version, i_id)
#                 config['dynamic_num'] = item[dynamic_num_key]
#                 config['daily_limit'] = item[daily_limit_key]
#                 if int(item[daily_limit_key]) == -1:
#                     non_list.append(config)
#                 cfg_list.append(config)
#     print(cfg_list)


def reset_data(config):
    data = {}
    id_list = []
    item_list = []
    if config:
        for k, v in config.items():
            if 'id' in k:
                data['id'] = v
                id_list.append(v)
        print(id_list)
        for i in id_list:
            item_data = {}
            for k, v in config.items():
                if (k.split('_')[-1] == i):
                    item_data[k] = v
            item_list.append(item_data)
    return item_list


def set_data():
    # config_list_data = []
    # config_data ={"id_20180929172120874_14": "14", "id_20180929172120874_15": "15", "id_20180929172120874_16": "16", "id_20180929172120874_17": "17", "id_20180929172120874_10": "10", "id_20180929172120874_11": "11", "id_20180929172120874_12": "12", "id_20180929172120874_13": "13", "daily_limit_20180929172120874_20": "-1", "id_20180929172120874_18": "18", "daily_limit_20180929172120874_1": "-1", "daily_limit_20180929172120874_14": "-1", "daily_limit_20180929172120874_3": "0", "daily_limit_20180929172120874_7": "-1", "daily_limit_20180929172120874_6": "-1", "daily_limit_20180929172120874_5": "-1", "id_20180929172120874_8": "8", "daily_limit_20180929172120874_2": "-1", "daily_limit_20180929172120874_4": "-1", "id_20180929172120874_4": "4", "dynamic_num20180929172120874_17": "-1", "id_20180929172120874_6": "6", "id_20180929172120874_7": "7", "pond_type_20180929172120874_8": "0", "id_20180929172120874_5": "5", "id_20180929172120874_2": "2", "id_20180929172120874_3": "3", "id_20180929172120874_1": "1", "pond_type_20180929172120874_2": "0", "pond_type_20180929172120874_3": "0", "dynamic_num_20180929172120874_1": "0", "pond_type_20180929172120874_1": "0", "pond_type_20180929172120874_6": "0", "pond_type_20180929172120874_7": "0", "pond_type_20180929172120874_4": "0", "pond_type_20180929172120874_5": "0", "daily_limit_20180929172120874_17": "-1", "id_20180929172120874_20": "20", "dynamic_num_20180929172120874_8": "800", "dynamic_num_20180929172120874_9": "5000", "daily_limit_20180929172120874_13": "150", "daily_limit_20180929172120874_12": "50", "daily_limit_20180929172120874_11": "1", "daily_limit_20180929172120874_10": "-1", "dynamic_num_20180929172120874_2": "0", "dynamic_num_20180929172120874_3": "20", "daily_limit_20180929172120874_9": "-1", "daily_limit_20180929172120874_8": "-1", "dynamic_num_20180929172120874_6": "0", "dynamic_num_20180929172120874_7": "100", "dynamic_num_20180929172120874_4": "0", "dynamic_num_20180929172120874_5": "0", "pond_type_20180929172120874_20": "1", "pond_type_20180929172120874_9": "0", "pond_type_20180929172120874_18": "1", "dynamic_num_20180929172120874_20": "0", "daily_limit_20180929172120874_16": "-1", "pond_type_20180929172120874_14": "1", "pond_type_20180929172120874_15": "1", "pond_type_20180929172120874_16": "1", "pond_type_20180929172120874_17": "1", "pond_type_20180929172120874_10": "0", "pond_type_20180929172120874_11": "1", "pond_type_20180929172120874_12": "1", "pond_type_20180929172120874_13": "1", "daily_limit_20180929172120874_15": "-1", "dynamic_num_20180929172120874_18": "0", "dynamic_num_20180929172120874_19": "0", "daily_limit_20180929172120874_18": "-1", "dynamic_num_20180929172120874_14": "0", "dynamic_num_20180929172120874_15": "0", "dynamic_num_20180929172120874_16": "0", "dynamic_num_20180929172120874_17": "0", "dynamic_num_20180929172120874_10": "4080", "dynamic_num_20180929172120874_11": "0", "dynamic_num_20180929172120874_12": "0", "dynamic_num_20180929172120874_13": "10000", "id_20180929172120874_19": "19", "daily_limit_20180929172120874_19": "-1", "id_20180929172120874_9": "9", "pond_type_20180929172120874_19": "1"}
    #
    # config_data = reset_data(config_data)
    # print(config_data)
    # for item in config_data:
    #
    #     pond_type =
    #     dynamic_num = ''
    #     item[]
    #     int(item[pond_type]) == 1 and int(item[dynamic_num]) < 1000:
    #     config_list_data.append(item)
    # for k, v in item.items():
    #
    #     status = 0
    #     if 'pond_type' in k and int(v) == int(1) :
    #         status = 1
    #     if 'dynamic_num' in k and int(v) <= int(100000):
    #         status = status + 1
    #     if status == 2:
    #         config_list_data.append(item)
    # print(config_list_data)
    data = -1
    if data != 0:
        print ("000000")

def set_dict():
    keys = {"game_name", "icon", "sort", "update_url", "folder_name", "game_type", "platform"}
    for key in keys:
        #if keys[key] == 1 :
            print(keys[key])
def jiequ():
    str = '1001:100'
    # print(str[5:])
    # print(str[str.index(':') + 1:])
    # s = str.index(':')
    print(str.split(":")[1])

if __name__ == '__main__':
    # data =[{u'start_num': 0, u'item_id': 1, u'equal_money': 1000000, u'id': 1, u'pond_id': 1, u'putaway_money': 2000000, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 0}, {u'start_num': 0, u'item_id': 2, u'equal_money': 50000, u'id': 2, u'pond_id': 1, u'putaway_money': 100000, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 0}, {u'start_num': 20, u'item_id': 3, u'equal_money': 10000, u'id': 3, u'pond_id': 1, u'putaway_money': 20000, u'daily_limit': 0, u'pond_type': 0, u'dynamic_num': 20}, {u'start_num': 0, u'item_id': 4, u'equal_money': 100000, u'id': 4, u'pond_id': 1, u'putaway_money': 200000, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 0}, {u'start_num': 0, u'item_id': 5, u'equal_money': 50000, u'id': 5, u'pond_id': 1, u'putaway_money': 100000, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 0}, {u'start_num': 0, u'item_id': 6, u'equal_money': 10000, u'id': 6, u'pond_id': 1, u'putaway_money': 20000, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 0}, {u'start_num': 100, u'item_id': 7, u'equal_money': 5000, u'id': 7, u'pond_id': 1, u'putaway_money': 10000, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 100}, {u'start_num': 800, u'item_id': 8, u'equal_money': 1000, u'id': 8, u'pond_id': 1, u'putaway_money': 2000, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 800}, {u'start_num': 5000, u'item_id': 9, u'equal_money': 100, u'id': 9, u'pond_id': 1, u'putaway_money': 200, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 5000}, {u'start_num': 4080, u'item_id': 10, u'equal_money': 1000, u'id': 10, u'pond_id': 1, u'putaway_money': 0, u'daily_limit': -1, u'pond_type': 0, u'dynamic_num': 4080}, {u'start_num': 3, u'item_id': 1, u'equal_money': 1000000, u'id': 11, u'pond_id': 2, u'putaway_money': 2000000, u'daily_limit': 1, u'pond_type': 1, u'dynamic_num': 3}, {u'start_num': 50, u'item_id': 2, u'equal_money': 50000, u'id': 12, u'pond_id': 2, u'putaway_money': 100000, u'daily_limit': 50, u'pond_type': 1, u'dynamic_num': 50}, {u'start_num': 200, u'item_id': 3, u'equal_money': 10000, u'id': 13, u'pond_id': 2, u'putaway_money': 20000, u'daily_limit': 150, u'pond_type': 1, u'dynamic_num': 200}, {u'start_num': 250, u'item_id': 4, u'equal_money': 100000, u'id': 14, u'pond_id': 2, u'putaway_money': 20000, u'daily_limit': -1, u'pond_type': 1, u'dynamic_num': 233}, {u'start_num': 400, u'item_id': 5, u'equal_money': 50000, u'id': 15, u'pond_id': 2, u'putaway_money': 200000, u'daily_limit': -1, u'pond_type': 1, u'dynamic_num': 397}, {u'start_num': 2040, u'item_id': 6, u'equal_money': 10000, u'id': 16, u'pond_id': 2, u'putaway_money': 10000, u'daily_limit': -1, u'pond_type': 1, u'dynamic_num': 1976}, {u'start_num': 3000, u'item_id': 7, u'equal_money': 5000, u'id': 17, u'pond_id': 2, u'putaway_money': 10000, u'daily_limit': -1, u'pond_type': 1, u'dynamic_num': 2900}, {u'start_num': 2000, u'item_id': 8, u'equal_money': 1000, u'id': 18, u'pond_id': 2, u'putaway_money': 2000, u'daily_limit': -1, u'pond_type': 1, u'dynamic_num': 1940}, {u'start_num': 1000, u'item_id': 9, u'equal_money': 100, u'id': 19, u'pond_id': 2, u'putaway_money': 2000, u'daily_limit': -1, u'pond_type': 1, u'dynamic_num': 962}, {u'start_num': 1057, u'item_id': 10, u'equal_money': 0, u'id': 20, u'pond_id': 2, u'putaway_money': 0, u'daily_limit': -1, u'pond_type': 1, u'dynamic_num': 1009}]

    jiequ()
