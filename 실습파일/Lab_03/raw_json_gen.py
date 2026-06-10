# [실습 3] Format Control
# 목표: 까다로운 규칙을 준수하는 JSON 데이터를 생성하세요.
# Bad Prompt: "이 데이터로 JSON 만들어줘"
# Good Prompt: "결과를 JSON으로 출력하되, 1) 모든 Key는 snake_case, 2) 전화번호 없으면 'N/A', 3) 날짜는 YYYY-MM-DD 형식으로 변환해."

users = [
    {"Name": "Alice", "Phone": "010-1234-5678", "JoinedAt": "2024.01.01"},
    {"Name": "Bob", "Phone": None, "JoinedAt": "2024/02/15"},
    {"Name": "Charlie", "Phone": "010-9876-5432", "JoinedAt": "2024-03-10"}
]

def generate_custom_json(data):
    # 여기에 AI가 짠 코드를 붙여넣으세요.
    pass
