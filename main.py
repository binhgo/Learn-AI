import http.client
import json


def array():
    days = ["a", "b", "c", "d", "e"]
    print(days[0:2])


def openFile():
    file = open("abc.txt", "r")
    file_text = file.read()
    print(file_text)


def printLala(bl):
    print("hahaha", "huhuhu")
    if True:
        print("true")
    else:
        print("false")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def forArray(arr):
    for a in arr:
        print(a)


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
    # print(jData)
    print(jData["data"]["order_code"])


def sum(a, b):
    return a + b


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = 10
    b = 20
    c = sum(a, b)
    print(c)
    # a = 1
    # b = 2
    # total = a + b
    # print(total)
    #
    # s = 'hello'
    # print(s)

    # for i in range(10):
    #     if i % 2 == 0:
    #         print(i)
    #     else:
    #         print('so le: ', i)

    # print_hi('PyCharm')
    # for i in range(1000):
    #     createOrder()
    # printLala(False)
    # openFile()
    # array()
    # print(sum("a", "1"))
    # days = ["a", "b", "c", "d", "e"]
    # forArray(days)
    # abc = 12
    # if abc == 100:
    #     print("100")
    # else:
    #     print("20000")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
