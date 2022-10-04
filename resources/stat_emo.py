from flask_restful import Resource
from models.statistic import StatisticModel, init_emotion
import json

def summary_emotion(stats):
    ret_emotions = init_emotion.copy()
    ret_score = 0
    total_cnt = 0

    for stat in stats:
        temp = json.loads(stat.emotions)
        total_cnt += stat.total
        ret_score += stat.emotion_score
        for key in ret_emotions.keys():
            ret_emotions[key] += temp[key]


    ret_score /= len(stats)

    if ret_score < 0:
        ret_score = 0

    elif ret_score > 100:
        ret_score = 100

    return total_cnt, ret_emotions.copy(), ret_score


class EmotionNumberStatList(Resource):
    def get(self,date, number):

        child_id = 1

        stats = StatisticModel.find_by_number_with_child_id(child_id,date,number)

        if not stats :
            return {
                'isSummary':False,
                "statistics" : []
               }

        total_cnt, ret_emotions, ret_score= summary_emotion(stats)

        return {
                'isSummary':True,
                   'summary':{
                       "emotion":{
                        "total":total_cnt,
                        'emotions': ret_emotions,
                        'emotion_score': ret_score,
                       }
                    },
                    "statistics" : [stat.emo_json() for stat in stats]
               }, 200


class EmotionRangeStatList(Resource):
    def get(self,end,begin):
        child_id = 1

        stats = StatisticModel.find_range_with_child_id(child_id, begin, end)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        total_cnt, ret_emotions, ret_score = summary_emotion(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       "emotion": {
                           "total": total_cnt,
                           'emotions': ret_emotions,
                           'emotion_score': ret_score,
                       }
                   },
                   "statistics" : [stat.emo_json() for stat in stats]
               }, 200

class EmotionYMDStatList(Resource):
    def get(self,day):
        child_id = 1

        stat = StatisticModel.find_by_dateYMD_with_child_id(child_id,day)

        if not stat :
            return {
                'isSummary': False,
                "statistics": []
            }

        return {
                   'isSummary': False,
                   "statistics" : [stat.emo_json()]
               }, 200

class EmotionAllStatList(Resource):
    def get(self):
        child_id = 1

        stats = StatisticModel.find_by_child_id(child_id)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        total_cnt, ret_emotions, ret_score = summary_emotion(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       "emotion": {
                           "total": total_cnt,
                           'emotions': ret_emotions,
                           'emotion_score': ret_score,
                       }
                   },
                   "statistics": [stat.emo_json() for stat in stats]
               }, 200