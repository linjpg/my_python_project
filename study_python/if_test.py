import redis
import datetime
import time


def get_time_stamp():
    # list = []
    # if list:
    #     print('============1')
    # else:
    #     print('--------------2')
    ct = time.time()
    local_time = time.localtime(ct)
    today = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print(today)
    re = redis.StrictRedis(host='localhost', port=6379, db=0)
    task_five_key = "FLASH_TASK_FIVE_" + str(2)
    task_five_value = "FLASH_TASK_FIVE_:%s:%s" % (2, today)
    data = re.get(task_five_key)
    print(data)
    if data:
        time_value = str(data[-19:])
        print("=========", time_value)
    else:
        re.set(task_five_key, task_five_value)
    print(task_five_value)

    # if today.strftime('%Y-%m-%d %H:%M:%S') == time_value:
    #     print('==========================')

    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    print(type(yesterday.strftime('%Y-%m-%d')))
    print(type(yesterday.strftime('%Y-%m-%d')))


def time_a():
    import time
    import datetime

    dtime = datetime.datetime.now()
    ans_time = time.mktime(dtime.timetuple())
    print(time)
    print(ans_time)
    return ans_time


def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    # value为传入的值为时间戳(整形)，如：1332888820
    value = time.localtime(value)
    ## 经过localtime转换后变成
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式。
    dt = time.strftime(format, value)
    print(dt)
    a = (datetime.datetime.now() + datetime.timedelta(minutes=-2)).strftime("%Y-%m-%d %H:%M:%S")
    print(a)
    return dt


def get_time_stamp_num(data_head):
    time_stamp = "%s" % (data_head)
    print(time_stamp)
    stamp = ("".join(time_stamp.split()[0].split("-")) + "".join(time_stamp.split()[1].split(":"))).replace('.', '')
    return stamp


def time_expire():
    format = '%Y-%m-%d %H:%M:%S'
    data_head = (datetime.datetime.now() + datetime.timedelta(minutes=-2)).strftime('%Y-%m-%d %H:%M:%S')
    head_time = int(get_time_stamp_num(data_head))
    data_head = (datetime.datetime.now() + datetime.timedelta(minutes=-2)).strftime('%Y-%m-%d %H:%M:%S')
    tail_time = int(get_time_stamp_num(data_head))
    value = time.localtime(1540553063)
    dt = time.strftime(format, value)
    c_time = int(get_time_stamp_num(dt))
    print(head_time)
    print(c_time)

def time_a():
    a = datetime.datetime.now().strftime('%Y-%m-%d')
    print(a)



if __name__ == '__main__':
    #time_a()
    #timestamp_datetime(1540552067)
    #get_time_stamp()
    #time_expire()
    time_a()