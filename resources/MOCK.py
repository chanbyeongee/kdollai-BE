from models import UserModel,ChatModel,StatisticModel,ChildModel,CounselorModel, IndexPageModel, ReservationModel
import json


def make_dummy():
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
        breif_desc="아동 심리상담 경력 5년의 전문 상담사",
        available_begin="0900",
        available_end="1800"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/1.jpg"
    counselor.save_to_db()

    make_reservation(user,counselor)
    make_chats(child)
    make_stats(child)

def make_reservation(user,counselor):
    page = IndexPageModel(
        main_desc=
        """국내 최초 기업 상담실과 연결된 상담센터
전국 상담실 네트워크 형성
최고의 전문성을 가진 센터
다양한 프로그램을 운영하는 종합상담센터
개인과 가족 그리고 사회가 행복하고 밝아지도록 노력하는 센터""",
        main_image="http://image.toast.com/aaaacho/pages/1.jpg",
        lunch_time="1200",
        address ="서울특별시 강남구 역삼동 717 한국은행 빌딩 7층 103호",
        post_address="테헤란로 202 (우) 06220",
        latitude="37.500519881040184",
        longitude="127.03794748482694",
        introduction=
        """서울 신학대 상담대학원 상담학 석사 졸업
미네소타 대학원 신학 박사 졸업
한국심리상담센터 대표
한국기업상담학회 이사
한국기업심리상담센터 원장
한국우울증연구소 소장
한국분노연구소 소장
현대자동차, 기아자동차 본사 상담사""",
        counselor_id=counselor.id
    )
    page.save_to_db()

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
    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220918",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["슬픔"] += 1
    stat.emotions = json.dumps(temp)
    stat.total +=1
    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20220919",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["기쁨"] += 1
    stat.emotions = json.dumps(temp)
    stat.total += 1
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

