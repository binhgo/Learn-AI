import http.client
import json
import time
from threading import Thread
import mongo

arr_order = []


def createOrder():
    conn = http.client.HTTPSConnection("dev-online-gateway.ghn.vn")

    payload = "{\n    \"shop_id\": 76896,\n    \"payment_type_id\": 1,\n    \"note\": \"Notes cho field notes\",\n    \"required_note\": \"KHONGCHOXEMHANG\",\n    \"return_phone\": \"0916192647\",\n    \"return_address\": \"Địa chỉ trả nha\",\n    \"return_district_id\": \"1631\",\n    \"return_ward_code\": \"300105\",\n    \"client_order_code\": \"\",\n    \"to_name\": \"Trần Văn Nhận\",\n    \"to_phone\": \"0916192647\",\n    \"to_address\": \"111D Lý Chính Thắng, Phường 7, Quận 3, Thành phố Hồ Chí Minh, Việt Nam\",\n    \"to_ward_code\": \"301003\",\n    \"to_district_id\": 1631,\n    \"cod_amount\": 1000001,\n    \"content\": \"Nhập cho Nội dung sản phẩm\",\n    \"weight\": 300,\n    \"length\": 11,\n    \"width\": 12,\n    \"height\": 13,\n    \"pick_station_id\": 0,\n    \"deliver_station_id\": 0,\n    \"insurance_value\": 10000000,\n    \"order_value\": 10000,\n    \"service_id\": 53320,\n    \"coupon\": \"\",\n    \"total_service\": 20900,\n    \"updated_client\": 500393,\n    \"updated_employee\": 1,\n    \"items\": [\n        {\n            \"name\": \"Sản phẩm 001\",\n            \"code\": \"MaSanPham001\",\n            \"quantity\": 1\n        }\n    ]\n}"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic b25saW5lOnl6MmdxeWdiSGJKV0JENXpra2pRSmdqU1o2MzRWYkFx'
    }

    conn.request("POST", "/tenant/api/v2/shipping-order/create", payload.encode('utf-8'), headers)
    res = conn.getresponse()
    data = res.read()
    jData = json.loads(data.decode("utf-8"))
    print(jData["data"]["order_code"])
    arr_order.append(jData["data"]["order_code"])


def queryOrder(orderCode):
    conn = http.client.HTTPSConnection("dev-nhanh-api.ghn.dev")
    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YmFja2VuZDp2eW02UFV5cE9hSm1EZDRNbHNEU3luazl0MGhudUNJNA=='
    }

    str = "/core/order-crud/v1/internal/order?order_code=" + orderCode

    conn.request("GET", str, payload, headers)
    res = conn.getresponse()
    data = res.read()
    jData = json.loads(data.decode("utf-8"))

    if "OK" != jData["status"]:
        print(jData["status"])
    # for order in jData["data"]:
    #     print(order["order_code"])
    # print(jData["data"]["order_code"])
    # print(data.decode("utf-8"))


def createOrderWithThread(num):
    # create a list of threads
    threads = []
    # In this case 'urls' is a list of urls to be crawled.
    for ii in range(num):
        # We start one thread per url present.
        process = Thread(target=createOrder)
        process.start()
        threads.append(process)


def checkLogWithThread(orders):
    # create a list of threads
    threads = []
    # In this case 'urls' is a list of urls to be crawled.
    for oo in orders:
        # We start one thread per url present.
        process = Thread(target=readLog(oo))
        process.start()
        threads.append(process)


def readLog(orderCode):
    filter = {"data": orderCode}
    result = mongo.cLog().find_one(filter)
    if result is None:
        print('cannot find order: ' + orderCode)
    print('log: ', orderCode)


def checkOrderDataWithThread(orders):
    # create a list of threads
    threads = []
    # In this case 'urls' is a list of urls to be crawled.
    for oo in orders:
        # We start one thread per url present.
        process = Thread(target=readOrderData(oo))
        process.start()
        threads.append(process)


def readOrderData(orderCode) -> str:
    filter = {"order_code": orderCode}
    result = mongo.cOrder().find_one(filter)
    if result is None:
        print('core order not found: ' + orderCode)
        return ''

    if result['updated_client'] != 'core/online-consumer':
        print('order created by: ' + result['updated_client'])


if __name__ == '__main__':
    # readOrderData('ZNRHD_PR')
    createOrderWithThread(100)

    # # read log
    # print('sleep 1')
    # time.sleep(5)
    #
    # print('loop 1')
    # checkLogWithThread(arr_order)
    # # for orderCode in arr_order:
    # #     readLog(orderCode)
    #
    # print('done 1')

    # read order
    print('sleep 2')
    # time.sleep(20)

    print('loop 2')
    # checkOrderDataWithThread(arr_order)

    print('done 2')
