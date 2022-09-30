from models import UserModel,ChatModel,StatisticModel,ChildModel,CounselorModel, IndexPageModel, ReservationModel
from models.statistic import emotion_weight, init_emotion
import json


def make_dummy():

    counselors=[]
    user = UserModel(
        user_name="well87865@gmail.com",
        user_subname="Chanee",
        password="123123",
    )
    user.user_profile = "http://image.toast.com/aaaacho/users/1.jpg"
    user.save_to_db()

    child = ChildModel(
        child_name="이동현",
        child_age=23,
        child_gender="male",
        user_id=user.id,
        serial_number="abcd1234"
    )
    child.profile = "http://image.toast.com/aaaacho/childs/1.jpg"
    child.save_to_db()

    counselor = CounselorModel(
        user_name="abcd123@gmail.com",
        user_subname="이경용",
        password="123123",
        breif_desc="서울 한마음 상담 센터",
        available_begin="0900",
        available_end="1800"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/1.jpg"
    counselor.save_to_db()

    counselors.append(counselor)
    make_reservation(user, counselor)

    counselor = CounselorModel(
        user_name="1q2w3e4r@gmail.com",
        user_subname="김형석",
        password="123123",
        breif_desc="분당 친구 상담 센터",
        available_begin="0900",
        available_end="1800"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/2.jpg"
    counselor.save_to_db()

    counselors.append(counselor)
    make_reservation(user, counselor)

    counselor = CounselorModel(
        user_name="zxcv1234@naver.com",
        user_subname="최은진",
        password="123123",
        breif_desc="구름 나라 정신 병원",
        available_begin="0900",
        available_end="1800"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/3.jpg"
    counselor.save_to_db()

    counselors.append(counselor)
    make_reservation(user, counselor)

    counselor = CounselorModel(
        user_name="power9999@hanmail.net",
        user_subname="정경미",
        password="123123",
        breif_desc="해바라기 테라피 의원",
        available_begin="1100",
        available_end="1800"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/4.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="counsel01@naver.com",
        user_subname="이고은",
        password="123123",
        breif_desc="수원 키즈 전문 상담 카페",
        available_begin="0900",
        available_end="2000"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/5.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="heart44@gmail.com",
        user_subname="김찬정",
        password="123123",
        breif_desc="인천 헬로스마일 상담 센터",
        available_begin="1100",
        available_end="2000"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/6.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="12kidheart@gmail.com",
        user_subname="노지선",
        password="123123",
        breif_desc="우리동네 아이 상담소",
        available_begin="1000",
        available_end="1800"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/7.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="light1@gmail.com",
        user_subname="장지윤",
        password="123123",
        breif_desc="한빛 마음 테라피",
        available_begin="0900",
        available_end="2300"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/8.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="cymi92@gmail.com",
        user_subname="차유미",
        password="123123",
        breif_desc="차유미 상담 센터",
        available_begin="0700",
        available_end="1800"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/9.jpg"
    counselor.save_to_db()

    counselors.append(counselor)
    make_page(counselors)

    make_chats(child)
    make_stats(child)

def make_page(counselors):
    counselor = counselors[0]
    page = IndexPageModel(
        main_desc=
        """국내 최초 기업 상담실과 연결된 상담센터
전국 상담실 네트워크 형성
최고의 전문성을 가진 센터
다양한 프로그램을 운영하는 종합상담센터
개인과 가족 그리고 사회가 행복하고 밝아지도록 노력하는 센터""",
        main_image="http://image.toast.com/aaaacho/pages/1.jpg",
        lunch_time="1200",
        address="서울특별시 강남구 역삼동 717 한국은행 빌딩 7층 103호",
        post_address="테헤란로 202 (우) 06220",
        latitude="37.500519881040184",
        longitude="127.03794748482694",
        introduction=
        """서울 신학대 상담대학원 상담학 석사 졸업
미네소타 대학원 신학 박사 졸업
한국심리상담센터 대표
한국기업상담학회 이사
""",
        counselor_id=counselor.id
    )
    page.save_to_db()

    counselor = counselors[1]
    page = IndexPageModel(
        main_desc=
        """맞벌이 가족 육아 전용 상담 센터
        지하철 3분거리에 위치하여 높은 편의성 제공
        미국 보스턴 대학 심리상담 박사 학위 보유
        24시간 전화 상담 가능
        """,
        main_image="http://image.toast.com/aaaacho/pages/2.jpg",
        lunch_time="1230",
        address="경기도 성남시 중원구 성남동 3453 2층 203호",
        post_address="성남대로1148번길 8",
        latitude="37.43240510000002",
        longitude="127.13006870000014",
        introduction=
        """미국 보스턴 대학 심리상담학 석/박사
고려대학교 상담복지학과 학사
2020 올해의 상담사 100인 선정
삼성, 현대 등 주요 임직원 전문 상담사
""",
        counselor_id=counselor.id
    )
    page.save_to_db()

    counselor = counselors[2]
    page = IndexPageModel(
        main_desc=
        """정신과 전문 면허 자격 취득
        15년 이상의 경력의 의사들과 함께 고민을 나눠봐요.
        육와 관련 상담도 환영합니다! 현재 특가 이벤트 진행중!
        직접 방문시 등촌역 3번출구로 나오셔서 왼쪽으로 쭉 오세요!
        """,
        main_image="http://image.toast.com/aaaacho/pages/3.jpg",
        lunch_time="1200",
        address="서울 강서구 염창동 272-8 3층 315호",
        post_address="공항대로65길 1-5",
        latitude="37.550396799999824",
        longitude="126.86700719999935",
        introduction=
        """서울대병원 정신과 학사
        한국 정신과 협회 정회원
        우울 치료 방법 관련 특허 3개 보유
        정부 지정 공식 자살 방지 상담사
        """,
        counselor_id=counselor.id
    )
    page.save_to_db()

    counselor = counselors[3]
    page = IndexPageModel(
        main_desc=
        """###무료 심리상담 이벤트 진행중###
         미취학 아동 50% 할인!!
         단체 상담 환영, 학생 상담 전문
         국내 유일 24시간 콜 서비스 제공 
         """,
        main_image="http://image.toast.com/aaaacho/pages/4.jpg",
        lunch_time="1300",
        address="서울특별시 송파구 문정동 11-13 2층",
        post_address="송이로32길 6 (우) 05796",
        latitude="37.48947490000017",
        longitude="127.12804969999932",
        introduction=
        """경희대학교 의과대학 졸업
경희대학교 의과대학 석사
경희대학교병원 정신건강의학과 전공의 수료
대학신경정신의학회 정회원
""",
        counselor_id=counselor.id
    )
    page.save_to_db()

    counselor = counselors[4]
    page = IndexPageModel(
        main_desc=
        """국내 최고 수준의 정신건강 멤버들이 함께 합니다.
        정신건강의학과 전문의, 전문 임상심리사, 1급 상담심리사와 협업
        보건복지부 상담 교육 과정 수료
        한국상담심리학회의 공인을 받은 상담사만으로 구성되어 있습니다.
        """,
        main_image="http://image.toast.com/aaaacho/pages/5.jpg",
        lunch_time="1230",
        address="경기도 성남시 수정구 창곡동 551-11 3층 안내데스크",
        post_address="위례서일로3길 3-8 (우) 13647",
        latitude="37.46582849999996",
        longitude="127.13786129999963",
        introduction=
        """한국상담심리학회 상담심리전문가 1급
        한국상담심리학회 주수퍼바이저
        보건복지부 청소년상담사2급
        건국대학교 학생생활상담센터 상담사
        김포청소년육성재단 청소년상담사
        """,
        counselor_id=counselor.id
    )
    page.save_to_db()

    counselor = counselors[5]
    page = IndexPageModel(
        main_desc=
        """온가족을 위한 심리치료, 종합전문상담기관
        심리학 석사 이상의 전문가들이 항상 상주
        정직한 검사 진행, 정품 겅사도구
        연중무휴 야간 심리상담 진행
        """,
        main_image="http://image.toast.com/aaaacho/pages/6.jpg",
        lunch_time="1210",
        address="서울특별시 노원구 상계동 725 6층",
        post_address="동일로218길 25 (우) 01751",
        latitude="37.6539928000002",
        longitude="127.06200449999967",
        introduction=
        """서울대학교 심리학과 학사
        고려대학교 임상 및 상담심리학과 석사
        성북아이클리닉 임상심리 전문가
        삼성에스원 전문상담사
        마포 아동보호 전문기관 임상심리 전문가
        """,
        counselor_id=counselor.id
    )
    page.save_to_db()

    counselor = counselors[6]
    page = IndexPageModel(
        main_desc=
        """매일 5시마음을 들어주는 유투브 라이브 방송 진행
        화제의 유아맘 공감,위로 CF 500만뷰
        무료 자가진단 테스트 이벤트 중
        연령별 다양한 혜택 및 상담 제공 중
        """,
        main_image="http://image.toast.com/aaaacho/pages/7.jpg",
        lunch_time="1200",
        address="서울특별시 용산구 갈월동 69-27 202호",
        post_address="한강대로 305 (우) 04320",
        latitude="37.54556499999999",
        longitude="126.9713239999995",
        introduction=
        """미국 플로리다 주립대학 발달심리 박사
        미국 Indiana University 상담/상담교육 석사
        성북 허그맘허그인 심리상담센터 수석상담사
        미국 페니실바니아 주립대학 심리학과 전임강사
        """,
        counselor_id=counselor.id
    )
    page.save_to_db()

    counselor = counselors[7]
    page = IndexPageModel(
        main_desc=
        """각종 놀이치료 제공 및 1:1 육아 컨설팅 진행
        의료기록이 남지 않으며, 약물 치료에 의존하지 않습니다.
        최고의 상담시설, 조용하고 쾌적한 시설 속에서 상담을 진행해보세요!
        인천광역시 아동복지 협회와 협력 중입니다.
        """,
        main_image="http://image.toast.com/aaaacho/pages/8.jpg",
        lunch_time="1200",
        address="인천광역시 미추홀구 학익동 691-1 415호",
        post_address="한나루로 358 (우) 22225",
        latitude="37.43998689999977",
        longitude="126.66208559999974",
        introduction=
        """연세대학교 상담코칭학 박사
        연세대학교 상담코칭지원센터 수퍼바이저
        서울시 재난심리회복지원센터 상담활동가
        한국가족문화상담협회 공인 EAP 전문가 1급
        """,
        counselor_id=counselor.id
    )
    page.save_to_db()

    counselor = counselors[8]
    page = IndexPageModel(
        main_desc=
        """심리적, 정서적으로 어려움을 겪고 있는 분들을 위한 종합심리상담센터
        심리치료사, 가족상담사, 놀이치료사, 발달 치료사 등 각 분야 전문가 상담사님들이 계십니다.
        다양한 상담치료 프로그램을 마련하여 건강한 정신을 돕기 위해 노력합니다.
        치료가 끝나도 체계적인 사후 관리를 통해 재발을 방지합니다.
        """,
        main_image="http://image.toast.com/aaaacho/pages/9.jpg",
        lunch_time="1300",
        address="서울특별시 동대문구 이문동 324-21 301호",
        post_address="이문로 81 (우) 02451",
        latitude="37.594424699999585",
        longitude="127.05839119999952",
        introduction=
        """한양대학교 교육학과 박사 수료
        한국상담심리학회 공인 상담심리사 1급
        서울시 청년 마음건강 심층상담 전문 위촉상담사
        한국융연구원 예비과정 상임연구원
        서울시청 힐링센터 쉼표 심리상담사
        """,
        counselor_id=counselor.id
    )
    page.save_to_db()

def make_reservation(user,counselor):


    reservation = ReservationModel(
        day="20220920",
        begin="1000",
        end="1400",
        content="""
        안녕하세요, 저희아이가 언제부터인가 컴퓨터에 중독이 되서 코딩만 하는 기계가 되었어요...
        벌써부터 이러면 눈도 나빠지고 건강도 안좋아질 것 같아서 걱정이에요...
        상담사 선생님의 도움이 필요해요...
        """,
        user_id=user.id,
        counselor_id=counselor.id
    )
    reservation.save_to_db()


def make_stats(child):

    make_chats(child)
    stat = StatisticModel(
        date_YMD="20220917",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["중립"]+=1
    stat.emotions = json.dumps(temp)
    stat.total +=1

    temp = json.loads(stat.situation)
    temp["가족"] += 1
    stat.situation = json.dumps(temp)


    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220918",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["슬픔"] += 1
    stat.emotion_score += emotion_weight["슬픔"]
    stat.emotions = json.dumps(temp)
    stat.total +=1

    temp = json.loads(stat.situation)
    temp["학교"] += 1
    stat.situation = json.dumps(temp)

    temp = json.loads(stat.relation_ship)
    temp["친구"] = init_emotion.copy()
    temp["친구"]["슬픔"] += 1
    stat.relation_ship = json.dumps(temp)

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220919",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["기쁨"] += 1
    stat.emotion_score += emotion_weight["기쁨"]
    stat.emotions = json.dumps(temp)
    stat.total += 1

    temp = json.loads(stat.situation)
    temp["학교"] += 1
    stat.situation = json.dumps(temp)


    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220920",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["불만"] += 1
    stat.emotion_score += emotion_weight["불만"]
    stat.emotions = json.dumps(temp)
    stat.total += 1

    temp = json.loads(stat.situation)
    temp["건강"] += 1
    stat.situation = json.dumps(temp)

    temp = json.loads(stat.badwords)
    temp["씨발"] += 1
    stat.badwords = json.dumps(temp)
    temp = json.loads(stat.bad_sentences)
    temp["sentences"].append("씨발! 나 죽고싶어!")
    stat.bad_sentences = json.dumps(temp)

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220922",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["슬픔"] += 1
    stat.emotion_score += emotion_weight["슬픔"]
    stat.emotions = json.dumps(temp)
    stat.total += 1

    temp = json.loads(stat.situation)
    temp["가족"] += 1
    stat.situation = json.dumps(temp)

    temp = json.loads(stat.relation_ship)
    temp["엄마"] = init_emotion.copy()
    temp["엄마"]["슬픔"] += 1
    temp["아빠"] = init_emotion.copy()
    temp["아빠"]["슬픔"] += 1
    stat.relation_ship = json.dumps(temp)

    stat.save_to_db()

def make_chats(child):
    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220917",
        date_YMDHMS="20220917175322",
        date_Time="오후 5:53",
        direction="USER",
        utterance="안녕 도담아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220917",
        date_YMDHMS="20220917175326",
        date_Time="오후 5:53",
        direction="BOT",
        utterance="오랜만이야 동현아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220918",
        date_YMDHMS="20220918190022",
        date_Time="오후 7:00",
        direction="USER",
        utterance="학교에서 친구랑 싸웠어..."
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220918",
        date_YMDHMS="20220918190027",
        date_Time="오후 7:00",
        direction="BOT",
        utterance="정말? 많이 슬펐겠다..."
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220919",
        date_YMDHMS="20220919080140",
        date_Time="오전 8:01",
        direction="USER",
        utterance="이따 학교 끝나고 보자!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220919",
        date_YMDHMS="20220919080145",
        date_Time="오전 8:01",
        direction="BOT",
        utterance="그래! 이따 보자!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220920",
        date_YMDHMS="20220920123021",
        date_Time="오후 12:30",
        direction="USER",
        utterance="씨발! 나 죽고싶어!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220920",
        date_YMDHMS="20220920123024",
        date_Time="오후 12:30",
        direction="BOT",
        utterance="무슨 일 있어?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220922",
        date_YMDHMS="20220922210315",
        date_Time="오후 9:03",
        direction="USER",
        utterance="엄마 아빠가 너무 미워..."
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20220922",
        date_YMDHMS="20220922210318",
        date_Time="오후 9:03",
        direction="BOT",
        utterance="혹시 자세히 말해줄 수 있어??"
    )
    chat.save_to_db()

