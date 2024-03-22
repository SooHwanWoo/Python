def exchange(money):
    a = money//500
    print("500원동전의 개수:", a)
    money -= 500*a
    b = money//100
    print("100원동전의 개수:", b)
    money -= 100*b
    c = money//50
    money -= 50*c
    print("50원동전의 개수:", c)
    d = money//10
    print("10원동전의 개수:", d)

def get_integer(prompt):
    return int(input(prompt))

msg = "동전으로 교환하고자 하는 금액은?"
amount = get_integer(msg)
exchange(amount)
