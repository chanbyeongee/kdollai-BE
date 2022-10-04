from flask_restful import Resource
from models.statistic import StatisticModel, init_emotion, init_relationship, emotion_weight

import json

def summary_relationship(stats):
    ret_relationship = init_relationship.copy()

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
        ret_relationship[key]["score"]=50
        for emotion_key in init_emotion.keys():
            ret_relationship[key]["score"] += ret_relationship[key]["emotion"][emotion_key] * emotion_weight[emotion_key]

    return ret_relationship.copy()


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