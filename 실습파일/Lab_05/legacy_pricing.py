# [실습 1] 비즈니스 로직 해독
# 상황: 변수명이 엉망이고 주석이 없는 쇼핑몰 가격 계산 코드입니다.
# 미션: AI에게 "이 코드가 수행하는 '할인 정책'을 비즈니스 용어로 요약해줘"라고 요청하세요.

def c(p, t, m):
    # p: price, t: type, m: membership
    x = p
    if t == 1: # Electronics
        if x > 100000:
            x = x * 0.9
    elif t == 2: # Clothing
        if m == 'VIP':
            x = x * 0.8
        else:
            x = x * 0.95
    
    # Season Off
    if m == 'GUEST' and x > 50000:
        x = x - 2000
    
    return int(x)
