import json,numpy as np,pandas as pd
import pickle
import os
from flask import Flask,render_template
import CONFIG

class predictions():
    def __init__(self):
        print(os.getcwd())

    def load_raw(self):
        with open(CONFIG.MODEL_PATH,'rb') as model_file: 
            self.model = pickle.load(model_file)
    
        with open(CONFIG.ASSET_PATH,'r') as col_file: 
            self.column_names = json.load(col_file)   
            
    def predict_dep_del(self,data):
        self.load_raw()
        self.data = data
        user_input = np.zeros(len(self.column_names['Column Names']))
        array = np.array(self.column_names['Column Names'])
        DepTime = self.data['html_dt']
        CRSDepTime = self.data['html_cdt']
        ArrTime = self.data['html_at']
        CRSArrTime = self.data['html_cat']
        FlightNum = self.data['html_flightno']
        AirTime = self.data['html_airtime']
        ArrDelay = self.data['html_arrd']
        Origin = self.data['html_org']
        Dest = self.data['html_dest']
        Distance = self.data['html_dist']
        CarrierDelay = self.data['html_cd']
        LateAircraftDelay = self.data['html_lad']


        user_input[0] =DepTime
        user_input[1] =CRSDepTime
        user_input[2] =ArrTime
        user_input[3] =CRSArrTime
        user_input[4] =FlightNum
        user_input[5] =AirTime
        user_input[6] =ArrDelay

        Origin_string = 'Origin_'+Origin
        Origin_index = np.where(array == Origin_string)[0]
        user_input[Origin_index] = 1 

        dest_string = 'Dest_'+Dest
        dest_index = np.where(array == dest_string)[0]
        user_input[dest_index] = 1

        user_input[7] =Distance
        user_input[8] =CarrierDelay
        user_input[9] =LateAircraftDelay

        print(f"{user_input=}")
        print(len(user_input))

        dep_delay = self.model.predict([user_input])
        print(f"Predicted depature delay = {dep_delay}")
        print(f"Actual depature delay = 16")

        return render_template("air.html",PREDICT_DELAY=dep_delay)

if __name__ == "__main__":
     
    pred_obj=predictions()
    pred_obj.load_raw()