from flask_restful import Resource, reqparse
from models.chat import ChatModel
from models.child import ChildModel
from models.statistic import StatisticModel, init_emotion, init_topic, init_subtopic, init_badwords, init_badsentences, init_relationship, emotion_weight
from datetime import datetime,timedelta
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

def summary_situation(stats):
    ret_topics = init_topic.copy()
    ret_subtopics = init_subtopic.copy()

    for stat in stats:
        topic_temp = json.loads(stat.situation)
        sub_temp = json.loads(stat.subtopic)
        for key in ret_topics.keys():
            ret_topics[key] += topic_temp[key]

        for key in ret_subtopics.keys():
            ret_subtopics[key] += sub_temp[key]


    return ret_topics.copy(), ret_subtopics.copy()

def summary_badness(stats):
    ret_badwords = init_badwords.copy()
    ret_badsentences = init_badsentences.copy()

    for stat in stats:
        badwords_temp = json.loads(stat.badwords)
        badsentences_temp = json.loads(stat.bad_sentences)

        for key in ret_badwords.keys():
            ret_badwords[key] += badwords_temp[key]

        for content in badsentences_temp["sentences"] :
            ret_badsentences["sentences"].append(content)

    return ret_badwords.copy(), ret_badsentences.copy()


def summary_relationship(stats):
    ret_relationship = init_relationship.copy()
    real_relationship = {}
    for stat in stats:
        relationships = json.loads(stat.relation_ship)
        for key in relationships.keys():
            if not (key in ret_relationship.keys() ):
                ret_relationship[key]=init_emotion.copy()

            for emotion_key in ret_relationship[key].keys():
                ret_relationship[key][emotion_key] += relationships[key][emotion_key]


    for key in ret_relationship.keys():
        real_relationship[key] = 50
        for emotion_key in init_emotion.keys():

            real_relationship[key] += ret_relationship[key][emotion_key] * emotion_weight[emotion_key]

    return real_relationship.copy()

class NumberStatList(Resource):
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

        total_cnt, ret_emotions, ret_score= summary_emotion(stats)
        topics, sub_topic = summary_situation(stats)
        badwords, badsentences = summary_badness(stats)
        relationships = summary_relationship(stats)

        return {
                'isSummary':True,
                   'summary':{
                       "emotion":{
                        "total":total_cnt,
                        'emotions': ret_emotions,
                        'emotion_score': ret_score,
                       },
                       'situation':{
                           'topic':topics,
                           'subtopic':sub_topic
                       },
                       "badness":{
                            "bad_words":badwords,
                            "bad_sentences":badsentences
                       },
                       'relationship':relationships
                    },
                    "statistics" : [stat.json() for stat in stats]
               }, 200


class RangeStatList(Resource):
    def get(self,end,begin):
        child_id = 1

        stats = StatisticModel.find_range_with_child_id(child_id, begin, end)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        total_cnt, ret_emotions, ret_score = summary_emotion(stats)
        topics, sub_topic = summary_situation(stats)
        badwords, badsentences = summary_badness(stats)
        relationships = summary_relationship(stats)


        return {
                   'isSummary': True,
                   'summary': {
                       "emotion": {
                           "total": total_cnt,
                           'emotions': ret_emotions,
                           'emotion_score': ret_score,
                       },
                       'situation': {
                           'topic': topics,
                           'subtopic': sub_topic
                       },
                       "badness": {
                           "bad_words": badwords,
                           "bad_sentences": badsentences
                       },
                       'relationship': relationships
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

        stats = StatisticModel.find_by_child_id(child_id)

        if not stats :
            return {
                'isSummary': False,
                "statistics": []
            }

        total_cnt, ret_emotions, ret_score = summary_emotion(stats)
        topics, sub_topic = summary_situation(stats)
        badwords, badsentences = summary_badness(stats)
        relationships = summary_relationship(stats)

        return {
                   'isSummary': True,
                   'summary': {
                       "emotion": {
                           "total": total_cnt,
                           'emotions': ret_emotions,
                           'emotion_score': ret_score,
                       },
                       'situation': {
                           'topic': topics,
                           'subtopic': sub_topic
                       },
                       "badness": {
                           "bad_words": badwords,
                           "bad_sentences": badsentences
                       },
                       'relationship': relationships
                   },
                   "statistics": [stat.json() for stat in stats]
               }, 200