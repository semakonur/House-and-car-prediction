from importlib.resources import Resource
from flask import request
from flask_restful import Resource
import pandas as pd
import housePricePredictionModel
import carPricePredictionModel
import jsonify

class HousePricePredictionApi(Resource):

    def get(self):

        args = request.args

        district = int(args['district'])
        net_area = int(args['net_area'])
        gross_area = int(args['gross_area'])
        room_count = int(args['room_count'])
        building_age = int(args['building_age'])
        floor_location = int(args['floor_location'])

        new_data = [[district], [net_area], [gross_area], [room_count], [building_age], [floor_location]]
        new_data = pd.DataFrame(new_data).T

        df_2 = new_data.rename(columns={0: "District",
                                       1: "Gross Square Meter",
                                       2: "Net Square Meter",
                                       3: "Number of Rooms",
                                       4: "Building Age",
                                       5: "Floor Location"})

        pred = housePricePredictionModel.model_xgb.predict(df_2)

        return str(pred) 

class CarPricePredictionApi(Resource):

    def get(self):

        args = request.args

        brand = int(args['brand'])
        model = int(args['model'])
        year = int(args['year'])
        fuel_type = int(args['fuel_type'])
        transmission = int(args['transmission'])
        engine_capacity = int(args['engine_capacity'])
        engine_power = int(args['engine_power'])
        km = int(args['km'])
        total_damage = int(args['total_damage'])

        new_data = [[brand], [model], [year], [fuel_type], [transmission], [engine_capacity], [engine_power], [km], [total_damage]]
        new_data = pd.DataFrame(new_data).T
        
        df_2 = new_data.rename(columns={0: "Brand",
                                        1: "Model",
                                        2: "Year",
                                        3: "Fuel Type",
                                        4: "Transmission",
                                        5: "Engine Capacity",
                                        6: "Engine Power",
                                        7: "Kilometer",
                                        8: "Total Damage Amount"})

        pred = carPricePredictionModel.model_xgb.predict(df_2)
    
        return str(pred)
