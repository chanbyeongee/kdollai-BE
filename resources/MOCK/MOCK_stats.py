from models import StatisticModel
from models.statistic import emotion_weight, init_emotion
import json

def make_stats(child):

    stat = StatisticModel(
        date_YMD="20220930",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["중립"] += 2
    temp["기쁨"] += 3
    stat.emotion_score += emotion_weight["기쁨"]*3
    stat.emotions = json.dumps(temp)
    stat.total +=1

    temp = json.loads(stat.situation)
    temp["가족"]["total"] += 2
    temp["가족"]["emotion"]["중립"] += 1
    temp["가족"]["emotion"]["기쁨"] += 1
    temp["날씨/계절"]["total"] += 1
    temp["날씨/계절"]["emotion"]["기쁨"] += 1
    temp["건강"]["total"] += 2
    temp["건강"]["emotion"]["중립"] += 1
    temp["건강"]["emotion"]["기쁨"] += 1
    stat.situation = json.dumps(temp)

    temp = json.loads(stat.badwords)
    temp["개새끼"] += 1
    stat.badwords = json.dumps(temp)

    temp = json.loads(stat.bad_sentences)
    temp["sentences"].append("나한테 왜그러는거야 개새끼야")
    stat.bad_sentences = json.dumps(temp)

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221001",
        child_id=child.id
    )

    temp = json.loads(stat.emotions)
    temp["슬픔"] += 1
    temp["불만"] += 2
    temp["연민"] += 1
    stat.emotion_score += emotion_weight["슬픔"]
    stat.emotion_score += emotion_weight["불만"] * 2
    stat.emotion_score += emotion_weight["연민"]
    stat.emotions = json.dumps(temp)
    stat.total +=1

    temp = json.loads(stat.situation)
    temp["학교"]["total"] += 2
    temp["학교"]["emotion"]["슬픔"] += 1
    temp["학교"]["emotion"]["불만"] += 1
    temp["식음료"]["total"] += 2
    temp["식음료"]["emotion"]["슬픔"] += 1
    temp["식음료"]["emotion"]["불만"] += 1
    temp["게임"]["total"] += 2
    temp["게임"]["emotion"]["슬픔"] += 1
    temp["게임"]["emotion"]["불만"] += 1
    temp["반려동물"]["total"] += 1
    temp["반려동물"]["emotion"]["연민"] += 1
    stat.situation = json.dumps(temp)

    temp = json.loads(stat.relation_ship)
    temp["친구"]={}
    temp["친구"]["thumbnail"] = "http://image.toast.com/aaaacho/childs/id_1/relations/%EC%B9%9C%EA%B5%AC.png"
    temp["친구"]["emotion"] = init_emotion.copy()
    temp["친구"]["emotion"]["연민"] += 1

    temp["강아지"] = {}
    temp["강아지"]["thumbnail"]="http://image.toast.com/aaaacho/childs/id_1/relations/%EA%B0%95%EC%95%84%EC%A7%80.png"
    temp["강아지"]["emotion"] = init_emotion.copy()
    temp["강아지"]["emotion"]["연민"] += 1

    stat.relation_ship = json.dumps(temp)


    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221002",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["기쁨"] += 1
    temp["당혹"] += 2
    temp["걱정"] += 3
    temp["질투"] += 1
    stat.emotion_score += emotion_weight["기쁨"]
    stat.emotion_score += emotion_weight["당혹"]*2
    stat.emotion_score += emotion_weight["걱정"]*3
    stat.emotion_score += emotion_weight["질투"]
    stat.emotions = json.dumps(temp)
    stat.total += 1

    temp = json.loads(stat.situation)
    temp["학교"]["total"] += 3
    temp["학교"]["emotion"]["당혹"]+=2
    temp["학교"]["emotion"]["걱정"] += 1
    temp["여행"]["total"] += 3
    temp["여행"]["emotion"]["당혹"] += 2
    temp["여행"]["emotion"]["걱정"] += 1
    temp["방송/연예"]["total"] += 3
    temp["방송/연예"]["emotion"]["당혹"] += 2
    temp["방송/연예"]["emotion"]["걱정"] += 1
    stat.situation = json.dumps(temp)

    temp = json.loads(stat.relation_ship)
    temp["미영"] = {}
    temp["미영"]["thumbnail"] = "http://image.toast.com/aaaacho/childs/id_1/relations/%EB%AF%B8%EC%98%81%EC%9D%B4.png"
    temp["미영"]["emotion"] = init_emotion.copy()
    temp["미영"]["emotion"]["걱정"] += 2

    temp["반장"] = {}
    temp["반장"]["thumbnail"] = "http://image.toast.com/aaaacho/childs/id_1/relations/%EB%B0%98%EC%9E%A5.png"
    temp["반장"]["emotion"] = init_emotion.copy()
    temp["반장"]["emotion"]["질투"] += 1
    stat.relation_ship = json.dumps(temp)

    temp = json.loads(stat.badwords)
    temp["자살"] += 1
    stat.badwords = json.dumps(temp)

    temp = json.loads(stat.bad_sentences)
    temp["sentences"].append("그냥 자살하고 싶었어...")
    stat.bad_sentences = json.dumps(temp)

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221003",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["죄책감"] += 1
    temp["기쁨"] += 2
    temp["중립"] += 3
    temp["걱정"] += 1
    stat.emotion_score += emotion_weight["죄책감"]
    stat.emotion_score += emotion_weight["기쁨"]
    stat.emotion_score += emotion_weight["걱정"]
    stat.emotions = json.dumps(temp)
    stat.total += 1

    temp = json.loads(stat.situation)
    temp["건강"]["total"] += 1
    temp["건강"]["emotion"]["불만"]+=1
    temp["학교"]["total"] += 2
    temp["학교"]["emotion"]["불만"] += 1
    temp["학교"]["emotion"]["걱정"] += 1
    temp["식음료"]["total"] += 2
    temp["식음료"]["emotion"]["죄책감"] += 1
    temp["식음료"]["emotion"]["중립"] += 1
    temp["영화/만화"]["total"] += 1
    temp["영화/만화"]["emotion"]["기쁨"] += 1
    temp["여행"]["total"] += 1
    temp["여행"]["emotion"]["기쁨"] += 1
    temp["스포츠"]["total"] += 1
    temp["스포츠"]["emotion"]["기쁨"] += 1
    stat.situation = json.dumps(temp)

    temp = json.loads(stat.badwords)
    temp["존나"] += 1
    stat.badwords = json.dumps(temp)

    temp = json.loads(stat.bad_sentences)
    temp["sentences"].append("존나 짜증나...")
    stat.bad_sentences = json.dumps(temp)

    stat.save_to_db()

    stat = StatisticModel(
        date_YMD="20221004",
        child_id=child.id
    )
    temp = json.loads(stat.emotions)
    temp["슬픔"] += 3
    temp["중립"] += 2
    temp["불만"] += 4
    temp["당혹"] += 1
    stat.emotion_score += emotion_weight["슬픔"]*3
    stat.emotion_score += emotion_weight["불만"] * 4
    stat.emotion_score += emotion_weight["당혹"]
    stat.emotions = json.dumps(temp)
    stat.total += 1

    temp = json.loads(stat.situation)
    temp["학교"]["total"] += 2
    temp["학교"]["emotion"]["불만"]+=2
    temp["가족"]["total"] += 1
    temp["가족"]["emotion"]["슬픔"] += 1
    temp["방송/연예"]["total"] += 2
    temp["방송/연예"]["emotion"]["중립"] += 2
    temp["영화/만화"]["total"] += 1
    temp["영화/만화"]["emotion"]["중립"] += 1
    stat.situation = json.dumps(temp)

    temp = json.loads(stat.relation_ship)
    temp["엄마"]={}
    temp["엄마"]["thumbnail"] = "http://image.toast.com/aaaacho/childs/id_1/relations/%EC%97%84%EB%A7%88.png"
    temp["엄마"]["emotion"] = init_emotion.copy()
    temp["엄마"]["emotion"]["슬픔"] += 2
    temp["아빠"] = {}
    temp["아빠"]["thumbnail"] = "http://image.toast.com/aaaacho/childs/id_1/relations/%EC%95%84%EB%B9%A0.png"
    temp["아빠"]["emotion"] = init_emotion.copy()
    temp["아빠"]["emotion"]["슬픔"] += 2
    stat.relation_ship = json.dumps(temp)

    temp = json.loads(stat.badwords)
    temp["씨발"] += 1
    stat.badwords = json.dumps(temp)

    temp = json.loads(stat.bad_sentences)
    temp["sentences"].append("씨발! 오늘 시험 망쳤어!")
    stat.bad_sentences = json.dumps(temp)


    stat.save_to_db()
