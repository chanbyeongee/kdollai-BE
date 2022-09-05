from flask_restful import Resource, reqparse
from models.chat import ChatModel
from models.child import ChildModel
from models.statistic import StatisticModel
from datetime import datetime,timedelta

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required
)

class RangeStatistic(Resource):
    parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, sday,eday):
        user_id = get_jwt_identity()

        child_id = ChildModel.find_by_user_id(user_id).id


        start = datetime.strptime(sday, "%Y%m%d")
        end = datetime.strptime(eday, "%Y%m%d")
        dates = [(start + timedelta(days=i)).strftime("%Y%m%d") for i in range((end - start).days + 1)]

        rets = [StatisticModel.find_by_child_id_and_day(child_id,day) for day in dates]


        #DO SOMETHING!


        if rets:
            return {ret.json() for ret in rets}, 200
        return {'message': 'Chat not found'}, 404

class ListStatistic(Resource):
    parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, sday,eday):
        user_id = get_jwt_identity()

        child_id = ChildModel.find_by_user_id(user_id).id

        start = datetime.strptime(sday, "%Y%m%d")
        end = datetime.strptime(eday, "%Y%m%d")
        dates = [(start + timedelta(days=i)).strftime("%Y%m%d") for i in range((end - start).days + 1)]

        rets = [StatisticModel.find_by_child_id_and_day(child_id, day) for day in dates]

        if rets:
            return {ret.json() for ret in rets}, 200
        return {'message': 'Chat not found'}, 404
