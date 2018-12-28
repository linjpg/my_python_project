import requests
import json

import time


def draw_test():
    uid = '54036'
    lottery_type = '1'
    timestamp = get_time_stamp()
    url = "http://47.93.102.58:9277/lottery/lucky_draw_lottery?uid="+uid+"&lottery_type="+lottery_type+"&timestamp="+timestamp
    print('uid=%s,lottery_type=%s,timestamp=%s,url=%s'%(uid,lottery_type,timestamp,url))
    m = requests.get(url)
    print (json.dumps(m.json()))

    # 获取当前时间


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    #print(time_stamp)
    stamp = ("".join(time_stamp.split()[0].split("-")) + "".join(time_stamp.split()[1].split(":"))).replace('.', '')
    return stamp



if __name__ == '__main__':
    start_time = get_time_stamp()
    times = 0
    for i in range(800):
        times =times+1
        draw_test()
    print("总次数",times)
    end_time = get_time_stamp()
    pay_time = int(end_time)-int(start_time)
    print("开始时间",start_time)
    print("结束时间",end_time)
    print("最终花费时间",pay_time)





