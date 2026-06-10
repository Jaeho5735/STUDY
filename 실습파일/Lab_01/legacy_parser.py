# [Legacy Code] 작성자: 퇴사자A (2019)
# 건드리지 마시오. 돌아가긴 함.
import re

def p(t):
    # m = re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", t)
    # 위 정규식이 가끔 에러나서 아래걸로 바꿈
    if '@' in t:
        sp = t.split('@')
        if len(sp) == 2:
            if '.' in sp[1]:
                return True
    return False

def c(d):
    # 전화번호 처리?
    return d.replace('-', '').replace(' ', '')
