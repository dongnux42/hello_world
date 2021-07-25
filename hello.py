#예제 3
#클래스 변수, 인스턴트 변수
class Warehouse:
    #클래스 변수 = 0
    stock_num = 0 #재고

    def __init__(self, name):
        #인스턴스 변ㅅ
        self.name = name
        Warehouse.stock_num += 1
    #소멸할 때 실행
    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
