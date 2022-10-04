from flask_restful import Resource
from models.statistic import StatisticModel, init_emotion, init_topic, emotion_weight
import json
import copy

def summary_situation(stats):
    ret_topics = copy.deepcopy(init_topic)

    for stat in stats:
        topic_temp = json.loads(stat.situation)

        for key in ret_topics.keys():
            ret_topics[key]["total"] += topic_temp[key]["total"]

            for emo_key in init_emotion.keys():
                ret_topics[key]["emotion"][emo_key] += topic_temp[key]["emotion"][emo_key]

    for key in ret_topics.keys():
        temp_sum=50
        for emo_key in init_emotion.keys():
            temp_sum += ret_topics[key]["emotion"][emo_key]*emotion_weight[emo_key]
        ret_topics[key]["score"]=temp_sum

    return ret_topics.copy()

class TopicNumberStatList(Resource):
    def get(self,date, number):

        child_id = 1

        stats = StatisticModel.find_by_number_with_child_id(child_id,date,number)

        if not stats :
            return {
                'isSummary':False,
                "statistics" : []
               }

        topics = summary_situation(stats)

        return {
                'isSummary':True,
                   'summary':{
                       'situation':{
                           'topic':topics
                       }
                    },
                    "statistics" : [stat.topic_json() for stat in stats]
               }, 200


class TopicRangeStatList(Resource):
    def get(self,end,begin):
        child_id = 1

        stats = StatisticModel.find_range_with_child_id(child_id, begin, end)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        topics = summary_situation(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       'situation': {
                           'topic': topics
                       }
                   },
                   "statistics" : [stat.topic_json() for stat in stats]
               }, 200

class TopicYMDStatList(Resource):
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
                   "statistics" : [stat.topic_json()]
               }, 200

class TopicAllStatList(Resource):
    def get(self):
        child_id = 1

        stats = StatisticModel.find_by_child_id(child_id)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        topics = summary_situation(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       'situation': {
                           'topic': topics
                       }
                   },
                   "statistics" : [stat.topic_json() for stat in stats]
               }, 200