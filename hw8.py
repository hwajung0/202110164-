def buy(shopping_bag):
    while True:
        print('[구입]')
        item=input('상품명?')
        if item=='':
            return False
        quantity=int(input('수량은?'))
        shopping_bag[item]=quantity
        return print(f'장바구니에 {item} {quantity}개가 담겼습니다.\n')
   

def show(shopping_bag):
    return print(f'\n>>> 장바구니 보기: {shopping_bag}')

def find(shopping_bag):
    print('\n[검색]')
    item2=input('장바구니에서 확인하고자 하는 상품은?')
    def dict_get(dic,key):
        if key in dic:
            return dic[key]
        else:
            return None
    res=dict_get(shopping_bag,item2)
    if res!=None:
        return print(f'{item2}은(는) {shopping_bag.get(item2)}개 담겨 있습니다.')
    else:
        return print(f'장바구니에 {item2}은(는) 없습니다.')
    
shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)