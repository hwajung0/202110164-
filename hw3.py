def get_fixed_price(price):
    정가=price/((100-h)*0.01)
    return 정가
h=int(input('할인율은?'))
A할인=int(input('A상품의 할인된 가격은?'))
B할인=int(input('B상품의 할인된 가격은?'))
print('A 상품의 정가는',get_fixed_price(A할인),'원')
print('B 상품의 정가는',get_fixed_price(B할인),'원')
