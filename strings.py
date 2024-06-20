import random
# 언어 지원하는 파일 #
## 언어를 추가할 때 그 언어로 인삿말 리스트를 작성하고, 프로그램에서 출력할 string 값 여기에 등록! ##

# 인삿말 리스트
messages = [
    "좋은 하루 되세요!", "오늘도 수고하셨습니다.", "편안한 밤 되세요.", "즐거운 하루 보내세요.", "행복한 하루 되세요.",
    "오늘도 파이팅!", "시원한 커피 한 잔 어때요?", "건강하세요!", "맛있는 식사 하세요.", "힘찬 하루 되세요.",
    "기분 좋은 하루 되세요.", "오늘도 화이팅!", "멋진 하루 보내세요.", "오늘 하루도 빛나세요.", "행운을 빌어요!",
    "오늘은 여유롭게 보내세요.", "행복한 하루 되시길!", "좋은 저녁 되세요.", "오늘은 영화 한 편 어떠세요?", "편안한 주말 되세요.",
    "오늘도 즐겁게!", "따뜻한 차 한 잔 어때요?", "행복한 하루 보내세요.", "좋은 일만 가득하세요!", "오늘도 즐거운 하루!",
    "멋진 저녁 되세요", "편안한 저녁 보내세요", "건강한 하루 되세요", "기분 좋은 하루 보내세요", "행복 가득한 하루 되세요",
    "오늘도 웃음 가득한 하루 되세요", "오늘도 힘내세요", "즐거운 시간 보내세요", "행복한 시간 되세요", "좋은 아침 되세요",
    "행복한 하루 되세요", "기분 좋은 아침 되세요", "오늘도 파이팅!", "즐거운 아침 되세요", "편안한 하루 되세요"
]


def farewell():
    messages = ["좋은 하루 되세요!","오늘도 수고하셨습니다.","편안한 밤 되세요.","즐거운 하루 보내세요.","행복한 하루 되세요.","오늘도 파이팅!","시원한 커피 한 잔 어때요?","건강하세요!","맛있는 식사 하세요.","힘찬 하루 되세요!","기분 좋은 하루 되세요.","오늘도 화이팅!","멋진 하루 보내세요.","오늘 하루도 빛나세요.","행운을 빌어요!","오늘은 여유롭게 보내세요.","행복한 하루 되시길!","좋은 저녁 되세요.","오늘은 영화 한 편 어떠세요?","편안한 주말 되세요.","오늘도 즐겁게!","따뜻한 차 한 잔 어때요?","행복한 하루 보내세요.","좋은 일만 가득하세요!","오늘도 즐거운 하루!","멋진 저녁 되세요.","오늘 하루도 무사히!","행복한 밤 되세요.","좋은 꿈 꾸세요.","활기찬 하루 되세요!","오늘도 웃으면서!","맛있는 디저트 즐기세요.","즐거운 주말 되세요.","좋은 아침 되세요!","오늘은 산책 어떠세요?","오늘도 수고 많으셨어요.","따뜻한 하루 보내세요.","편안한 저녁 보내세요.","오늘도 기분 좋은 하루!","즐거운 시간 보내세요.","좋은 사람들과 함께하세요.","오늘 하루도 행복하세요.","맛있는 음식 드세요.","행복한 아침 되세요.","오늘도 잘 보내세요.","기운 내세요!","좋은 하루 보내세요.","오늘은 책 한 권 어떠세요?","활기찬 저녁 되세요.","즐거운 저녁 보내세요.","오늘도 행복하세요.","멋진 하루 되시길!","좋은 시간 보내세요.","기분 좋은 아침 되세요.","오늘 하루도 힘내세요.","행복한 하루 보내세요.","좋은 하루 시작하세요!","오늘도 파이팅하세요.","따뜻한 커피 한 잔 어떠세요?","편안한 밤 보내세요.","행복한 시간 보내세요.","기분 좋은 하루 되세요.","오늘은 음악 한 곡 어떠세요?","즐거운 저녁 되세요.","좋은 하루 되세요.","오늘도 수고하셨어요.","멋진 아침 되세요.","행복한 하루 되시길!","오늘도 힘내세요!","좋은 밤 되세요.","기운찬 하루 보내세요.","오늘도 잘 지내세요.","행복한 저녁 되세요.","맛있는 저녁 드세요.","편안한 아침 되세요.","오늘도 화이팅하세요!","멋진 하루 보내세요.","행복한 시간 가지세요.","좋은 하루 되시길!","오늘 하루도 즐겁게!","편안한 주말 보내세요.","행복한 주말 되세요.","기분 좋은 저녁 되세요.","오늘도 수고하셨어요.","따뜻한 하루 되세요.","좋은 시간 되세요.","오늘도 활기차게!","행복한 아침 보내세요.","맛있는 간식 드세요.","즐거운 시간 가지세요.","편안한 하루 되세요.","기분 좋은 하루 보내세요.","오늘 하루도 잘 보내세요.","좋은 주말 되세요.","행복한 저녁 시간 되세요.","좋은 하루 되세요.","오늘도 좋은 하루!","편안한 밤 보내세요.","즐거운 하루 되세요.","행복한 하루 되세요."
]
    random_num = random.randint(0, len(messages) - 1)
    return messages[random_num]
