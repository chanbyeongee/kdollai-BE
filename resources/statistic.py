from flask_restful import Resource, reqparse
from models.chat import ChatModel
from models.child import ChildModel
from models.statistic import StatisticModel, init_emotion
from datetime import datetime,timedelta
import json

class NumberStatList(Resource):
    def get(self,date, number):

        child_id = 1
        total_cnt=0

        end = datetime.strptime(date, '%Y%m%d')
        begin = (end - timedelta(number-1)).strftime("%Y%m%d")

        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_range_with_child_id(child_id, begin, date)

        if not stats :
            return {
                'isSummary':False,
                "statistics" : []
               }

        for stat in stats:
            temp = json.loads(stat.emotions)
            total_cnt += stat.total
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]


        return {
                'isSummary':True,
                   'summary':{
                        "total":total_cnt,
                        'emotions': ret_emotions
                    },
                    "statistics" : [stat.json() for stat in stats]
               }, 200


class RangeStatList(Resource):
    def get(self,end,begin):
        child_id = 1
        total_cnt = 0

        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_range_with_child_id(child_id, begin, end)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        for stat in stats:
            temp = json.loads(stat.emotions)
            total_cnt += stat.total
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]

        return {
                   'isSummary': True,
                   'summary': {
                       "total": total_cnt,
                       'emotions': ret_emotions
                   },
                   "statistics": [stat.json() for stat in stats]
               }, 200

class YMDStatList(Resource):
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
                   "statistics" : [stat.json()]
               }, 200

class AllStatList(Resource):
    def get(self):
        child_id = 1

        total_cnt = 0
        ret_emotions = init_emotion.copy()
        stats = StatisticModel.find_by_child_id(child_id)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        for stat in stats:
            temp = json.loads(stat.emotions)
            total_cnt += stat.total
            for key in ret_emotions.keys():
                ret_emotions[key] += temp[key]

        return {
                   'isSummary': True,
                   'summary': {
                       "total": total_cnt,
                       'emotions': ret_emotions
                   },
                   "statistics": [stat.json() for stat in stats]
               }, 200