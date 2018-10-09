import requests
import json


def TestQueryBalance(uid, account_type):
    body = {
        "uid": int(uid),
        "source_type": 100,
        "token": "100",
        "account_type": account_type
    }
    print (json.dumps(body))
    m = requests.post('http://10.55.3.227:22060/coin/BillCoinService/QueryBalance', data=json.dumps(body))
    print (json.dumps(m.json()))


def TestUpdate(uid, coin, account_type):
    body = {
        "uid": int(uid),
        "source_type": 100,
        "token": "100",
        "account_type": account_type,
        "coin": int(coin),
        "source_desc": "test",
    }
    # print json.dumps(body)
    m = requests.post('http://10.55.3.227:22060/coin/BillCoinService/GetBillID', data=json.dumps(body))
    # print json.dumps(m.json())
    body["bill_id"] = m.json()["bill_id"]
    # print json.dumps(body)
    m = requests.post('http://10.55.3.227:22060/coin/BillCoinService/UpdateCoin', data=json.dumps(body))
    print (json.dumps(m.json()))


if __name__ == '__main__':
    import sys

    # if len(sys.argv) != 4 or (sys.argv[2] != "gold_coin" and sys.argv[2] != "laidou_coin"):
    #     print sys.argv
    #     print 'Usage:[python add_coin.py uid coin_type coin]'
    #     print 'eg:[python add_coin.py 144247 laidou_coin 1000]'
    #     print 'support laidou_coin gold_coin'
    #     exit(1)
    # TestUpdate(sys.argv[1], sys.argv[3], sys.argv[2])
    # TestUpdate(sys.argv[1], sys.argv[3], sys.argv[2])
    # TestQueryBalance(sys.argv[1])

    uid = 54194
    TestQueryBalance(uid, 'gold_coin')

    #TestUpdate(uid, 8000, 'gold_coin')
    # TestQueryBalance(54054)

TestUpdate(54036, -2276556, 'gold_coin')
# TestUpdate(54031, -55, 'laidou_coin')
# TestUpdate(54054, -2, 'laidou_coin')
# TestUpdate(54067, -10, 'laidou_coin')

#TestUpdate(54171, -1, 'laidou_coin')

#TestUpdate(54194, -47, 'laidou_coin')


