# ------------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------------

from sys import meta_path
from flask import Flask, render_template, request
import numpy as np
import pandas as pd

import os
import sys
script_dir = os.path.dirname( __file__ )
sys.path.append(script_dir )
import functions_utils
#from .functions_utils.py import read_table, get_best, weighted_results_max
import json


# ------------------------------------------------------------------------
# CODE
# ------------------------------------------------------------------------

app = Flask(__name__)

data_summer_2020 = pd.read_csv(f'{os.getcwd()}/data/Olympic_Games_results_test.csv', index_col=0, sep = ';', encoding = "ISO-8859-1", low_memory=False)
data_winter_2022 = pd.read_csv(f'{os.getcwd()}/data/Olympic_Games_2022_results_v1.csv', index_col=0, sep = ',', encoding = "ISO-8859-1", low_memory=False)
#data_all = pd.read_csv(f'{os.getcwd()}/data/All_Olympic_Games_results.csv', index_col=0, sep = ',', encoding = "ISO-8859-1", low_memory=False)

#data_summer_2020 = data_summer_2020.rename(columns={'Sport':'Epreuve', 'Epreuve' : 'Sport'})
country_to_code = json.load(open(f"{os.getcwd()}/data/codes_countries.txt"))
code_to_country = {v: k for k, v in country_to_code.items()}

data_both = functions_utils.merge_data(data_summer_2020, data_winter_2022)

@app.route("/", methods = ['GET'])
def home(): 
    return render_template("index.html")

@app.route("/calculate", methods = ['GET', 'POST'])
def calculate(medals = 3, countries = 10, group = "normal", function = lambda x : x ): 
    dic_function = {'no_function': lambda x : x, 'square' : np.square, 'log' : lambda x : np.log(x+1), 'sqrt' : lambda x : np.sqrt(x)}
    dic_filter = {'individual':'normal', 'team':'team', 'group':'group'}
    dic_data = {'tokyo' : data_summer_2020 , 'pekin' : data_winter_2022, 'both' : data_both}
    param_data = request.form.get("data")
    param_function = request.form.get("function")
    param_group = request.form.get("filter")
    data = functions_utils.preprocess_data(dic_data[param_data], country_to_code, code_to_country)
    function =  dic_function[param_function]
    group =  dic_filter[param_group]
    if request.form['medals'] :
        medals = int(request.form['medals'])
    if request.form['countries'] : 
        countries = int(request.form['countries'])
    weight = request.form['btnradio']
    if  weight != 'no_weight' :
        print("with weight")
        res = functions_utils.weighted_results_max(data, weight, medals, countries, group, function)
    else : 
        if param_function == 'no_function':
            print("no weight and no function") 
            res = functions_utils.get_best(functions_utils.read_table (data, group, function), medals,countries, True)
        else : 
            print("no weight but function") 
            res = functions_utils.get_best(functions_utils.read_table (data, group, function), medals,countries, False)
    headings = tuple(['Country'] + [i for i in range(1,medals+1)]+['Total', 'Rank'])
    return render_template("dahsboard.html", headings = headings, data = res.reset_index().values, parameter = [param_data, param_function, param_group, medals, countries, weight])


if __name__ == '__main__':
    app.run()