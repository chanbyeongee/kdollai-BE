from models import IndexPageModel




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
        lunch_time="12:00",
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
        lunch_time="12:30",
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
        lunch_time="12:00",
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
        lunch_time="13:00",
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
        lunch_time="12:30",
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
        lunch_time="12:10",
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
        lunch_time="12:00",
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
        lunch_time="12:00",
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
        lunch_time="13:00",
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