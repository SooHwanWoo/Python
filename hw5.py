def read_single_digit(n):
    dic = {1:"일", 2:"이", 3:"삼", 4:"사", 5:"오",
       6:"육", 7:"칠", 8:"팔", 9:"구", 0:"영"}
    return dic[int(n)]

def read_number(N):
    msg=""
    for i in N:
        msg += read_single_digit(i)
        msg += " "
    return msg

num = input("세 자리 정수 입력?")
print(read_number(num))
