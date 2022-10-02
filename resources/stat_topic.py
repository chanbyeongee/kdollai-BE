from flask_restful import Resource, reqparse
from models.chat import ChatModel
from models.child import ChildModel
from models.statistic import StatisticModel, init_emotion, init_topic, init_subtopic, init_badwords, init_badsentences, init_relationship, emotion_weight
from datetime import datetime,timedelta
import json

def summary_situation(stats):
    ret_topics = init_topic.copy()
    ret_subtopics = init_subtopic.copy()

    for stat in stats:
        topic_temp = json.loads(stat.situation)
        sub_temp = json.loads(stat.subtopic)
        for key in ret_topics.keys():
            ret_topics[key]["total"] += topic_temp[key]["total"]

            for emo_key in init_emotion.keys():
                ret_topics[key]["emotion"][emo_key] += topic_temp[key]["emotion"][emo_key]

        for key in ret_subtopics.keys():
            ret_subtopics[key]["total"] += sub_temp[key]["total"]

            for emo_key in init_emotion.keys():
                ret_subtopics[key]["emotion"][emo_key] += sub_temp[key]["emotion"][emo_key]

    for key in ret_topics.keys():
        temp_sum=50
        for emo_key in init_emotion.keys():
            temp_sum += ret_topics[key]["emotion"][emo_key]*emotion_weight[emo_key]
        ret_topics[key]["score"]=temp_sum

    for key in ret_subtopics.keys():
        temp_sum=50
        for emo_key in init_emotion.keys():
            temp_sum += ret_subtopics[key]["emotion"][emo_key]*emotion_weight[emo_key]
        ret_subtopics[key]["score"]=temp_sum

    return ret_topics.copy(), ret_subtopics.copy()

class TopicNumberStatList(Resource):
    def get(self,date, number):

        child_id = 1

        end = datetime.strptime(date, '%Y%m%d')
        begin = (end - timedelta(number-1)).strftime("%Y%m%d")

        stats = StatisticModel.find_range_with_child_id(child_id, begin, date)

        if not stats :
            return {
                'isSummary':False,
                "statistics" : []
               }

        topics, sub_topic = summary_situation(stats)

        return {
                'isSummary':True,
                   'summary':{
                       'situation':{
                           'topic':topics,
                           'subtopic':sub_topic
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


        topics, sub_topic = summary_situation(stats)



        return {
                   'isSummary': True,
                   'summary': {
                       'situation': {
                           'topic': topics,
                           'subtopic': sub_topic
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


        topics, sub_topic = summary_situation(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       'situation': {
                           'topic': topics,
                           'subtopic': sub_topic
                       }
                   },
                   "statistics" : [stat.topic_json() for stat in stats]
               }, 200