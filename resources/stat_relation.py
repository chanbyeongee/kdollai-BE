from flask_restful import Resource
from models.statistic import StatisticModel, init_emotion, init_relationship, emotion_weight
import copy
import operator
import json

def find_three_emotion(stats):
    ret_emotions = copy.deepcopy(init_emotion)
    total_cnt = 0

    for stat in stats:
        temp = json.loads(stat.emotions)
        total_cnt += stat.total

        for key in ret_emotions.keys():
            ret_emotions[key] += temp[key]



    return ret

def summary_relationship(stats):
    ret_relationship = {}
    real_ret={}

    for stat in stats:
        relationships = json.loads(stat.relation_ship)
        for key in relationships.keys():
            if not (key in ret_relationship.keys() ):
                ret_relationship[key]={}
                ret_relationship[key]["thumbnail"] = relationships[key]["thumbnail"]
                ret_relationship[key]["emotion"]=init_emotion.copy()

            for emotion_key in init_emotion.keys():
                ret_relationship[key]["emotion"][emotion_key] += relationships[key]["emotion"][emotion_key]

    for key in ret_relationship.keys():
        real_ret[key]={}
        real_ret[key]["thumbnail"] = ret_relationship[key]["thumbnail"]
        ret_relationship[key]["score"]=50
        for emotion_key in init_emotion.keys():
            ret_relationship[key]["score"] += ret_relationship[key]["emotion"][emotion_key] * emotion_weight[emotion_key]

        real_ret[key]["score"]=ret_relationship[key]["score"]

        sorted_x = sorted(ret_relationship[key]["emotion"].items(), key=operator.itemgetter(1), reverse=True)
        temp = [{"name":content[0],"count":content[1]} for content in sorted_x[:3]]
        real_ret[key]["emotion"]= temp

    return real_ret.copy()

class RelationNumberStatList(Resource):
    def get(self,date, number):

        child_id = 1

        stats = StatisticModel.find_by_number_with_child_id(child_id,date,number)

        if not stats :
            return {
                'isSummary':False,
                "statistics" : []
               }

        relationships = summary_relationship(stats)

        return {
                'isSummary':True,
                   'summary':{
                       'relationship':relationships
                    },
                    "statistics" : [stat.relation_json() for stat in stats]
               }, 200


class RelationRangeStatList(Resource):
    def get(self,end,begin):
        child_id = 1

        stats = StatisticModel.find_range_with_child_id(child_id, begin, end)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }
        relationships = summary_relationship(stats)


        return {
                   'isSummary': True,
                   'summary': {
                       'relationship': relationships
                   },
                   "statistics" : [stat.relation_json() for stat in stats]
               }, 200

class RelationYMDStatList(Resource):
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
                   "statistics" : [stat.relation_json()]
               }, 200

class RelationAllStatList(Resource):
    def get(self):
        child_id = 1

        stats = StatisticModel.find_by_child_id(child_id)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        relationships = summary_relationship(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       'relationship': relationships
                   },
                   "statistics" : [stat.relation_json() for stat in stats]
               }, 200