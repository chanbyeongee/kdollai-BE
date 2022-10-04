from models import UserModel,ChildModel,CounselorModel, ReservationModel

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



def make_account():

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
        available_begin="09:00",
        available_end="18:00"
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
        available_begin="09:00",
        available_end="18:00"
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
        available_begin="09:00",
        available_end="18:00"
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
        available_begin="11:00",
        available_end="18:00"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/4.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="counsel01@naver.com",
        user_subname="이고은",
        password="123123",
        breif_desc="수원 키즈 전문 상담 카페",
        available_begin="09:00",
        available_end="20:00"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/5.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="heart44@gmail.com",
        user_subname="김찬정",
        password="123123",
        breif_desc="인천 헬로스마일 상담 센터",
        available_begin="11:00",
        available_end="20:00"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/6.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="12kidheart@gmail.com",
        user_subname="노지선",
        password="123123",
        breif_desc="우리동네 아이 상담소",
        available_begin="10:00",
        available_end="18:00"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/7.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="light1@gmail.com",
        user_subname="장지윤",
        password="123123",
        breif_desc="한빛 마음 테라피",
        available_begin="09:00",
        available_end="23:00"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/8.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    counselor = CounselorModel(
        user_name="cymi92@gmail.com",
        user_subname="차유미",
        password="123123",
        breif_desc="차유미 상담 센터",
        available_begin="07:00",
        available_end="18:00"
    )
    counselor.profile = "http://image.toast.com/aaaacho/counselors/9.jpg"
    counselor.save_to_db()

    counselors.append(counselor)

    return counselors, child