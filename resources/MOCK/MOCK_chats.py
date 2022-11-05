from models import ChatModel


def make_chats(child):

    #10.03일
    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175322",
        date_Time="오후 5:53",
        direction="USER",
        utterance="안녕 도담아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175330",
        date_Time="오후 5:53",
        direction="BOT",
        utterance="오랜만이야 동현아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175340",
        date_Time="오후 5:53",
        direction="USER",
        utterance="오늘 저번에 싸운 친구와 화해했어!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175350",
        date_Time="오후 5:53",
        direction="BOT",
        utterance="정말? 좋은 일이네! 축하해!"
    )
    chat.save_to_db()


    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175403",
        date_Time="오후 5:54",
        direction="USER",
        utterance="너 덕분이야! 고마워!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175415",
        date_Time="오후 5:54",
        direction="BOT",
        utterance="그렇게 말해줘서 내가 더 고마운걸?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175430",
        date_Time="오후 5:54",
        direction="USER",
        utterance="그건 그렇고 나는 부모님이랑 저녁 외식을 갈것같아"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175445",
        date_Time="오후 5:54",
        direction="BOT",
        utterance="부모님과 시간을 보내는구나? 좋은 시간 보냈으면 좋겠어"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175502",
        date_Time="오후 5:55",
        direction="USER",
        utterance="그럼 나 갔다올게"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175510",
        date_Time="오후 5:55",
        direction="BOT",
        utterance="일찍 오는거야?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175525",
        date_Time="오후 5:55",
        direction="USER",
        utterance="좀 있다 올것 같아.. 있다가 봐!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221103",
        date_YMDHMS="20221103175532",
        date_Time="오후 5:55",
        direction="BOT",
        utterance="그래! 이따 봐"
    )
    chat.save_to_db()


    #10.04
    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131158",
        date_Time="오후 1:11",
        direction="USER",
        utterance="씨발! 오늘 하루 완전 망했어"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131204",
        date_Time="오후 1:12",
        direction="BOT",
        utterance="무슨 일이야 동현아? 오늘 좀 화난 것 같아"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131204",
        date_Time="오후 1:12",
        direction="USER",
        utterance="학교에서 쪽지시험을 봤는데 너무 망쳤어"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131210",
        date_Time="오후 1:12",
        direction="BOT",
        utterance="그런 일이 있었구나... 혹시 더 자세히 말해줄 수 있어?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131222",
        date_Time="오후 1:12",
        direction="USER",
        utterance="수학 시험을 봤는데 2로 나눠야 할것을 곱해버렸어... 너무 화가나"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131235",
        date_Time="오후 1:12",
        direction="BOT",
        utterance="실수를 했구나.. 많이 중요한 시험이었니?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131248",
        date_Time="오후 1:12",
        direction="USER",
        utterance="아니, 많이 중요하지는 않았어.."
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131301",
        date_Time="오후 1:13",
        direction="BOT",
        utterance="그럼 다른 기회도 분명 많이 있을거야! 너무 걱정하지마! 혹시 부모님도 알고 계시니?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131315",
        date_Time="오후 1:13",
        direction="USER",
        utterance="아니 부모님은 알면 안돼.. 많이 혼내실 거야"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131327",
        date_Time="오후 1:13",
        direction="BOT",
        utterance="그래? 저번에도 비슷한 일이 있었니?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131339",
        date_Time="오후 1:13",
        direction="USER",
        utterance="그건 나중에 말해줄게..!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221104",
        date_YMDHMS="20221104131350",
        date_Time="오후 1:13",
        direction="BOT",
        utterance="그래! 나중에 편안할때 말해줘!"
    )
    chat.save_to_db()

    # 10.05일
    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175322",
        date_Time="오후 5:53",
        direction="USER",
        utterance="안녕 도담아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175330",
        date_Time="오후 5:53",
        direction="BOT",
        utterance="오랜만이야 동현아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175340",
        date_Time="오후 5:53",
        direction="USER",
        utterance="오늘 저번에 싸운 친구와 화해했어!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175350",
        date_Time="오후 5:53",
        direction="BOT",
        utterance="정말? 좋은 일이네! 축하해!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175403",
        date_Time="오후 5:54",
        direction="USER",
        utterance="너 덕분이야! 고마워!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175415",
        date_Time="오후 5:54",
        direction="BOT",
        utterance="그렇게 말해줘서 내가 더 고마운걸?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175430",
        date_Time="오후 5:54",
        direction="USER",
        utterance="그건 그렇고 나는 부모님이랑 저녁 외식을 갈것같아"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175445",
        date_Time="오후 5:54",
        direction="BOT",
        utterance="부모님과 시간을 보내는구나? 좋은 시간 보냈으면 좋겠어"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175502",
        date_Time="오후 5:55",
        direction="USER",
        utterance="그럼 나 갔다올게"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175510",
        date_Time="오후 5:55",
        direction="BOT",
        utterance="일찍 오는거야?"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175525",
        date_Time="오후 5:55",
        direction="USER",
        utterance="좀 있다 올것 같아.. 있다가 봐!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221105",
        date_YMDHMS="20221105175532",
        date_Time="오후 5:55",
        direction="BOT",
        utterance="그래! 이따 봐"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221106",
        date_YMDHMS="20221106105322",
        date_Time="오전 10:53",
        direction="USER",
        utterance="안녕 도담아!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221106",
        date_YMDHMS="20221106105330",
        date_Time="오전 10:53",
        direction="BOT",
        utterance="동현아 안녕!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221106",
        date_YMDHMS="20221106105340",
        date_Time="오전 10:53",
        direction="USER",
        utterance="오늘 친구가 생일 케이크를 사줬어"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221106",
        date_YMDHMS="20221106105350",
        date_Time="오전 10:53",
        direction="BOT",
        utterance="정말 오늘 생일 이구나?? 축하해!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221106",
        date_YMDHMS="20221106105403",
        date_Time="오전 10:54",
        direction="USER",
        utterance="고마워! 오늘 부모님이랑 점심 먹으로 갈 거 같아"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221106",
        date_YMDHMS="20221106105415",
        date_Time="오전 10:54",
        direction="BOT",
        utterance="그래 오늘 좋은 하루가 되길 바라!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221106",
        date_YMDHMS="20221106105430",
        date_Time="오전 10:54",
        direction="USER",
        utterance="응, 이따 보자!"
    )
    chat.save_to_db()

    chat = ChatModel(
        child_id=child.id,
        date_YMD="20221106",
        date_YMDHMS="20221106105532",
        date_Time="오전 10:55",
        direction="BOT",
        utterance="그래! 이따 봐"
    )
    chat.save_to_db()

