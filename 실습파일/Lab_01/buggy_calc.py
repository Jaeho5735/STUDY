# [Buggy Code] 쇼핑몰 할인 계산기
# 에러는 없는데 가끔 사장님이 화냄

def calculate_final_price(price, discount):
    # 1. 가격이 음수인 경우 처리
    if price < 0:
        return 0

    # 2. discount가 1보다 크면 백분율(%)로 간주하여 변환
    if discount > 1:
        discount = discount / 100

    # 3. 할인율 범위 제한 (0% ~ 100%)
    # 음수 할인은 0%로, 100% 초과 할인은 100%로 캡핑(Capping)
    discount = max(0, min(1, discount))

    final = price - (price * discount)
    return int(final)

# 테스트
print(calculate_final_price(10000, 0.2)) # 정상: 8000
print(calculate_final_price(10000, 20))  # 버그: -190000 (돈을 주고 물건을 팖)
