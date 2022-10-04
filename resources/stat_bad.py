from flask_restful import Resource
from models.statistic import StatisticModel, init_badwords, init_badsentences
import json
import copy

def summary_badness(stats):
    ret_badwords = init_badwords.copy()
    ret_badsentences = copy.deepcopy(init_badsentences)

    for stat in stats:
        badwords_temp = json.loads(stat.badwords).copy()
        badsentences_temp = json.loads(stat.bad_sentences).copy()

        for key in ret_badwords.keys():
            ret_badwords[key] += badwords_temp[key]

        for content in badsentences_temp["sentences"] :
            ret_badsentences["sentences"].append(content)

    return ret_badwords.copy(), ret_badsentences.copy()

class BadNumberStatList(Resource):
    def get(self,date, number):

        child_id = 1

        stats = StatisticModel.find_by_number_with_child_id(child_id,date,number)

        if not stats :
            return {
                'isSummary':False,
                "statistics" : []
               }

        badwords, badsentences = summary_badness(stats)

        return {
                'isSummary':True,
                   'summary':{
                       "badness":{
                            "bad_words":badwords,
                            "bad_sentences":badsentences
                       }
                    },
                    "statistics" : [stat.bad_json() for stat in stats]
               }, 200


class BadRangeStatList(Resource):
    def get(self,end,begin):
        child_id = 1

        stats = StatisticModel.find_range_with_child_id(child_id, begin, end)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        badwords, badsentences = summary_badness(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       "badness": {
                           "bad_words": badwords,
                           "bad_sentences": badsentences
                       }
                   },
                   "statistics" : [stat.bad_json() for stat in stats]
               }, 200

class BadYMDStatList(Resource):
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
                   "statistics" : [stat.bad_json()]
               }, 200

class BadAllStatList(Resource):
    def get(self):
        child_id = 1

        stats = StatisticModel.find_by_child_id(child_id)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        badwords, badsentences = summary_badness(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       "badness": {
                           "bad_words": badwords,
                           "bad_sentences": badsentences
                       }
                   },
                   "statistics" : [stat.bad_json() for stat in stats]
               }, 200