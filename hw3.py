def get_fixed_price(d, p):
    price = p*100/(100-d)
    return int(price)

discount = int(input('할인율은?'))
a_p=int(input('A 상품의 할인된 가격은?'))
b_p=int(input('B 상품의 할인된 가격은?'))
print('A 상품의 정가는', get_fixed_price(discount, a_p),'원')
print('B 상품의 정가는', get_fixed_price(discount, b_p),'원')
