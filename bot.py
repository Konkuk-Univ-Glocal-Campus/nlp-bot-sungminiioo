import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["그거 참 흥미로운데요, 더 자세히 말해주세요.",
                    "알겠어요. 계속 이야기해주세요.",
                    "왜 그렇게 말하시는 건가요?",
                    "요즘 날씨가 웃긴데, 그렇죠?",
                    "주제를 바꿔볼까요?",
                    "어젯밤 경기 보셨나요?"]

print("안녕하세요, 저는 Marvin이라고 하는 간단한 로봇입니다.")
print("'잘가'를 입력하여 언제든 대화를 마칠 수 있습니다.")
print("각 응답을 입력한 후 '엔터' 키를 누르세요.")
print("오늘 기분은 어떠신가요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "잘가":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("대화가 좋았어요. 안녕히 계세요!")
