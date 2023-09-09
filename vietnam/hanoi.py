import json

with open("C:\\Users\\AnhPham\\Desktop\\LocationFinder\\vietnam\\hanoi.json", "r") as hanoiJson:
    hotels = json.load(hanoiJson)

def locDesc():
    return "Thủ đô của Việt Nam với nhiều địa điểm lịch sử và văn hóa như Hoàn Kiếm Lake, Ngọc Sơn Temple, và khu phố cổ Hà Nội."

def getHotel(hotelStar):
    print(hotels)